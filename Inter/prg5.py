# testing materials
import qrcode
import cv2
import pyzbar
from pyzbar.pyzbar import decode

color = ["black","white"]
def qrGenerator(bd,bx):
    qr = qrcode.QRCode(
        version=1,
        border=bd,
        box_size=bx,
        error_correction=qrcode.constants.ERROR_CORRECT_L
    )
    return qr

def qrInput():
    wow = input("Enter the content of qr ~ ")
    b_size = input("Enter Custom border size ~ ")
    box_size = input("Enter Custom box size ~ ")
    c_c = input("need Diffrent Color Combinations ?? y/n ~ ").lower()
    if c_c == "y":
        f_c = input("giv fill color ~ ")
        b_c = input("giv background color ~ ")
    else:
        print(f"By default colors :{color[0]}, {color[1]} ")
        f_c = color[0]
        b_c = color[1]
    qr = qrGenerator(b_size,box_size)
    qr.add_data(wow)
    qr.make(fit=True)
    img = qr.make_image(fill_color=f_c,back_color=b_c)
    img.save("wow_QR.png")
    print("img saved")

qrInput()


def Read_QR():
    Read = cv2.imread("wow_QR.png")
    Decode = decode(Read)
    for x in Decode:
        print("Data: ",x.data)

def Choose_read():
    Wanna_read_Data = input("Wanna Read Data : ? y/n ~ ").lower()
    if Wanna_read_Data == "y":
        Read_QR()
    elif Wanna_read_Data == "n":
        print("Bie")
    else:
        print("Invalid option ~")
        Choose_read()

Choose_read()
