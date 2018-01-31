import Scrape 
# Imports the Scrape script, responsible for getting the link and hyperlinks
import Compare
# Imports the Compare script, responsible for compring the links to the links in the database

'''
Importing the TKinter for creating a basic GUI
'''
from tkinter import *
from tkinter import ttk


def checkDomain():
    # Check the URL of the given website, by invoking the check function in the Compare script
    fo = open('title.txt')
    link = fo.readline().rstrip("\n")
    fo.close()
    # Reading from the 'title.txt' file for the link of the site
    ret = Compare.check(link)
    # Store the return value of the check function in the Compare script
    if ret==1:
        return True
    else:
        reasons.set(Compare.check(link))
        # Set the reasons variable (which is tkinter StringVar() type) to the justification
        return False


def checkLinks():
    # Check the domain of all the hyperlinks in the given URL
    fo = open('links.txt')
    for line in fo:
        # Call the getStrippedLink function in the Scrape script, to get only the domain of the hyperlinked URL 
        link = Scrape.getStrippedLink(line)
        if not Compare.check(link):
            return False
    return True


def result(link):
    # Main function for invoking all the respective scripts
    link = str(link)
    Scrape.starter(link)
    # Call the starter function in the Scrape script, which runs the Scrape script compeletely
    global results
    # Set the 'results' variable as global, so that it does not the shadow the already defined 'results' variable
    if checkDomain():
        if checkLinks():
            results.set("This site is not a fake news site")
            # If the response is True, none of the hyperlinked URLs are present in the database
        else:
            results.set("This site has sources from a fake site")
            # If the response is False, one or more hyperlinked URLs are present in the database
    else:
        results.set("This site is a fake news site")

'''
Creating a basic GUI in TKinter
''''           
root = Tk()
# Intialse root with a Tk object
root.title("FakeNews")
# Set the title of the GUI windows as 'FakeNews'

'''
Declare the necessary variables:
link = Stores user input URL
results = Stores the result of the 'result' function
reasons = Stores the reason for the domain being in the database
'''
link = StringVar()
results = StringVar()
reasons = StringVar();
reasons.set("N/A")
# Define a default value for reasons as 'N/A'

'''
Create a grid for the GUI. The 'root' variable is the Tk object which is used to create the GUI frame.
Padding sets the maximum grid space
'''
mainframe = ttk.Frame(root, padding="6 6 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

''' 
Create the input label (ttk.Label) and the text box (ttk.Entry).
The grid function assigns the position to the object and the sticky option sets the direction
'''
ttk.Label(mainframe, text="Input").grid(column=0, row=2, sticky=W)
word_entry = ttk.Entry(mainframe, width=55, textvariable=link)
word_entry.grid(column=1, row=2, sticky=(W, E))

'''
Creates the 'Run' button. The command parameter is executed when the button is pressed.
lambda function is used to prevent the ttk button from the calling the function, with an
empty value, during the initialisation of the GUI
'''
ttk.Button(mainframe, text="Run", command=lambda: result(link.get())).grid(column=3, row=6, sticky=W)

# Create the result text field with the 'results' variable value
ttk.Label(mainframe, text="Result :").grid(column=0, row=4, sticky=W)
ttk.Label(mainframe, textvariable=results).grid(column=1, row=4, sticky=(W, E))

# Create a reason text field for displaying the value of the 'reason' variable
ttk.Label(mainframe, text='Reason:').grid(column=0, row=5, sticky=W)
ttk.Label(mainframe, textvariable=reasons).grid(column=1, row=5, sticky=(W, E))

# Configures the x and y padding of the GUI
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

# The main executing loop
root.mainloop()
