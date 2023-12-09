from PIL import Image
import os
import sys
import csv
from concurrent.futures import ProcessPoolExecutor

def resize_image(input_path, output_folder, target_width):
    original_image = Image.open(input_path)

    target_height = int((target_width / float(original_image.size[0])) * original_image.size[1])

    resized_image = original_image.resize((target_width, target_height))

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    output_path = os.path.join(output_folder, os.path.basename(input_path))
    resized_image.save(output_path)

    print(f"Image resized and saved to {output_path}")

    return output_path

def resize_images_in_folder(input_folder, output_folder, target_width, csv_file):
    # Get a list of all files in the input folder
    input_files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]

    output_paths = []

    with ProcessPoolExecutor() as executor:
        # Resize each image in the input folder using multiple processes
        futures = {executor.submit(resize_image, os.path.join(input_folder, input_file), output_folder, target_width): input_file for input_file in input_files}

        # Wait for all processes to complete
        for future in futures:
            try:
                output_path = future.result()
                output_paths.append(output_path)
            except Exception as e:
                print(f"Error processing image: {e}")

    # Write output paths to a CSV file
    with open(csv_file, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow("Output Path")
        for output_path in zip( output_paths):
            csv_writer.writerow(output_path)

def main():
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 5:
        print("Usage: python resize_images.py <input_folder> <output_folder> <target_width> <csv_file>")
        sys.exit(1)

    # Get command-line arguments
    input_folder = sys.argv[1]
    output_folder = sys.argv[2]
    target_width = int(sys.argv[3])
    csv_file = sys.argv[4]

    # Resize images in the input folder, save in the output folder, and generate a CSV file
    resize_images_in_folder(input_folder, output_folder, target_width, csv_file)

if __name__ == "__main__":
    main()
