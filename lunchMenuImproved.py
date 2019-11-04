###
###  Francis Parker Lunch menu downloader and parser, improved
###  By Jake Boxerman
###  Original Sep. 2019, improved Oct. 2019
###

import pdftotext
from six.moves.urllib.request import urlopen
import io
import sys

# Getting the lunch menu PDF and putting it into a variable
url = 'https://fwparker.myschoolapp.com/ftpimages/1048/download/download_3453838.pdf'
remote_file = urlopen(url).read()
memory_file = io.BytesIO(remote_file)
pdf = pdftotext.PDF(memory_file)
pdf_content = pdf[0]

# Getting the requested day
day_requested = str(sys.argv[1]).title()

# Turning the string into list (each word is its own element)
menu = pdf_content.split()

# Creating dictionary to hold the location of each day's meal list in the list
dict = {"Monday:": 0, "Tuesday:": 0, "Wednesday:": 0, "Thursday:": 0, "Friday:": 0}

# Removing weird unicode chars (bullet points)
for item in menu:
    if item == "\uf0b7":
        menu.remove(item)

# Finding and setting the location of each day's meal list beginning
for day, spot in dict.items():
    dict[day] = menu.index(day)

#day_requested = input("What day do you want to know the menu for? ")
#day_requested = day_requested.title()
# Finding and setting the end of each day's meal list. Could probably be shorter.
if day_requested == "Monday":
    end_day_pos = menu.index("Tuesday:")
elif day_requested == "Tuesday":
    end_day_pos = menu.index("Wednesday:")
elif day_requested == "Wednesday":
    end_day_pos = menu.index("Thursday:")
elif day_requested == "Thursday":
    end_day_pos = menu.index("Friday:")
elif day_requested == "Friday":
    end_day_pos = len(menu)

# Printing the menu/outputting your selection
print(' '.join(menu[dict.get(day_requested + ":"):end_day_pos]))