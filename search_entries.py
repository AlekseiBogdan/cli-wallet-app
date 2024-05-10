import click

from helpers import open_wallet, validate_amount, validate_date

SEARCH_GROUP = {
    'id': 'id',
    'd': 'Date',
    'c': 'Category',
    'a': 'Amount',
    'desc': 'Description',
    'all': 'all'
}

@click.command(help='Search for entry')
@click.argument('search_group', type=click.Choice(SEARCH_GROUP.keys()), default='all')
def search_for_entry(search_group):
    """
    
    App's search engine :)
    Search for entries in wallet by provided parameters
    Input -> str
    Print -> dict[str: any]

    """
    file = open_wallet()
    match search_group:
        case 'id':
            search_value = click.prompt('Input entry ID', type=int)
            try:
                click.echo(file[search_value])
            except IndexError:
                click.echo('No entry with such id')
        case 'd':
            search_value = click.prompt('Input date in valid format (YYYY-MM-DD)')

            search_value = validate_date(search_value)

            if not search_value:
                return 0
            
            search_result = [entry for entry in file if entry[SEARCH_GROUP[search_group]] == search_value]

            if not search_result:
                click.echo('No entries found')
                return 0
            else:
                for entry in search_result:
                    print(entry)
        case 'c':
            search_value = click.prompt('Input category (income or expense)')

            search_result = [entry for entry in file if entry[SEARCH_GROUP[search_group]] == search_value]

            if not search_result:
                click.echo('No entries found')
                return 0
            else:
                for entry in search_result:
                    print(entry)
        case 'a':
            search_value = click.prompt('Input numeric amount', type=int)

            search_value = validate_amount(search_value)

            if not search_value:
                return 0
            
            search_result = [entry for entry in file if entry[SEARCH_GROUP[search_group]] == search_value]

            if not search_result:
                click.echo('No entries found')
                return 0
            else:
                for entry in search_result:
                    print(entry)
        case 'desc':
            search_value = click.prompt('Input description')

            search_result = [entry for entry in file if entry[SEARCH_GROUP[search_group]] == search_value]

            if not search_result:
                click.echo('No entries found')
                return 0
            else:
                for entry in search_result:
                    print(entry)
        case _:
            for entry in file:
                print(entry)

    


