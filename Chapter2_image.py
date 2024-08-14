from PIL import Image

# Memuat gambar
image = Image.open('test.jpg')

cropped_image = image.crop((10, 10, 200, 200))
cropped_image.save('cropped_result.jpg')

resized_image = cropped_image.resize((100, 100))
resized_image.save('resized_result.jpg')


from PIL import ImageFilter

filtered_image = resized_image.filter(ImageFilter.BLUR)
filtered_image.save('filtered_result.jpg')

# Menyimpan gambar
image.save('test2.jpg')

from PIL import ImageFilter, Image

# Membuka gambar
image = Image.open('test2.png')

# Mengubah ukuran gambar
resized_image = image.resize((100, 100))

# Menambahkan efek blur
filtered_image = resized_image.filter(ImageFilter.BLUR)

# Menyimpan gambar hasil sebagai PNG tanpa perlu mengonversi mode warna
filtered_image.save('test2_result.png')

