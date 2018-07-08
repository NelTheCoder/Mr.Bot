import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.voice_client import VoiceClient
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix="@")
client.remove_command('help')
chat_filter = []
vote_to_jail = {}
jailset = 7
voted = []
@client.event
async def on_ready():
  print("Mr. Bot is wondering how to help you...")

@client.event
async def on_message(message,amount = 100):
  contents = message.content.split(" ")
  userID = message.author.id
  for word in contents:
    if word.lower() in chat_filter:
      if not "403718470182633483" in [role.id for role in message.author.roles]:
        try:
          await client.delete_message(message)
          await client.send_message(message.channel, "Mr. Bot did not like what you just said, <@%s>. He is considering washing out your mouth with soap..." % (userID))
        except discord.errors.NotFound:
          return
  if "458331153200578659" in [role.id for role in message.author.roles]:
    await client.delete_message(message)
    await client.send_message(message.channel, "Mr. Bot checks the prison, and sees that you are jailed, <@%s>. He tells you to wait till you are unjailed to speak in any for of chat" % (userID))
  if "461993974568058892" in [role.id for role in message.author.roles]:
    await client.delete_message(message)
    await client.send_message(message.channel, "Mr. Bot checks the prison, and sees that you are jailed, <@%s>. He tells you to wait till you are unjailed to speak in any for of chat" % (userID))
  if message.content.lower().startswith('@ping'):
    await client.send_message(message.channel, "Mr. Bot wonders how he can help you, <@%s>?" % (userID))
  if message.content.lower().startswith('@say'):
    words = message.content.split(" ")
    await client.send_message(message.channel, "Mr. Bot says, %s" % (" ".join(words[1:])))
  if message.content.lower().startswith('@speak'):
    words = message.content.split(" ")
    await client.send_message(message.channel, "%s" % (" ".join(words[1:])), tts = True)
  if message.content.lower().startswith('@human'):
    if "403727313495261186" not in [role.id for role in message.author.roles]:
      await client.send_message(message.channel, 'Mr. Bot is pretty sure you are a human, <@%s>' % (userID))
    else:
      await client.send_message(message.channel, 'Mr. Bot believes you are not a human, <@%s>' % (userID))
  if message.content.lower().startswith('@help'):
    author = message.author
    embed = discord.Embed(
      colour = discord.Color.red()
    )
    embed.set_author(name="Help")
    embed.add_field(name = "Mr. Bot's guide to getting his help:", value = "@ping - Mr. Bot will ping you...\n\n@say - Mr. Bot will say what you wish for him to...\n\n@speak - Mr. Bot will say whatever you want him to out loud... \n\ns@human- Mr. Bot will deduce if you are human or not...\n\n@clear- Mr. Bot will clear up the chat for people who are very special...\n\n@add - Mr. Bot will add together any numbers you have, as long as they are seperated by spaces...\n\n@jail - Mr. Bot will take your help to jail people who affect the server.", inline = False)
    await client.send_message(message.channel, embed = embed)
  if message.content.lower().startswith('@add'):
    words = message.content.split("")
    total = 0
    if len(words) >= 3:
      for x in words[1:]:
        total += int(x)
      await client.send_message(message.channel, "Mr. Bot figured out how to add without using his fingers, and he has calculated that your total is %s" % (str(total)))
    else:
      await client.send_message(message.channel, "Mr. Bot is confused with the numbers you have given him. His calculator is confused as well, <@%s>" % (userID))
  if message.content.lower().startswith('@clear'):
    if "403718470182633483" in [role.id for role in message.author.roles]:
      channel = message.channel
      messages = message.content.split()
      if len(messages) == 2:
        amount = int(messages[1])+1
      async for message in client.logs_from(channel, limit = int(amount)):
          await client.delete_message(message)
    elif "461032588123832330" in [role.id for role in message.author.roles]:
      channel = message.channel
      messages = message.content.split()
      if len(messages) == 2:
        amount = int(messages[1])+1
      async for message in client.logs_from(channel, limit = int(amount)):
          await client.delete_message(message)
    else:
      await client.send_message(message.channel, "Mr. Bot is sad that you cannot use one of his commands, <@%s>..." % (userID))
  if message.content.lower().startswith("@kick"):
    if "403718470182633483" in [role.id for role in message.author.roles]:
       await client.kick(message.mentions[0])
  if message.content.lower().startswith("@jail"):
    jailed = message.mentions[0]
    if "403718470182633483" in [role.id for role in message.author.roles]:
      role = discord.utils.get(jailed.server.roles, name="JAILED")
      await client.add_roles(jailed, role)
    elif "461032588123832330" in [role.id for role in message.author.roles]:
      role = discord.utils.get(jailed.server.roles, name="JAILED")
      await client.add_roles(jailed, role)
    else:
      if userID in voted:
        await client.send_message(message.channel, "Mr. Bot looks at something and tells you that you have already voted for someone to be jailed, <@%s>" % (userID))
      else:
        vote_to_jail[jailed] += 1
        if vote_to_jail[jailed] == jailset:
          await client.send_message(message.channel, "Mr. Bot decides that justice has been served! He informs everyone that <@%s> is now going to jail" % (jailed.id))
          vote_to_jail[jailed] = 0
          voted = []
        else:
          await client.send_message(message.channel, "Mr. Bot adds your vote to the number of people that want <@%s> jailed, <@%s>" % (jailed.id, userID))
          voted.append(userID)
  if message.content.lower().startswith("@unjail"):
    jailed = message.mentions[0]
    if "403718470182633483" in [role.id for role in message.author.roles]:
      role = discord.utils.get(jailed.server.roles, name="JAILED")
      if role in jailed.roles:
        await client.remove_roles(jailed, role)
        await client.send_message(message.channel, "Mr. Bot informs everyone that <@%s> has been released from jail..." % (jailed.id))
    elif "461032588123832330" in [role.id for role in message.author.roles]:
      role = discord.utils.get(jailed.server.roles, name="JAILED")
      if role in jailed.roles:
        await client.remove_roles(jailed, role)
        await client.send_message(message.channel, "Mr. Bot informs everyone that <@%s> has been released from jail..." % (jailed.id))
async def on_reaction_add(reaction, user):
  channel = reaction.message.channel
  await client.send_message(channel, "Mr. Bot noticed that <@%s> reacted to <@%s>, who said '%s', with a %s..." % (user.id, reaction.message.author.id,reaction.message.content,reaction.emoji))
async def on_reaction_remove(reaction, user):
  channel = reaction.message.channel
  await client.send_message(channel, "Mr. Bot noticed that <@%s> removed the %s reaction they had on <@%s>'s message, which was '%s'..." % (user.id, reaction.emoji,reaction.message.author.id,reaction.message.content)) 

client.run(os.getenv('TOKEN'))
