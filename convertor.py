from PIL import Image
import os

def convert_tif_to_png(input_path, output_path):
    try:
        # Open the TIFF image
        tif_image = Image.open(input_path)

        # Convert and save as PNG
        tif_image.save(output_path, format="PNG")

        print(f"Conversion successful. Image saved as {output_path}")

    except Exception as e:
        print(f"Error converting image: {e}")
    
if __name__ == "__main__":
    tif_source = "./dataset_tif/"
    png_destination = "./dataset_png/"
    for file in os.listdir(tif_source):
        if file.endswith(".tif"):
            # Get the file name without extension
            file_name = os.path.splitext(file)[0]
            # Convert and save as PNG
            convert_tif_to_png(
                input_path=os.path.join(tif_source, file),
                output_path=os.path.join(png_destination, file_name + ".png")
            )