#importing all the libraries which will be used
from bs4 import BeautifulSoup
import requests
import csv
#imorting the header file using a server proxy to scarpe the data 
header = {
  "User-Agent":
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15"
}

user_id=str(input("Please enter your user id"))#get googlescholar id from tthe user
url = "https://scholar.google.co.in/citations?user="+user_id +"=en"#making the url to scrape data from
response = requests.get(url, headers=header)#using the response function to ger the webpage

soup = BeautifulSoup(response.content, 'lxml')
main_list=[]#declaring main_list to store all the parameters 
for item in soup.select('.gsc_a_tr'):

  side_list=[]#declaring summy list
  
  project_title=(item.select('a')[0].get_text())#scrape the project title from a tab
  
  link_of_project=(item.select('a')[0]['href'])#usl stored in variable link_of_project
  link_of_project='https://scholar.google.com'+link_of_project
  
  collaborators=(item.select('.gs_gray')[0].get_text())#storing all  the collabiorators in 
  #variable collabororator
  
  year=(item.select('.gs_oph')[0]) #declaring year variable to declare the year of publication
  year=str(year)
  year=year[-11:-7]
  year=int(year)
  #                                  _________
  side_list.append(project_title)#            |
  side_list.append(link_of_project)#          | adding all the parameters to the side list
  side_list.append(collaborators)#            |
  side_list.append(year)#            _________|                   
  
  main_list.append(side_list) #adding side list as an input of main list
#exiting loop

for i in range(20):#20 max no of range known till now more to be added in the next version 
  #                                 _____________________
  print("TITLE : "+main_list[i][0])   #                 |
  print('')#                                            |
  print("LINK : "+main_list[i][1])#                     |
  print('')#                                            | Formating the outout 
  print("COLLLABORATORS : "+main_list[i][2])#           |
  print('')#                                            |
  print('YEAR PUBLISHED : '+str(main_list[i][3]))#______|
  print("---------------------------------------------------------------------------------------------------------------------------")

#code to convert data into a csv file  using csv function
  with open('file.csv','w',newline='') as f:
    writer=csv.writer(f)
    writer.writerows(main_list)

