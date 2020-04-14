# -*- coding: utf-8 -*-
# clipboard.py

from AppKit import NSPasteboard, NSPasteboardTypePNG, NSPasteboardTypeTIFF, NSPasteboardTypePDF, NSPasteboardTypeString
from objc._pycoder import NSArray


def get_paste_img_file():
    """
    将剪切板数据保存到本地文件并返回文件路径
    """
    pb = NSPasteboard.generalPasteboard()  # 获取当前系统剪切板数据
    data_type = pb.types()  # 获取剪切板数据的格式类型
    # print(pb)
    # print(data_type)

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

def writeToFile(type):
    print("type: " + type)
    pb = NSPasteboard.generalPasteboard()
    data = pb.dataForType_(type)
    filename = type
    filepath = '/tmp/%s' % filename
    ret = data.writeToFile_atomically_(filepath, False)
    if ret:
        return filepath

def setClip (text):
    pb = NSPasteboard.generalPasteboard()
    pb.clearContents()
    # TODO 如果传入图片
    a = NSArray.arrayWithObject_(text)
    return pb.writeObjects_(a)

if __name__ == '__main__':
    text = "激战"
    setClip(text)
    # bytes字节符，打印以b开头。
    print(bytes(get_paste_img_file()).decode("utf-8"))