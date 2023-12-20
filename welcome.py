import discord
from discord import File
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='>', case_insensitive = True, intents=intents)

@client.event
async def on_ready():
    print('Bot esta ON')

@client.event
async def on_member_join(member):
    boasvindas = client.get_channel(1187005919272382554)
    regras = client.get_channel(1107384844821995531)
    chat = client.get_channel(1107384569478516738)
    aovivoemlive = client.get_channel(1146640261238243419)
    mensagem = await boasvindas.send(f'Seja bem vindo(a) {member.mention} ao servidor! \nDê uma olhada nas regras em {regras.mention} \nFique a vontade pra conversar no canal de chat {chat.mention} \nAlertas de quando o canal estiver AO VIVO serão notificados em {aovivoemlive.mention} ')

client.run('MTE4NjY3NjQ2NjIwNTg1NTc1NQ.G3ZGkq.-JVDDEuKoq_ngdZq3_Zp_nI1sejsgi5QW8IAtY')
