import pytesseract

# https://tesseract-ocr.github.io/tessdoc/Data-Files
# Error opening data file /usr/local/share/tessdata/chi_sim.traineddata
from src.utils.utils import utils

try:
    import Image
except ImportError:
    from PIL import Image

image_path = utils.getDataDir("/images/gushi.png")

# CASE 1
# image = Image.open(image_path)

# 对图片进行阈值过滤,然后保存
# image = image.point(lambda x: 0 if x<143 else 255)
# image.save('./new.png')

# lang 指定中文简体
# text = pytesseract.image_to_string(image, lang='chi_sim')
# print(text)

# CASE 2
# 通过text文件批量处理图片
# text = pytesseract.image_to_string('../../../../data/images/images.txt', lang='chi_sim')
# print(text)

# CASE 3
# 直接通过图片路径处理图片，跳过Image open
# text = pytesseract.image_to_string(image_path, lang='chi_sim')
# print(text)

# CASE 4
# Get verbose data including boxes, confidences, line and page numbers
# print(pytesseract.image_to_data(image_path, lang="chi_sim"))

# CASE 5
# Get information about orientation and script detection
# print(pytesseract.image_to_osd(image_path, lang="chi_sim"))

# CASE 6
# Get a searchable PDF
# pdf = pytesseract.image_to_pdf_or_hocr(image_path, extension='pdf')
# with open('test.pdf', 'w+b') as f:
#    f.write(pdf) # pdf type is bytes by default

# CASE 7
# Get HOCR output
# hocr = pytesseract.image_to_pdf_or_hocr(image_path, extension='pdf')
# print(hocr)






