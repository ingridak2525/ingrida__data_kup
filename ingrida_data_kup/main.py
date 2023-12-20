from lxml.etree import HTML
from requests import get
import csv

data= get("https://www.gintarine.lt").text
data= HTML(data)
medical_name= data.xpath("//a/img[contains(@class, 'category-grid__title')]/@alt")

medical_image=data.xpath("//a/img[contains(@class, 'img-responsive')]/@src")
medical_image_url=[]
for link in data.xpath("//a/img[contains(@class, 'img-responsive')]/@src"):
    medical_image_url.append("https://www.gintarine.lt" + link)

medical_page=data.xpath("//a[contains(@class,'vehicle-item fp-cta-gtm')]/@href")
medical_page_url=[]
for link in data.xpath("//a[contains(@class,'vehicle-item fp-cta-gtm')]/@href"):
   medical_page_url.append("https://www.gintarine.lt" + link)

with open("Medical.csv", "w") as file_writer:
    fieldnames=['Pavadinimas', 'Img', 'Linkas']
    csv_write = csv.DictWriter(file_writer, fieldnames, delimiter = ',')
    csv_write.writeheader()
    #csv_write.writerow
    for i in range(len(medical_name)):
        csv_write.writerow({"Pavadinimas": medical_name[i], "Img": medical_image_url[i], "Linkas": medical_page_url[i]})