from discord.ext import commands
from datetime import datetime

class BBot(commands.Bot):

    async def on_ready(self):
        print(f'{self.user.name} has connected to Discord!')
        time = str(datetime.now())
        f = open("example.log", "a")
        f.write(time + " The bot " + self.user.name + " is logged to the server !\n")
        f.close()

    

    

   













