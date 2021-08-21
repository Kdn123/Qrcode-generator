import pyqrcode
 
def qrgenerator(data1):
    data = data1.replace(" ","_")
    qr = pyqrcode.create(data)
    file_name = data+".png"
    qr.png(file_name, scale=6)
    print("QR code is ready")
    print(data)

print("contact no")

data1 = input("Enter the data: ")
qrgenerator(data1)