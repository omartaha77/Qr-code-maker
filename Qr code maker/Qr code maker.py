import qrcode

x = input("please, enter your text: ")

rcodeImg = qrcode.make(x)

rcodeImg.save('qrImages/myQrcode.png')
