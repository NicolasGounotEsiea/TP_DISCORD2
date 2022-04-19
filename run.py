
import json
from lib2to3.pgen2 import token
from pickle import NONE
from sys import prefix

from bot import BBot

import discord
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv(dotenv_path="config")
import os
from help import MyHelp
import logging
from datetime import datetime
from argparse import ArgumentParser, Namespace







    
    
def parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument(
        "-c", "--config", help="Config file", required=True, dest="config"
    )
    return parser.parse_args()

def get_config(config_file: str)-> dict:

    with open(config_file, "r") as f:

        config = json.load(f)

    return config



def main(config : dict) -> bool:

    TOKEN = config["TOKEN"]
    PREFIX = config["prefix"]

    logging.basicConfig(filename='logs.log', filemode='w', encoding='utf-8', format='%(levelname)s: %(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
    logging.info('Started')
    
    logging.info('Finished')
    intents = discord.Intents.default()
    intents.presences = True
    intents.members = True
    bbot = BBot(command_prefix=PREFIX, intents=intents)



    bbot.add_cog(MyHelp(bbot))
  

    bbot.run(TOKEN)


   

    pass



if __name__ == "__main__":

    args = parse_args()

    #print(args.config)

    #print(os.path.isfile(args.config))

    #assert os.path.isfile(args.config), "Config file not found"

    config = get_config(args.config)

    main(config)

    pass



