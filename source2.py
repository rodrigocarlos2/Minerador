
from PyPDF2 import PdfFileWriter, PdfFileReader

output = PdfFileWriter()

ipdf = PdfFileReader(open('pdf1.pdf', 'rb'))
wpdf = PdfFileReader(open('pdf1.pdf', 'rb'))
watermark = wpdf.getPage(0)

for i in range(ipdf.getNumPages()):
	page = ipdf.getPage(i)
	page.mergePage(watermark)
	output.addPage(page)

with open('newfile.pdf', 'wb') as f:
	output.write(f)