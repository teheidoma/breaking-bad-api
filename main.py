import json
import discord
import random as r
from html2image import Html2Image
from easygoogletranslate import EasyGoogleTranslate

translator = EasyGoogleTranslate(
    source_language='en',
    target_language='uk',
    timeout=10
)
client = discord.Client(intents=discord.Intents.all())
tree = discord.app_commands.CommandTree(client)


@tree.command(name='random', description='qwe', guild=discord.Object(id=699197199883698198))
async def random(int: discord.Interaction):
    get_image()
    await int.response.send_message(file=discord.File('a.png'))


@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=699197199883698198))

    print(f'{client.user} has connected to Discord!')


def read_from_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


def get_image():
    quotes = read_from_json('data/quotes.json')
    names = read_from_json('data/names.json')

    with open('quote.html', 'r') as file:
        elem = r.choice(quotes)
        name = next(filter(lambda x: x['name'] == elem['author'], names))
        template = file.read().replace('%quote%', translator.translate(elem['quote'])) \
            .replace('%author%', translator.translate(name['name_ua'])) \
            .replace('%img%', name['img'])
        print(elem)
        hti = Html2Image()
        hti.load_file('img/mike.png')
        hti.load_file('img/saul.png')
        hti.load_file('img/skylar.png')
        hti.load_file('img/hank.png')
        hti.load_file('img/walter.png')
        hti.load_file('img/jesse.png')
        hti.load_file('img/gus.png')
        hti.load_file('img/fly.png')
        hti.load_file('img/wwj.png')
        hti.load_file('img/badger.png')
        hti.screenshot(html_str=template, save_as='a.png', size=(800, 400))


client.run('NDk0ODg3MzA4ODkwNDcyNDU4.GZe7dl.nYl3e3omXHT6ZzzAwyAmf8WaXGb32ONYrxf17Q')
