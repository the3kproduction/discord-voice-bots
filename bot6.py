import discord
import os
from discord.ext import tasks

TOKEN = os.getenv("DISCORD_TOKEN_6")
CHANNEL_ID = int(os.getenv("VOICE_CHANNEL_ID_6"))

# Set up the required intents
intents = discord.Intents.default()
intents.voice_states = True  # Enable voice state updates (required for joining channels)

class VoiceClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected')
        channel = self.get_channel(CHANNEL_ID)
        if channel:
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio("silent.mp3"), after=lambda e: print('done', e))
            loop.start(vc)
        else:
            print("Channel not found")

@tasks.loop(seconds=60)
async def loop(vc):
    if not vc.is_playing():
        vc.play(discord.FFmpegPCMAudio("silent.mp3"))

# Pass the intents when initializing the client
client = VoiceClient(intents=intents)
client.run(TOKEN)
