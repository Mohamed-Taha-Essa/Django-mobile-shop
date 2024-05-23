from PIL import Image
import os

def convert_jpeg_to_jpg(input_paths):
    for input_path in input_paths:
        # Split the file path to get the file name without extension
        base_name = os.path.splitext(input_path)[0]
        # Create the output path with .jpg extension
        output_path = base_name + '.jpg'
        
        # Open the image file
        with Image.open(input_path) as img:
            # Save it with the .jpg extension
            img.save(output_path, 'JPEG')
            print(f"Converted {input_path} to {output_path}")

# List of paths to your input JPEG files
input_paths = [
    '01.jpeg', '02.jpeg', '03.jpeg', '04.jpeg', '05.jpeg',
    '06.jpeg', '07.jpeg', '08.jpeg', '09.jpeg', '10.jpeg',
    '11.jpeg', '12.jpeg', '13.jpeg', '14.jpeg', '15.jpeg',
    '16.jpeg', '17.jpeg', '18.jpeg', '19.jpeg', '20.jpeg',
    '21.jpeg', '22.jpeg'
]


# Convert all JPEG files to JPG
convert_jpeg_to_jpg(input_paths)
