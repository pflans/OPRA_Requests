import pyPdf
x = '10'
pdf = pyPdf.PdfFileReader(open(x+'.pdf', 'rb'))
c = 0
for page in pdf.pages:
	c = c + 1
	txt = open(x+'-'+str(c)+'.txt', 'w')
	txt.write(page.extractText().encode('UTF-8'))
	txt.close()