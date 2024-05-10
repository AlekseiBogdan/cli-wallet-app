import click

from manage_wallet_entries import add_entry, delete_entry, edit_entry, \
    show_bal
from manage_wallet_file import create_wallet, delete_wallet
from search_entries import search_for_entry

@click.group()
def app():
    """

    main app instance
    all app functionality is added via add_command() from Click package
    
    """
    pass

app.add_command(create_wallet)
app.add_command(delete_wallet)
app.add_command(show_bal)
app.add_command(add_entry)
app.add_command(search_for_entry)
app.add_command(edit_entry)
app.add_command(delete_entry)


if __name__ == '__main__':
    app()