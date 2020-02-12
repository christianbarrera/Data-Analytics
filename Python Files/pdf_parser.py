import PyPDF2
import re

pdfFile = "sdge_bill.pdf"
pdfRead = PyPDF2.PdfFileReader(pdfFile)
page = pdfRead.getPage(2)
pageContent = page.extractText()
# print(pageContent[0:1000])

for i in range(0, pdfRead.getNumPages()):
	if "Electric" in pdfRead.getPage(i).extractText()[:1000]:
		print("works")
		break
	else:
		print("NEXT")

# print(pageContent)  

#  print(re.findall(r"Meter Number: [0-9]{8}", pageContent)[0][-8:])
# print(re.findall(r"Total Taxes & Fees on Electric Charges  \n(-\s*\$[0-9]*.?[0-9]{2})", pageContent)[0])

Meter_number = re.findall(r"Meter Number: [0-9]{8}", pageContent)[0][-8:]
taxes = re.findall(r"Total Taxes & Fees on Electric Charges  \n(-?\s*\$[0-9]*.?[0-9]{2})", pageContent)[0]
print("Meter number:", Meter_number.replace(" ", ""))
print("Electric Tax total amount:", taxes.replace(" ", ""))

