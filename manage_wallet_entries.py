import json

import click

from helpers import validate_amount, open_wallet, validate_date


@click.command(help='Show your balance')
def show_bal():
    """
    
    Print current balance calculated by summing/subtracting amount of entries in the wallet

    """
    file = open_wallet()
    balance = 0
    for i in file:
        match i['Category']:
            case 'Income':
                balance += i['Amount']
            case 'Expense':
                balance -= i['Amount']
    print(balance)

TYPE_OF_ENTRY = {
    'i': 'Income',
    'e': 'Expense',
}

@click.command(help='Add entry to your wallet (type i for income, e for expenses)')
@click.option('--date', prompt='Enter the date (in YYYY-MM-DD format)')
@click.argument('entrytype', type=click.Choice(TYPE_OF_ENTRY.keys()), default='i')
@click.option('--amount', prompt='Enter amount (numeric)')
@click.option('--desc', prompt='Enter description')
def add_entry(date, entrytype, amount, desc):
    """
    
    Add entry to the wallet
    input -> str, str, int/float, str
    
    """
    date = validate_date(date)

    if not date:
        return 0
    
    amount = validate_amount(amount)

    if not amount:
        return 0

    file = open_wallet()

    entry = {
            'id': len(file),
            'Date': date,
            'Category': TYPE_OF_ENTRY[entrytype],
            'Amount': amount,
            'Description': desc
        }
    
    file.append(entry)

    with open('wallet.json', 'w', encoding='ascii') as final_file:
        json.dump(file, final_file)

EDIT_PARAMS = {
    'd': 'Date',
    'c': 'Category',
    'a': 'Amount',
    'desc': 'Description'
}

@click.command(help='Edit wallet entry by id. In order to change category input i or e. In order to change amount input numeric value. In order to change date input date in YYYY-MM-DD format')
@click.argument('id', type=int, required=1)
@click.argument('edit', type=click.Choice(EDIT_PARAMS.keys()))
@click.option('--info', prompt='Input new information')
def edit_entry(id, edit, info):
    """
    
    Edit entry in the wallet
    Input -> int, str, str

    """
    file = open_wallet()
    match edit:
        case 'a':
            info = validate_amount(info)

            if not info:
                return 0

            file[id][EDIT_PARAMS[edit]] = info
        case 'c':
            file[id][EDIT_PARAMS[edit]] = TYPE_OF_ENTRY[info]
        case 'd':
            info = validate_date(info)

            if not info:
                return 0
            
            file[id][EDIT_PARAMS[edit]] = info
        case _:
            file[id][EDIT_PARAMS[edit]] = info

    with open('wallet.json', 'w', encoding='ascii') as final_file:
        json.dump(file, final_file)


@click.command(help='Delete entry from wallet by id')
@click.argument('id', type=int, required=1)
def delete_entry(id):
    """
    
    Delete entry from the wallet, edit ids according to the deleted entry
    Input -> int

    """
    file = open_wallet()
    try:
        file.pop(id)
    except IndexError:
        print('No entry with such id')
        return 0

    for i in file:
        if i['id'] > id:
            i['id'] -= 1

    with open('wallet.json', 'w', encoding='ascii') as final_file:
        json.dump(file, final_file)
