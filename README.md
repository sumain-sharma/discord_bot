# discord_bot

A discord bot having following functionalities:
- Reply 'hey' to 'hi.
- Search top 5 links from google for the given keyword.
- Display matching search history of the user for the given keyword.

# Requirements:
## software and package
- Python - 3.7.6

# Installation:
1. Clone the repo.
2. Open terminal inside "discord_bot" dir.
3. Install virtualenv package:&nbsp;&nbsp;<code> pip3 install virtualenv </code>
4. Create a virtualenv: &nbsp;&nbsp;<code> python3 -m virtualenv venv </code>
5. Activate virtualenv: &nbsp;&nbsp;<code> source venv/bin/activate </code>
6. Install python packages: &nbsp;&nbsp;<code> pip install -r requirements.txt </code>
7. Setup discord bot, get access token and put it in .env file.

# Commands
- To search a keyword and display top 5 links:
    ### !google \<keyword>

    e.g: !google python

- To search matching data from the search history of the user:
    ### !recent \<keyword>

    e.g: !google python
