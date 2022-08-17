from PIL import Image, ImageDraw
import xml.etree.ElementTree as ET

# Load image:
input_image = Image.open("cv-image-download/blink-03-03-06_1655959049.jpg")
input_pixels = input_image.load()

# Parse pascal voc xml
origin_coordinate_1 = []
origin_coordinate_2 = []
end_coordinate_1 = []
end_coordinate_2 = []
bbch = []

# Get coordinates
tree = ET.parse('cv-image-download/blink-03-03-06_1655959049.xml')
for bndbox in tree.iter(tag = 'bndbox'):
        xmin = bndbox.find('xmin').text
        ymin = bndbox.find('ymin').text
        xmax = bndbox.find('xmax').text
        ymax = bndbox.find('ymax').text
        origin_coordinate_1.append(xmin)
        origin_coordinate_2.append(ymin)
        end_coordinate_1.append(xmax)
        end_coordinate_2.append(ymax)

for i in range(len(origin_coordinate_1)):
        # Cropped area
        origin = (origin_coordinate_1[i], origin_coordinate_2[i])
        end = (end_coordinate_1[i], end_coordinate_2[i])

        # Create output image
        output_image = Image.new("RGB", (int(float(end[0])) - int(float(origin[0])), int(float(end[1])) - int(float(origin[1]))))
        draw = ImageDraw.Draw(output_image)

        # Copy pixels
        for x in range(output_image.width):
                for y in range(output_image.height):
                        xp, yp = x + int(float(origin[0])), y + int(float(origin[1]))
                        draw.point((x, y), input_pixels[xp, yp])

        output_image.save("cv-image-cropped/output_"+str(i)+".png")

