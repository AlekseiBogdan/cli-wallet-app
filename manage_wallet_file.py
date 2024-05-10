import json
import os

import click


@click.command(help='Create your wallet')
def create_wallet():
    """
    
    Creation of the wallet JSON-file
    
    """
    if not os.path.exists('wallet.json'):
        with open('wallet.json', 'w') as f:
            json.dump([], f)
    else:
        try:
            with open('wallet.json', 'r') as f:
                f = json.load(f)
        except ValueError:
            with open('wallet.json', 'w') as f:
                json.dump([], f)
        print('Wallet already exists!')

@click.command(help='Delete your wallet')
@click.confirmation_option(prompt='Do you want to remove your wallet?')
def delete_wallet():
    """
    
    Delete wallet JSON-file if confirmation is provided

    """
    os.remove('wallet.json')
    print('Your wallet has been deleted')
    print('You may create new one with create-wallet command')




