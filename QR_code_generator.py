import qrcode
from PIL import Image
from urllib.parse import quote

def generate_qr_code(link, image_path, output_path):
    # Encode the link
    encoded_link = quote(link, safe=':/')

    # Generate QR code with higher error correction
    qr = qrcode.QRCode(
        version=5,  # Increased version for more data capacity
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Higher error correction
        box_size=20,
        border=4,
    )
    qr.add_data(encoded_link)
    qr.make(fit=True)

    qr_code = qr.make_image(fill_color="black", back_color="white")

    # Open the image
    img = Image.open(image_path)

    # Resize the image to fit within the QR code
    max_size = (qr_code.size[0] // 2, qr_code.size[1] // 2)
    img.thumbnail(max_size, Image.ANTIALIAS)

    # Calculate position to center the image on the QR code
    position = ((qr_code.size[0] - img.size[0]) // 2, (qr_code.size[1] - img.size[1]) // 2)

    # Create a new image with RGBA mode
    new_img = Image.new("RGBA", qr_code.size, (255, 255, 255, 0))

    # Paste the image onto the new image, preserving the original colors
    new_img.paste(img, position)

    # Composite the new image onto the QR code
    qr_code = Image.alpha_composite(qr_code.convert("RGBA"), new_img)

    # Save the final image with the embedded QR code
    qr_code.save(output_path)

if __name__ == "__main__":
    link = "https://apps.apple.com/in/app/solution-time-cloud/id6468779113"
    image_path = "image.png"
    output_path = "output_qr_code4.png"

    generate_qr_code(link, image_path, output_path)
