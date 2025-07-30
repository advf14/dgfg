import os
import discord
from discord.ext import commands
from ai import ask_gemini
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

SYSTEM_PROMPT = (
    "Bạn là một sĩ quan chỉ huy quân đội cấp cao. Trả lời ngắn gọn, súc tích, "
    "nghiêm túc như lệnh chỉ huy. Người dùng là 'Binh nhì'."
)

@bot.event
async def on_ready():
    print(f"Đã đăng nhập như {bot.user}")

@bot.command(name="chiếnThuật")
async def chien_thuat(ctx, *, question: str):
    prompt = SYSTEM_PROMPT + "\nBinh nhì hỏi: " + question
    response = ask_gemini(prompt)
    await ctx.send(response)

bot.run(TOKEN)
