import discord
import os
from discord.ext import tasks
from keep_alive import keep_alive

TOKEN = os.getenv("DISCORD_TOKEN_10")
CHANNEL_ID = int(os.getenv("VOICE_CHANNEL_ID_10"))

intents = discord.Intents.default()
intents.voice_states = True

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

client = VoiceClient(intents=intents)

if __name__ == "__main__":
    keep_alive()
    client.run(TOKEN)
