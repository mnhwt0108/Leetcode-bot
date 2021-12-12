import discord
import os
import collect_data
from discord.ext import commands
from keep_alive import keep_alive


prefix = '!'
client = discord.Client()
bot = commands.Bot(command_prefix=prefix)
data = collect_data.get_data()

client = discord.Client()
my_secret = os.environ['TOKEN']


@client.event
async def on_ready(): 
  print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith(prefix + "help"):
    await message.channel.send('How to use Grind Bot: \n❓    !help : all commands \n💡    !total : total leetcode questions \n💻    !grind : random questions \n📊    !grind easy/medium/hard : random easy/medium/hard questions \n📈    !grind popular easy/medium/hard: random popular easy/medium/hard questions \n')
  
  if message.content.startswith(prefix + "grind"):
    # cmd, num, topic = message.content.split()
    temp = message.content.split()
    num = temp[1]
    
    cur_problem = data[int(num)]
    link = cur_problem["url"]
    difficulty = cur_problem["difficulty"]
    title = cur_problem["question_title"]
    description = cur_problem["description"]
    
    embed = discord.Embed(title=f"Leet code question:", url=link, color=0xFFA500)
    embed.set_thumbnail(url=
    "https://upload.wikimedia.org/wikipedia/commons/1/19/LeetCode_logo_black.png")
    embed.add_field(name="Title", value=f"{num}. {title}", inline=False)
    embed.add_field(name="Difficulty", value=difficulty, inline=True)
    embed.add_field(name="Total submission", value=description, inline=True)

    await message.delete()
    await message.channel.send(embed=embed)

keep_alive()
client.run(os.getenv('TOKEN'))