# web-scraping-challenge
This repo was created for the Bootcamp HW12 web-scraping-challenge

I created a folder called "Mission_to_Mars" which houses a mission_to_mars.ipynb jupiter notebook, an app.py file, a scrape_mars.py file.

There is also a templates folder that houses an index.html file and style.css file.


The mission_to_mars.ipynb jupiter notebook contains the code used to scrape websites in order to gather data on mars, and compile the results into a dictionary.

The code in this notebook was then exported to the scrape_mars.py file.

A few minor changes were made to the code in scrape_mars.py file to remove certain lines where I was testing the results of my code in the notebook.

I also put the code in the scrape_mars.py file into a function called scrape()

Next, I configured an app.py file to call a main route and a /scrape route which uses the scrape() funciton to scrape data from the websites given in the HW instructions

Finally, I created the index.html and style.css files to create a landing page to display the results of the scraping.