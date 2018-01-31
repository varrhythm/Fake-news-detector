''' 
Used to work with CSV (Comma-separated Values) [https://en.wikipedia.org/wiki/Comma-separated_values] files, 
which our database file, sources.csv is in
'''
import csv


def check(domain):
# Used to check if the given 'domain' argument is present in the database
    with open('sources.csv', 'r') as csv_data:
        # Opens the file with a object as csv_data
        fields = csv.reader(csv_data)
        # Reads the column titles in the field
        for row in fields:
            # Reads the value in each row, into a list for columns
            if domain == row[0]:
                # Compares with the 0th element in the list 'row', which are the domain URLs
                return row[1]
                # Return the 1st element, which is the justification for the site being in the list
    return 1
    #return True if the URL is not present in the database
