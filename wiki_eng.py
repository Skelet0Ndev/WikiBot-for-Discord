import discord
from discord import utils
import wikipedia

client = discord.Client()

@client.event         
async def on_ready():       
    print('Wikipedia referencing engaged for {}'.format(client.user))
    wikipedia.set_lang("en")    #default
    x = int(0)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!whelp') or message.content.startswith('!welp') or message.content.startswith('!help'):      #help
        await message.channel.send('''`Quickstart with Wiki-bot (please state the parameters or requests after the command divided by a single space):`
    "!wb"(Wiki Brief) - Briefly about somewhat. 
    "!ws"(Wiki Summary) - Summary of an article.
    "!wm"(Wiki Multiply) - Used for addressing disambiguation issues. Returns a table of different meanings of your request. 
    "!wp"(Wiki Page) - Returns the URL of the requested page.
    "!wl"(Wiki Language) - Adjusts the Wikipedia language. Default: English. **Language short names only. Example: "!wl en", "!wl fr", "!wl de", "!wl ru"**
            *Note: Request may refer to more than one page. For more certainty, state the subject of the request.
        ''')
                                   
    if message.content.startswith('!wl'):       #wikipedia laguage
        try:
            s = message.content
            wikipedia.set_lang(s[4:6])
            await message.channel.send('Language set: `' + s[4:6] + '`. \n**Please, type your search requests in this language only!**')
        except WikipediaException as e:
            erpl = '`Invalid language option`'
            await message.channel.send(erpl)
            print('[ERROR] Invalid language option')
        except WikipediaException as e:
            print(repr(e))

    if message.content.startswith('!wm'):       #wikipedia brief
        try:
            s = message.content
            op = wikipedia.search(s[4:100], results=10)
            x = int(0)
            repl = ''
            for x in range (len(op)):
                repl = repl + op[x] + '\n '
            await message.channel.send('`"' + s[4:100] + '"` may refer to: \n' + repl)
        except WikipediaException as e:
            print(repr(e))

    if message.content.startswith('!wb'):       #wikipedia brief
        try:
            s = message.content
            full = wikipedia.page(s[4:100])
            t = full.title
            repl = wikipedia.summary(s[4:100], sentences=4)
            await message.channel.send('Briefly about `"' + t + '"`: \n' + repl)
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
            erpl = '**Disambiguation error!** `' + s[4:100] + '` may refer to these pages. Please, select one of the options. Don\'t forget about the command!\n'
            op = wikipedia.search(s[4:100], results=10)
            x = int(0)
            for x in len(op):
                erpl = erpl + op[x] + '\n '
            await message.channel.send(erpl)
        except WikipediaException as e:
            print(repr(e))
    
    if message.content.startswith('!ws'):       #wikipedia summary
        try:
            s = message.content
            full = wikipedia.page(s[4:100])
            t = full.title
            repl = wikipedia.summary(s[4:100])
            await message.channel.send('Summary about `"' + t + '"`: \n' + repl)
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
            erpl = '**Disambiguation error!** `' + s[4:100] + '` may refer to these pages. Please, select one of the options. Don\'t forget about the command!\n'
            op = wikipedia.search(s[4:100], results=10)
            x = int(0)
            for x in len(op):
                erpl = erpl + op[x] + '\n '
            await message.channel.send(erpl)
        except WikipediaException as e:
            print(repr(e))

    if message.content.startswith('!wp'):       #wikipedia page
        try:
            s = message.content
            repl = wikipedia.page(s[4:100])
            await message.channel.send('For more information about `"' + repl.title + '"`: \n' + repl.url)
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
            erpl = '**Disambiguation error!** `' + s[4:100] + '` may refer to these pages. Please, select one of the options. Don\'t forget about the command!\n'
            op = wikipedia.search(s[4:100], results=10)
            x = int(0)
            for x in len(op):
                erpl = erpl + op[x] + '\n '
            await message.channel.send(erpl)
        except WikipediaException as e:
            print(repr(e))

client.run('Your Token Here')
