import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

intents = discord.Intents.default()
intents.reactions = True  # Enable reaction events
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

@bot.event
async def on_reaction_add(reaction, user):
    print(f"{user} reacted with {reaction.emoji} to message '{str(reaction.message.content)}'")
    if reaction.emoji == "👎" and reaction.count >= 1:  # change the 1 to the minimum amount of reactions required
        message = reaction.message
        if message.channel.id == 927372332341817436: # channel id of the channel you want to check from
            destination_channel = bot.get_channel(1153189714153713674) # change the id to the channel you want as the "shameboard" channel
            if destination_channel:
                # Create an embed
                embed = discord.Embed(
                    title=f"Reposted from {message.author}",
                    description=message.content,
                    color=0x00ff00  # embed color ))
                )
                if message.attachments:
                    for attachment in message.attachments:
                        if attachment.url.endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp', 'mp4', 'mov', 'avi', 'webm')):
                            if attachment.url.endswith(('png', 'jpg', 'jpeg', 'gif')):
                                embed.set_image(url=attachment.url)
                            elif attachment.url.endswith(('mp4', 'mov', 'avi')):
                                embed.add_field(name="Video Attachment", value=f"[Watch Here]({attachment.url})")
                
                await destination_channel.send(embed=embed)

# Run the bot using the token
bot.run(os.environ["DISCORD_BOT_TOKEN"])