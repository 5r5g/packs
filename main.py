import discord
from discord.ext import commands
import config
from tournament_manager import TournamentManager

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.reactions = True

bot = commands.Bot(command_prefix=config.PREFIX, intents=intents)

# Initialize tournament manager
tournament_manager = TournamentManager(bot)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print(f'Bot is in {len(bot.guilds)} guilds')
    await bot.change_presence(activity=discord.Game(name=f"{config.PREFIX}help | Tournament Mode"))

# Load cogs
async def load_cogs():
    await bot.load_extension('cogs.tournament_commands')
    await bot.load_extension('cogs.admin_commands')
    await bot.load_extension('cogs.help_command')

async def main():
    async with bot:
        await load_cogs()
        await bot.start(config.TOKEN)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
