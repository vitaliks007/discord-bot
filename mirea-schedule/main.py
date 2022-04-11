import hikari

from configparser import ConfigParser
from os import path

conf = ConfigParser()
conf.read(path.dirname(__file__) + '/config.ini')
token = conf['auth']['token']
bot = hikari.GatewayBot(token)

@bot.listen()
async def test(event: hikari.MessageCreateEvent):
    if event.is_bot or not event.content:
        return

    if event.content.startswith('м!привет'):
        await event.message.respond('Привет!')


bot.run()