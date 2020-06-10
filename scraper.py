import PyPDF2

pdfFile = open('teast.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFile)
page_count = pdfReader.numPages
pageObj = pdfReader.getPage()
print(pageObj.extractText())


#sites to monitor, dictionary of site name and date
#9/6 = 0
# 9/7 = 1
# 9/8 = 2
# 9/9 = 3
# 9/10 = 4

sites = {}

sites['Renegade'] = 4


pdfFile.close()
