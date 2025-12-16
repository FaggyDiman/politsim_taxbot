# Politsim Taxbot
This workflow automatically posts tax returns from Xenforo-based forums using DBTech Shop and DBTech Credits, with **politsim.ru** as the main working platform

## Contacts
**Discord**: karakalkas

## Algorithm
- Fetches user inventory data from the Xenforo SQL database and wallet data from a dedicated service page.  
- Calculates the value of the inventory using `items.json` (currently updated manually).  
- Compiles the total value of the user's property: wallet plus inventory value.  
- Creates a log file in the `YYYY-MM-DD` format.  
- Searches for the previous log file, if available.  
- Calculates tax based on `TAX_RATE` and `THRESHOLD`.  
- Inserts the calculated values into a BB-code table.
- Makes API call to post the table in a thread.

## Usage
The entry point is `main.py`. Constants in the file represent the credentials needed to connect to the database and post to the forum. Repo uses Github Actions workflow to execute automatically.

### Politsim users
*Instructions coming soon*  

### Other users
*Instructions coming soon*  

## Branches
- **main** — template branch  
- **working** — currently used for virtual Germany  
