import asyncio
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import platform
import discord
from discord.ext import commands
from discord.ext.commands import Bot

TOKEN = ''
client = Bot(description="FieryText bot", command_prefix='ff', pm_help = False)
driver = webdriver.Firefox()

@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
    print('--------')
    print('Use this link to invite {}:'.format(client.user.name))
    print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
    print('--------')
    print('You are running FieryText')
    print('Created by /u/Lemminsky')
    return await client.change_presence(game=discord.Game(name='type "fff" to ignite'))

@client.command()
async def f(*args):
    sentence = ''
    for word in args:
        sentence = sentence + word + ' '
    text = str.upper(sentence)
    text = text[:-1]
    text = text.replace(' ', '+')
    if 0 < len(text) < 20:
        print(text)
        address = str('http://www5.flamingtext.com/net-fu/dynamic.cgi?script=flaming-logo&text=' + text + '&fontsize=70&fontname=SF+Gushing+Meadow&textColor=%23000&transparent=on#customize')
        print(address)
        driver.get(address)
        driver.find_element_by_id('wizard-done-btn').click()
        elements = driver.find_elements_by_class_name('ft-result-logo-image-wrapper')
        for i in elements:
            image = i.find_element_by_tag_name('img')
            img_src = image.get_attribute('src')
            print(img_src)
            await client.say(img_src)

    else:
        await client.say('ur message gotta be between 1 and 20 char long')

client.run(TOKEN)
