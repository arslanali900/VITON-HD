from PIL import Image

# Open the image
image = Image.open("VITON-HD/datasets/test/image/00891_00_bu.jpg")  # Replace "input_image.jpg" with the path to your image file

rgb_image = image.convert('RGB')
# Resize the image to 1024x768
resized_image = rgb_image.resize((768, 1024))
# Save the resized image
resized_image.save("VITON-HD/datasets/test/image/00891_00.jpg")  # Replace "output_image.jpg" with the desired path and name for the output image file
