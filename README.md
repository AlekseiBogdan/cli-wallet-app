
# Wallet CLI Python app

## Installation

Prerequisities:
- Python 3.11

To use the app:
- Clone git-repository
- run ```pip install -r requirements.txt``` command (to install correct version of ```Click``` package)
- You're done!

## Basic Usage

To see all the possible commands run ```app.py --help``` command. Also you can run ```--help``` flag with each command to see possible arguments and options.

First of all, create your wallet JSON-file with ```app.py create-wallet``` command. 

After that you can add entries to your wallet with ```app.py add-entry [[i|e]]``` command, specify date, sum of money, write description to your entry.

Now, you can edit/delete existing entries or add new ones. See **List of commands** for further info.

# List of commands

| Command | Description |
| ---|---|
| ```create-wallet``` | Create your wallet |
| ```delete-wallet``` | Delete your wallet |
| ```add-entry```| Add entry to your wallet|
|```edit-entry```| Edit wallet entry by id|
|```delete-entry```|Delete entry from wallet by id|
|```show-bal```|Show your current balance|
| ```search-for-entry``` | Search for particular entry in your wallet or see all entries (if no other argument is provided)|