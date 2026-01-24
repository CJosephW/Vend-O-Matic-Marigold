# Vend-O-Matic
### A beverage vending machine service using Python

[Setup](#setup)

[Testing](#testing)

[Project Requirements](#project-requirements)

## Setup
Firstly setup your python virtual enviornment inside the repo

### OSX/Linux 
``` python3 -m venv myenv ```

```source myenv/bin/activate```

### Windows
``` python3 -m venv myenv ```

```.\myenv\Scripts\activate.bat  (or .ps1 if using powershell)```

Then install the required packages using pip

``` pip install -r requirements.txt```

## Testing
For testing I set up sonme simple unit tests using the built in unittests library these can be ran using

``` python -m unittest discover -s tests ```

For a 'integration' type test I just made a simple pythong script to ensure the specification requests are returning the correct responses 

## Project Requirements
1. The machine only accepts US quarters - you physically cannot put anything else in, and
you can only put one coin in at a time.
2. Purchase price of an item is two US quarters.
3. Machine only holds five of each of the three beverages available to purchase in its
inventory.
4. Machine will accept more than the purchase price of coins, but will only dispense a single
beverage per transaction.
5. Upon transaction completion, any unused quarters must be dispensed back to the
customer.
6. All test interactions will be performed with a single content type of “application/json”.
![route specs](./img/route_specifications.png)

## Design/Technical Decisions
For this project I followed test driven development for this project, so first building out the test cases and then continuing to the REST route functionalty from that point onwards.

For the database I elected to use a in memory json file 
