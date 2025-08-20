import os
import asyncio
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID", "0"))

async def main():
    if not TOKEN or not GUILD_ID:
        raise SystemExit("Set DISCORD_BOT_TOKEN and GUILD_ID in your .env")
    intents = discord.Intents.none()
    client = discord.Client(intents=intents)
    tree = discord.app_commands.CommandTree(client)

    @client.event
    async def on_ready():
        guild = discord.Object(id=GUILD_ID)
        await tree.sync(guild=guild)
        print(f"Synced commands to guild {GUILD_ID}")
        await client.close()

    await client.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
