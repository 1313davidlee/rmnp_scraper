import PyPDF2
import requests

pdf_url = 'https://www.nps.gov/webcams-romo/wo/sa-20200906.pdf'

  
r = requests.get(pdf_url, stream = True) 
  
with open("python.pdf","wb") as pdf: 
    for chunk in r.iter_content(chunk_size=1024): 
  
         # writing one chunk at a time to pdf file 
         if chunk: 
             pdf.write(chunk)


pdfFile = open('python.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFile)
page_count = pdfReader.numPages



#sites to monitor, dictionary of site name and date
#9/6 = 1
# 9/7 = 2
# 9/8 = 3
# 9/9 = 4
# 9/10 = 5

sites = []

sites.append(['Renegade', 5])
sites.append(['Sourdough', 4])
sites.append(['July', 1])
sites.append(['Pine Marten', 1])
sites.append(['North Inlet Junction', 1])
sites.append(['North Inlet Falls', 1])

prefix = 3

all_text = ''
for page in range(5):
    currPage = pdfReader.getPage(page)
    currPageText = currPage.extractText()
    all_text += currPageText

text_array = []
for line in iter(all_text.splitlines()):
    text_array.append(line)


for site in sites:
    site_name = site[0]
    target_day = site[1]
    line_count = 0
    for line in text_array:
        if site_name in line:
            if 'Group' not in line and 'mid' not in line and 'before' not in line:
                captured = text_array[line_count + prefix + target_day]
                if captured == '1' or captured == '2':
                    print('there was an opening at ', site_name, '!')
                else:
                    print(site_name, 'still booked :(')
                #print('site status on target day', text_array[line_count + prefix + target_day])
        line_count += 1

pdfFile.close()
