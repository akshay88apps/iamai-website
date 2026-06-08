from PIL import Image

SOURCE = "grow10x-logo.png"

# The source logo is a wide image (icon mark + wordmark) on a light background.
# The icon mark (circular arrow/network graphic) sits left-of-center; crop a
# square region around it so it can stand alone as a favicon.
CROP_BOX = (210, 225, 570, 585)  # (left, top, right, bottom) -> 360x360 square

img = Image.open(SOURCE).convert("RGBA")
icon = img.crop(CROP_BOX)

# favicon.ico (32x32)
icon.resize((32, 32), Image.LANCZOS).save("favicon.ico", format="ICO", sizes=[(32, 32)])

# favicon-96x96.png
icon.resize((96, 96), Image.LANCZOS).save("favicon-96x96.png", format="PNG")

# apple-touch-icon.png (180x180)
icon.resize((180, 180), Image.LANCZOS).save("apple-touch-icon.png", format="PNG")

print("Generated favicon.ico, favicon-96x96.png, apple-touch-icon.png")
