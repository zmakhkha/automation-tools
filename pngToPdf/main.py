import os
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PIL import Image

def convert_png_to_pdf(input_folder, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Process each PNG file in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".png"):
            input_path = os.path.join(input_folder, filename)

            # Open the PNG image using PIL
            img = Image.open(input_path)

            # Create a PDF canvas with the same dimensions as the image
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.pdf")
            pdf_canvas = canvas.Canvas(output_path, pagesize=img.size)

            # Draw the image on the PDF canvas
            pdf_canvas.drawInlineImage(input_path, 0, 0, width=img.width, height=img.height)

            # Save the PDF file
            pdf_canvas.save()
            print(output_path + " saved successfully !!")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input_folder output_folder")
        sys.exit(1)

    input_folder = sys.argv[1]
    output_folder = sys.argv[2]

    convert_png_to_pdf(input_folder, output_folder)
