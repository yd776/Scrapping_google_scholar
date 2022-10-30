#importing all the libraries which will be used
from bs4 import BeautifulSoup
import re
import requests
import csv
import time
start_time=time.time()
#imorting the header file using a server proxy to scarpe the data 
header = {
  "User-Agent":
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15"
}

user_id=str(input("Please enter your user id"))#get googlescholar id from tthe user
start=0
#end=int(input("enter the max page size"))
end=1000
url = "https://scholar.google.com/citations?user="+ user_id+"&cstart="+str(start)+"&pagesize="+str(end)#making the url to scrape data from


response = requests.get(url, headers=header)#using the response function to ger the webpage

soup = BeautifulSoup(response.content, 'lxml')
main_list=[]#declaring main_list to store all the parameters 
links=[]

name1=(soup.select('div[id^=gsc_prf_inw]'))

name1=(str(name1))
name1=name1.split(">")
name1=name1[2]
name1=name1.split("<")
name1=name1[0]
name1=str(name1)


#name1=soup.find_all('div',attrs={'class': 'gsc_lcl'})
#for div in name1:
    #print(div.get_text(strip=True).encode("utf-8"))
'''for i in soup.select('.gs_bdy'):
  print(i)
  name1=soup.select('.gsc_prf_in')[0]
  print(name1)'''

for item in soup.select('.gsc_a_tr'):
  #print(item)

  side_list=[]#declaring summy list
  
  project_title=(item.select('a')[0].get_text())#scrape the project title from a tab
  #print(project_title)
  
  link_of_project=(item.select('a')[0]['href'])#usl stored in variable link_of_project
  link_of_project='https://scholar.google.com'+link_of_project
  
  
  collaborators=(item.select('.gs_gray')[0].get_text())#storing all  the collabiorators in 
  #variable collabororator
   #journal=(item.select('.gs_gray')[1].get_text())
  #print(journal)'''

  
  year=(item.select('.gsc_a_y')[0]) #declaring year variable to declare the year of publication

  year=str(year)
  year=year[-16:-12]

  ##add ur code here
 
  journal=(item.select(".gs_gray")[1].get_text()).replace(year,'').replace(',','')

  
  #print(year)
  #                                  _________
  side_list.append(project_title)
  side_list.append(link_of_project)#          | adding all the parameters to the side list
  links.append(link_of_project)
  side_list.append(collaborators)#            |
  side_list.append(year)#     _________|       
  side_list.append(journal)
  
  main_list.append(side_list) #adding side list as an input of main list
  #print(main_list)
#exiting loop
time_diff=time.time()-start_time
n=(len(main_list))
print('Scrapping time: %2f miliseconds.' % time_diff)
for i in range(n):#20 max no of range known till now more to be added in the next version 
  #                                 _____________________
  print(" ")
  
  print("TITLE : "+main_list[i][0])   #                 |
  print('')#                                            |
  print("LINK : "+main_list[i][1])#                     |
  print('')#                                            | Formating the outout 
  print("COLLLABORATORS : "+main_list[i][2])#           |
  print('')#                                            |
  print('JOURNAL NAME : '+main_list[i][4]) #___|
      #|
  print('') 
  #    |
  print('YEAR PUBLISHED : '+str(main_list[i][3]))#______|
 
  print("---------------------------------------------------------------------------------------------------------------------------")

#code to convert data into a csv file  using csv function
  with open(name1+'.csv','w',newline='') as f:
    writer=csv.writer(f)
    writer.writerows(main_list)
  

'''for i in links:
  header = {
  "User-Agent":
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko)     Version/12.1.1 Safari/605.1.15"}
  L=i
  r=requests.get(url=L,headers=header)
  
  soup = BeautifulSoup(r.content, 'lxml')
  
  for item in soup.select('.gs_el_ph gs_el_sm gs_el_tcZQLOLBMAAAAJ'):
    #print("hello")
    print(item)'''
    

