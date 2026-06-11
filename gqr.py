import qrcode

# Alteração necessária: link apontando para o projeto correto
link = "https://rareblack777.github.io/resineimcz/social.html"

qr = qrcode.QRCode(version=1, box_size=15, border=2)
qr.add_data(link)
qr.make(fit=True)

img = qr.make_image(fill_color="#d4af37", back_color="#0a0f14")
img.save("qrcode_siga_resinei.png")

print("QR Code gerado com sucesso!")