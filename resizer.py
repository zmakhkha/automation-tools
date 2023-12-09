from PIL import Image
import sys

def resize_image(input_path, output_path, target_width):
    # Open the image
    original_image = Image.open(input_path)

    # Calculate the proportional height based on the target width
    target_height = int((target_width / float(original_image.size[0])) * original_image.size[1])

    # Resize the image
    resized_image = original_image.resize((target_width, target_height))

    # Save the resized image
    resized_image.save(output_path)

    print(f"Image resized and saved to {output_path}")

def main():
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 4:
        print("Usage: python resize_image.py <input_path> <output_path> <target_width>")
        sys.exit(1)

    # Get command-line arguments
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    target_width = int(sys.argv[3])

    # Resize the image
    resize_image(input_path, output_path, target_width)

if __name__ == "__main__":
    main()
