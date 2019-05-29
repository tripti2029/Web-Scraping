#Importing necessary libraries


from bs4 import BeautifulSoup 
import pandas as pd
import reimport csv
import requests

r= []
c= []
s=[]
e=[]
cen=[]
chan=[]
l=[]
p=[]
l=[]

#Accessing Wikepedia page

URL="https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population"
response=requests.get(URL)
soup=BeautifulSoup(response.text, 'html.parser')

#Accessing table from Wikepedia page

table=soup.find('table',{'class':'wikitable '}).tbody
rows=table.find_all('tr')

for i in rows[1:]:
    i=str(i)
    row_split = row.split('</td>')
    r = row_split[0].replace('<tr>\n<td>','')
    r.append(r)
    rawc = re.sub('<a.*title=','',re.sub('</a.*</sup>','',re.sub('<td style.*title=','',row_split[1]).replace('<td align "left">','')))
    cleancity = rawc.split('>')[1].replace('</a','').replace('\n','')
    c.append(cleancity)
    raws = re.sub('<a.*title>','',re.sub('<td.*span>','',re.sub('<a.*wiki/','',row_split[2])))
    cleans = raws.split('"')[0].replace('\n','')
    s.append(cleans)
    rawe= re.sub('<td.*">','',row_split[3])
    cleane=rawe.replace('\n','')
    estimate.append(cleane)
    cleancen = re.sub('<td.*;">','',row_split[4]).replace('\n','')
    cen.append(cleancen)
    rawchan = re.sub('<td.*">','',row_split[5])
    cleanchan =rawchan.split('%')[0].replace('\n','')
    chan.append(cleanchan)
    rawl= re.sub('<td.*">','',row_split[6])
    cleanl = rawl.split("'")[0].replace('\n','')
    l.append(cleanl)
    rawp = re.sub('<td.*">','',row_split[7])
    cleanp = rawp.split("'")[0].replace('\n',' ')
    p.append(cleanp)
    rawl = re.sub('<td.*location">','',row_split[10])
    cleanl = rawl.split("</span>")[0].replace('\n','')
    l.append(cleanl)

    
    
data = pd.DataFrame({"rank":r,"City":c,"State":s,"Estimate":e,"Census":cen,"Change":chan,"land area":l,"population density ":p,"Location":l})
data.to_csv('Topos.csv')
