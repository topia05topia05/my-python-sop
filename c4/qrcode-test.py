import qacode

# QRコードを作成する
img = qacode.make("https://www.kujirahand.com")
#ファイルに保存
img.save("qrcode-test.png")