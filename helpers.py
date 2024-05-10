import json
from datetime import datetime

def open_wallet():
    """
    
    Open wallet JSON-file, throw exception if failed
    
    return -> list

    """
    try:
        with open('wallet.json', 'r', encoding='ascii') as f:
            f = json.load(f)
            return f
    except FileNotFoundError:
        print('No wallet JSON file found, create one with create-wallet option')
        return 0

def validate_amount(amount):
    """
    
    Validate sum of money, convert to float, throw exception if not numeric value
    input -> int/float
    return -> float

    """
    try:
        amount = float(amount)
        return amount
    except ValueError:
        print('Input valid numeric amount (e.g. 30000)')
        return 0
    

def validate_date(date):
    """
    
    Validate date, throw exception if wrong date format is provided

    input -> str
    return -> str
    
    """
    try:
        date = datetime.strptime(date, '%Y-%m-%d').date().isoformat()
        return date
    except ValueError:
        print('Input date in valid format (YYYY-MM-DD)')
        return 0

