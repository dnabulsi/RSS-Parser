# Flask framework
from flask import Flask, render_template
# Used to parse the link
from feedparser import parse

# Turn this file into a Flask application
app = Flask(__name__)

# Route of "homepage"
@app.route("/")
def index():
    # Parse link for data, then set as value of parserResponse
    parserResponse = parse("https://www.rotanacareers.com/live-bookmarks/all-rss.xml")
    
    # Initiailize an empty list
    myList = []

    # Position of job in table
    pos = 1

    # Loop for looking through all responses
    for entry in parserResponse.entries[:10]:
        
        # Turn string enty["profile"] into a list, store in responseList
        responseList = list(entry["profile"])

        # Loop for iterating over every letter in responseList
        for letter in range(len(responseList)):
            
            # If the letter is an ampersand, change it into "%26", otherwise profiles
            # containing an ampersand will not load the google map embed due to GET method in URL
            if responseList[letter] == "&":
                responseList[letter]= "%26"
        
        # Change responseList back into a string, store in newResponse
        newResponse = ''.join(responseList)

        # Append myList with the position, title, country, and profile
        myList.append({"number" : pos, "title" : entry["title"], "country" : entry["country"], "profile" : newResponse})
        
        # Increment position by 1
        pos = pos + 1

    # Render html template 
    return render_template("index.html", myList = myList)