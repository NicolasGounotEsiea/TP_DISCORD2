from pickle import NONE
from bot import BBot

import discord
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv(dotenv_path="config")
import os
from help import MyHelp
import logging
from datetime import datetime






def main():
    
    logging.basicConfig(filename='logs.log', filemode='w', encoding='utf-8', format='%(levelname)s: %(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
    logging.info('Started')
 
    logging.info('Finished')
    intents = discord.Intents.default()
    intents.presences = True
    intents.members = True
    bbot = BBot(command_prefix=os.getenv("prefix"), intents=intents)



    bbot.add_cog(MyHelp(bbot))
  

    bbot.run(os.getenv("TOKEN"))


if __name__ == '__main__':
    main()