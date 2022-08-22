from os import system
from imp import reload
system('cls')
import discord, asyncio
from function import add_message
from discord_components import DiscordComponents, Button, ButtonStyle
import os

intents = discord.Intents.all()
client = discord.Client(intents=intents)

url = "https://cdn.discordapp.com/attachments/728177794265120852/1011223673547534346/download.png" # 서버 로고 URL을 적어주세요 ex) https://..

@client.event
async def on_ready():
    DiscordComponents(client)
    print("유저 관리봇이 시작되었어요!")


@client.event
async def on_message(message):
    if message.author.bot: return None
    if message.content.startswith("##리로드"):
        if message.author.id == 727063255423516692 or message.author.id == 886170769472782337:
            reload(add_message)
            await message.reply(embed=discord.Embed(title="Module Reload", description="✅ 모든 모듈을 모두 다시 시작했습니다"))
    elif message.content.startswith("#정리"):
        system('cls')
    else:
        await add_message.message(client, message, url)

@client.event
async def on_member_join(member):
    embed=discord.Embed(title=f"**감자 Bot**에 오신것을 환영합니다!", description=f"저희서버에서 즐겁고 행복한시간 보내봅시당~", color=0x00ff56) #수정이 필요합니다 '서버' 텍스트를 변경해주세요
    embed.set_thumbnail(url=url)
    embed.set_footer(text=f"감자 Bot", icon_url=member.avatar_url) #수정이 필요합니다 '서버' 텍스트를 변경해주세요
    await client.get_channel(1011221300171255909).send(content=member.mention, embed=embed) #수정이 필요합니다 get_channel() 괄호안에 채널 아이디를 적어주세요! 수정하셨다면 맨 앞에 '#'만 지워주세요!
    
@client.event
async def on_member_remove(member):
    embed=discord.Embed(title=f"다음에 또 뵈요ㅠㅠ", description=f"다음에또 저희 **감자 Bot**를 찾아주세요!", color=0xff0000) #수정이 필요합니다 '서버' 텍스트를 변경해주세요
    embed.set_thumbnail(url=url)
    embed.set_footer(text=f"감자 Bot", icon_url=member.avatar_url) #수정이 필요합니다 '서버' 텍스트를 변경해주세요
    await client.get_channel(1011221300171255909).send(content=member.mention, embed=embed) #수정이 필요합니다 get_channel() 괄호안에 채널 아이디를 적어주세요! 수정하셨다면 맨 앞에 '#'만 지워주세요!
    
access_token = os.environ["BOT_TOKEN"
client.run(access_token)
