
# import module
import requests 
import bs4 
  
# Taking thecity name as an input from the user
city = "ai là người sáng lập google"
  
# Generating the url  
url = "https://google.com/search?q=" + city
  
# Sending HTTP request 
request_result = requests.get( url )

soup = bs4.BeautifulSoup( request_result.text  , "html.parser" )
  
    

temp = soup.find_all(class_="g")
    
with open("./text.txt", "w") as f:
    for i in temp:
        print(str(i))
        # f.write(str(i))
# print( temp ) 