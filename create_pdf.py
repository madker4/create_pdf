# -*- coding: utf-8 -*-
import csv
import sys
import jinja2
import argparse
import hours_to_string as hts
from xhtml2pdf import pisa

arg_pars = argparse.ArgumentParser()
arg_pars.add_argument("--name","-n",type = str,help = 'name csv file')
arg_pars.add_argument("--template","-t",type = str,default = '.',help = 'path to template')
arg_pars.add_argument("--pdf","-p",type = str,default = '.',help = 'path to pdf file')

input_file = open("data.csv","r")
reader = csv.DictReader(input_file,delimiter = ';',
                        skipinitialspace = 'TRUE',
                        restkey = 'Error_key',
                        restval = 'Error_value')
env = jinja2.Environment(loader = jinja2.FileSystemLoader('.'))
template = env.get_template("tmplt.html")

for row in reader:
    if 'Error_key' in row:
        print 'too many parameters ',row['Number'] 
        continue
    if 'Error_value' in row.values():
        print 'too few parameters ',row['Number'] 
        continue
    
    tmpl_str = template.render(Number = row['Number'].decode('utf-8'),
                                   FIO = row['FIO'].decode('utf-8'),
                                   DtFrom = row['DtFrom'].decode('utf-8'),
                                   DtTo = row ['DtTo'].decode('utf-8'),
                                   Programm = row['Programm'].decode('utf-8'),
                                   Module = row['Module'].decode('utf-8'),
                                   Hours = row['Hours'].decode('utf-8') + hts.hours_2_str(row['Hours']))
    name_pdf = row['Number'] + ".pdf"
    ##out_file = open(name_pdf,'w+b')
    pisa.showLogging()    
    pisa.CreatePDF(tmpl_str.encode('utf-8'),file(name_pdf,'wb'))    
    ##out_file.close()
    
    


    


        


