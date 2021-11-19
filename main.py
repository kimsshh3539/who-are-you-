import discord
import requests
from bs4 import BeautifulSoup
import os

client = discord.Client()
    

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='명령어는 !전적 플레이어 이름'))
    print('로그인되었습니다!')
    print(client.user.name)
    print(client.user.id)
    print('====================================')

@client.event
async def on_message(message):
    if message.author.bot:
        return None
    else:
        if message.content.startswith('!전적'):
            Name = message.content.split(" ")
            space = Name[1]
            url = 'https://www.op.gg/summoner/userName=' + space
            SummonerName = ''
            Tier = []
            TierUnranked = 'false'
            LP = []
            Winsp = []
            hdr = {'Accept-Language': 'ko_KR,en;q=0.8', 'User-Agent': ('Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Mobile Safari/537.36')}
            req = requests.get(url, headers=hdr)
            html = req.text 
            soup = BeautifulSoup(html, 'html.parser')
            for i in soup.select('div[class=SummonerName]'): 
                SummonerName = i.text
            for i in soup.select('div[class=Tier]'): 
                Tier = i.text
            for i in soup.select('div[class=LP]'): 
                LP = i.text
            for i in soup.select('span[class=Ratio]'): 
                Winsp = i.text


        embed=discord.Embed(color=0xff00, title=SummonerName + '님의 전적입니다.', description='티어' + Tier + '' + '\nLP\n' + LP + '\n\n승률\n' + Winsp, timestamp=message.created_at)
        embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

@client.event
async def on_message(message):
    if message.author.bot:
        return None
    else:
        if message.content.startswith('!개발자'):
            await message.channel.send('개발자 디스코드 : 정신분열자#1473')

        
        
access_token = os.environ["BOT_TOKEN"] 
client.run(access_token)
