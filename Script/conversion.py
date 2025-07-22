# Instal PIL from https://pypi.org/project/pillow/


import os
from PIL import Image


def type_conversion(source_path, destination_path):
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)

    
    for i in os.listdir(source_path):
        if i.lower().endswith(('.tif', '.tiff')):
            input_image_path = os.path.join(source_path, i)
            output_filename = os.path.splitext(i)[0] + '.jpg'
            output_image_path = os.path.join(destination_path,output_filename)

            try:
                with Image.open(input_image_path) as img:
                    img.convert('RGB').save(output_image_path, 'JPEG')
                    print(f"converted '{i} to '{output_filename}'")
            except Exception as e:
                print(f"Error converting '{i}': {e}")



    
print("Started to convert images from Insect Damage folder")
print("\n")
type_conversion(source_path = './InsectDamage', destination_path = './InsectDamageJPEGFolder')
print("Completed: converted images from Insect Damage folder")
print("\n")


print("Started to convert images from No Damage folder")
print("\n")
type_conversion(source_path = './NoDamage', destination_path = './NoDamageJPEGFolder')
print("Completed: converted images from No Damage folder")



