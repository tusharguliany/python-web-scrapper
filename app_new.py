# Python v3.7.1

# Before running this script, you'll need python package for beautiful soup
# Run the next line in cmd without the #
# pip install beautifulsoup4

# Imports the Library for Scraping through the Webpage
from bs4 import BeautifulSoup as soup

# Imports the urlopen module to fetch Web Pages
from urllib.request import urlopen as uReq

# imports the time module, used to write time to file in this program
import time

import csv

# url for the web scrapping
myUrl='https://www.cbc.ca/'

#saves the time in the modern format in the asc format
localtime = time.asctime( time.localtime(time.time()) )

# opens the file with "newsArticles.csv" name
# File opens in the append+ mode which takes the cursor to the end of the file and if the file doesn't exist, it creates the file in the working   # directory
filename="newsArticles.csv"
f= open(filename,"a+")

# Writes the date and title as header
headers= ["S.No.","Titles"]
date=['Date',localtime]
writer=csv.writer(f)
writer.writerow(date)
writer.writerow(headers)

# Prints the url to the console
print(myUrl)

# fetches the webpage by opening a connection and closing it after it has been read
# NOTES:
# Internet Connection is required for the next 3 lines to work
uClient= uReq(myUrl)
pageHTML= uClient.read()
uClient.close()

# scrapes the fetched data by BeautifulSoup's inbuild library
pageSoup= soup(pageHTML, "html.parser")

# searches and stores in the form of a list, the fetched and scrapped data for all the instances of divs with class of card
cards= pageSoup.find_all("a",class_="card")

# initializes the loop with counter as i inside the cards of data 
i=1
for card in cards:
    # loop runs till an exception of out of bounds is encountered
    try:
        # Next 5 lines are used to fetch the data in cardText as string
        cardText= card.find_all("div",class_="contentWrapper")
        cardText=cardText[0].find_all("div",class_="card-content")
        cardText=cardText[0].find_all("div",class_="card-content-top")
        cardText=cardText[0].find_all("h3",class_="headline")
        cardText= cardText[0].text

        # stores the headline in the csv file by first fetching the data and prefix as the number variable and incrementing the number in the next # line
        row= [i,cardText]
        # f.write(str(i)+".\t "+cardText + "\n")
        writer.writerow(row)

        i= int(i)+1

    except:
        # Breaks out of the loop in case of an exception
        break

# Writes the content with 3 new lines as a gap between the next instance of data when program runs again
# f.write("File Closed\n\n\n")

#closes the file
f.close()