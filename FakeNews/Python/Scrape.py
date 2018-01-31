import urllib.request
import urllib.error
from urllib.parse import urlparse
# Import the urllib2 libraries necessary for operating with the URLs
from bs4 import BeautifulSoup
# Import BeautifulSoup4 library for parsing the HTML response

accepted_scheme = ['http://', 'https://', 'ftp']
# Create a list of accepted connection types

def getStrippedLink(link):
    # Used to generate a string with only the domain
    parse = urlparse(link)
    # Parse the given link as a URL
    stripped_link = parse[1]
    # Get the domain specific string from the list 'parse'
    if 'www.' in link or 'http://' in link or 'https://' in link:
        # Check for the given strings in the link and remove them 
        stripped_link = stripped_link.strip('https://').strip('http://').strip('www.')
    return stripped_link


def openURL(link):
    # Create a Request object for the given link, with a user-agent specified 
    web_link = urllib.request.Request(link, data=None, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        handle = urllib.request.urlopen(web_link)
        # Attempt to connect to the URL and store the HTML GET response in 'handle' variable
    except urllib.error.HTTPError:
        print("Page unavailable")
        exit()
    return handle


def fileTitleWrite(soup, link):
    # Write the domain and title to the 'title.txt' file
    fo = open("title.txt", "w")
    fo.write(link + "\n")
    fo.write(soup.title.text)
    fo.close()


def fileLinkWrite(soup, parse):
    # Write the hyperlinked URLs to the 'links.txt' file
    fo = open("links.txt", "w")
    for link in soup.findAll('a'):
        # Find all the 'a' tags
        if 0 <= str(link.get('href')).find(str(parse[1])):
            # Find the tags with 'href' and which do not match to given link's domain 
            continue
        else:
            for s in accepted_scheme:
                if 0 <= str(link.get('href')).find(s):
                    # If accepted connection type, write the hyperlink to the file
                    fo.write(str(link.get('href')) + "\n")
    fo.close()


def starter(link):
    # Runs the entire script
    stripped_link = getStrippedLink(link)
    page = openURL(link)
    res = page.read()
    #Parse the pase into res
    soup = BeautifulSoup(res, "html.parser")
    #Use BeautifulSoup to create a nested data structure out of the HTML file of the website
    fileTitleWrite(soup, stripped_link)
    fileLinkWrite(soup, urlparse(link))
