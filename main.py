"""the main"""
import sys
import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
	if message.content.startswith("+ping"):
		await client.send_message(message.channel, "Pong!")
	elif message.content.startswith("+g"):
		msg = "https://www.google.com/search?q=" + message.content[3:].replace(' ', "\%20")
		await client.send_message(message.channel, msg)
	elif message.content.startswith("+big"):
		msg = " ".join(message.content[5:])
		await client.send_message(message.channel, msg)
	

def main():
	"""Main entry point for the script."""
	env = open(".env")
	token = env.readline()
	env.close()
	
	client.run(token)

if __name__ == '__main__':
	sys.exit(main())
