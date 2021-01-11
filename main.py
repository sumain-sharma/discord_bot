'''
    Python module work as entrypoint for the project
'''
import os

from src.bot import run_bot
from src.data_storage import DataStorage

if __name__ == "__main__":

    # initializing DB
    with DataStorage() as data_storage_obj:
        data_storage_obj.initializing_schema()

    # start discord bot
    run_bot(os.getenv("DISCORD_TOKEN"))
