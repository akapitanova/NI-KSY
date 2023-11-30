from PIL import Image
import os

def reduce_resolution(input_path, output_path):
    try:
        original_image = Image.open(input_path)
        original_width, original_height = original_image.size

        new_width = original_width // 4
        new_height = original_height // 4

        reduced_image = original_image.resize((new_width, new_height), Image.BICUBIC)

        reduced_image.save(output_path, format="PNG")

        print(f"Resolution reduced successfully. Image saved as {output_path}")

    except Exception as e:
        print(f"Error reducing resolution: {e}")

if __name__ == "__main__":
    for file in os.listdir("./train/0"):
        reduce_resolution("./train/0/" + file, "./train/0/" + file)
    for file in os.listdir("./train/1"):
        reduce_resolution("./train/1/" + file, "./train/1/" + file)
    for file in os.listdir("./test/0"):
        reduce_resolution("./test/0/" + file, "./test/0/" + file)
    for file in os.listdir("./test/1"):
        reduce_resolution("./test/1/" + file, "./test/1/" + file)