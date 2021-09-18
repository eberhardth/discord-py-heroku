import os
from datetime import datetime



token = os.getenv("BOT_TOKEN")
owner_id = os.getenv("OWNER_ID")



from discord.ext import commands


def get_prefix(client, message):

    prefixes = ['!', '!!']    # sets the prefixes, u can keep it as an array of only 1 item if you need only one prefix

    if not message.guild:
        prefixes = ['!!']   # Only allow '==' as a prefix when in DMs, this is optional

    # Allow users to @mention the bot instead of using a prefix when using a command. Also optional
    # Do `return prefixes` if u don't want to allow mentions instead of prefix.
    return commands.when_mentioned_or(*prefixes)(client, message)


bot = commands.Bot(                         # Create a new bot
    command_prefix=get_prefix,              # Set the prefix
    description='musikbot',  # Set a description for the bot
    owner_id=owner_id,            # Your unique User ID
    case_insensitive=True                   # Make the commands case insensitive
)

# case_insensitive=True is used as the commands are case sensitive by default

cogs = ['cogs.basic','cogs.musik',]

@bot.event
async def on_ready():                                       # Do this when the bot is logged in
    print(f'Logged in as {bot.user.name} - {bot.user.id}')  # Print the name and ID of the bot logged in.
    for cog in cogs:
      bot.load_extension(cog)
    return

# Finally, login the bot
bot.run(token, bot=True, reconnect=True)
