import tika
tika.initVM()
from tika import parser
parsed = parser.from_file('/Users/kevinle/PycharmProjects/ufo-ocr-image-captioning/british-ufo-files/DEFE-24-1922/outtxt/12.txt')
print(parsed["metadata"])
print(parsed["content"])