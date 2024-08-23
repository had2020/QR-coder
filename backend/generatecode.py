import qrcode

# URL == string
def generate_qrcode(url):
    # QR code object
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # adding URL to object
    qr.add_data(url)
    qr.make(fit=True)

    # create image for code
    img = qr.make_image(fill='black', back_color='white')
    img.save("qr_code_with_link.png")
