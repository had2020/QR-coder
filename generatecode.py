import qrcode
import datetime

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

    #image path
    time_obj = str(datetime.datetime.now())
    stringged_url = str(url)
    image_folder = "qr-code-pngs/"
    image_name = stringged_url + time_obj
    image_path = image_folder + image_name + ".png"

    # create image for code
    img = qr.make_image(fill='black', back_color='white')
    img.save(image_path)

    return(image_path)
