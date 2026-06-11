import qrcode

# O segredo: o link aqui é o da sua página própria (ex: seu-dominio.com/hub.html)
link_do_seu_hub = "https://seusite.com/hub.html" 

qr = qrcode.QRCode(version=1, box_size=15, border=2)
qr.add_data(link_do_seu_hub)
qr.make(fit=True)

img = qr.make_image(fill_color="#d4af37", back_color="#0a0f14")
img.save("qrcode_hub_resinei.png")