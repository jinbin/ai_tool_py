# -*- coding: utf-8 -*-
# clipboard.py

from AppKit import NSPasteboard, NSPasteboardTypePNG, NSPasteboardTypeTIFF, NSPasteboardTypePDF, NSPasteboardTypeString
from objc._pycoder import NSArray
from PIL import Image

from src.utils.utils import utils

def get_paste_img_file():
    """
    将剪切板数据保存到本地文件并返回文件路径
    """
    pb = NSPasteboard.generalPasteboard()  # 获取当前系统剪切板数据
    data_type = pb.types()  # 获取剪切板数据的格式类型

    # 根据剪切板数据类型进行处理
    if NSPasteboardTypePNG in data_type:          # PNG处理
        data = pb.dataForType_(NSPasteboardTypePNG)
        return data
    elif NSPasteboardTypeTIFF in data_type:         #TIFF处理： 一般剪切板里都是这种
        data = pb.dataForType_(NSPasteboardTypeTIFF)
        return data
    elif NSPasteboardTypeString in data_type:
        data = pb.dataForType_(NSPasteboardTypeString)
        return data
    elif NSPasteboardTypePDF in data_type:
        # string todo, recognise url of png & jpg
        print("NSPasteboardTypePDF")
        pass

# 将剪切板数据写入到指定文件
def writeToFile(data):
    filepath = '/tmp/%s' % "test.file"
    ret = data.writeToFile_atomically_(filepath, False)
    if ret:
        return filepath

# 设置剪切板的内容
# TODO 目前只支持String，图片等还需要另外支持
def setClip (text):
    pb = NSPasteboard.generalPasteboard()
    pb.clearContents()
    # TODO 如果传入图片
    a = NSArray.arrayWithObject_(text)
    return pb.writeObjects_(a)

# 将bytes数据还原为图片
def image_from_bytes(raw):
    from_img = Image.frombytes(img.mode, img.size, raw)
    return from_img

if __name__ == '__main__':
    text = "激战"
    setClip(text)
    # bytes字节符，打印以b开头。
    # encode() will result in a sequence of bytes. decode() decodes a stream of bytes to a string object
    # bytes([source[, encoding[, errors]]]): source to initialize the array of bytes. if source is a string, the encoding of the string.
    print(bytes(get_paste_img_file()).decode("utf-8"))

    data = get_paste_img_file()
    writeToFile(data)

    # 将bytes数据还原为图片
    # TODO 如何将剪切板获取的数据转成合适的bytes
    img = Image.open(utils.getDataDir("/images/gushi.jpeg"))
    raw = img.tobytes()

    img_out = image_from_bytes(raw)
    img_out.show()