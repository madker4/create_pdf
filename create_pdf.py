import csv
import sys
import jinja2
import hours_to_string as hts
import pdfcrowd   
input_file = open("data.csv","r",encoding = 'utf-8')
reader = csv.DictReader(input_file,delimiter = ';',
                        skipinitialspace = 'TRUE',
                        restkey = 'Error_key',
                        restval = 'Error_value')
env = jinja2.Environment(loader = jinja2.FileSystemLoader('template'))
template = env.get_template("tmplt.html")
client = pdfcrowd.Client('madker4','1da7d8f6a609d9676c4cd6aad0a804d3')
for row in reader:
    if 'Error_key' in row:
        print('too many parameters ',row['Number'])
        continue
    if 'Error_value' in row.values():
        print('too few parameters ',row['Number'])
        continue
    tmpl_str = template.render(Number = row['Number'],
                                   FIO = row['FIO'],
                                   DtFrom = row['DtFrom'],
                                   DtTo = row ['DtTo'],
                                   Programm = row['Programm'],
                                   Module = row['Module'],
                                   Hours = row['Hours']+hts.hours_2_str(row['Hours']))
    name_pdf = row['Number'] + '.pdf'
    out_file = open(name_pdf,'wb')
    pdf = client.convertHtml(tmpl_str,out_file)
    out_file.close()
    
    


    


        


