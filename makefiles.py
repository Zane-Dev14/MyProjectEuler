import os
import requests
from bs4 import BeautifulSoup
problem=1
url = "https://projecteuler.net/archives"
response = requests.get(url)    
def create_file():
    global problem
    if(problem>10):

        print("DOi ng")

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    # Parse and extract data using Beautiful Soup
    table_id="problems_table"
    table=soup.find('table',{'id':table_id})
    for i in table.find_all('a'):
        create_file()
        print(f"PE: {problem}- {i.text}")
        problem+=1

# savingto="/home/zane/Desktop/Code/git/MyProjectEuler"
# for i in range (1,101,15):
#     folder_Path=os.path.join(savingto,f"Project Euler: {i}-{i+14}")
#     if not os.path.exists(folder_Path): 
#         os.makedirs(folder_Path)
#         print(f"{savingto}/Project Euler: {i}-{i+14}")
    