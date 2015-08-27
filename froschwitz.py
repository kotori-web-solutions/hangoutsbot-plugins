import random
import asyncio
from urllib.request import urlopen
import plugins
from random import randint

def _initialise(bot):
    plugins.register_user_command(["froschwitz"])


def froschwitz(bot, event, *args):
    """Ich kenne ein paar maximal unlustige Froschwitze."""
      
    randomjokenr = random.randint(0,7)
    jokes = [ ]
      
    jokes.append("Was bestellt ein Frosch im Restaurant? Quark.")
    jokes.append("Was ist grün und wird auf Knopfdruck rot? Ein Frosch im Mixer. Was ist grün und bleibt auf Knopfdruck grün? Ein Frosch, der um sein Leben rennt.")
    jokes.append("Der angetrunkene Jäger nimmt die Wildente auf dem Teich ins Visier, zielt aber daneben und trifft nur einen Frosch. Als er den leblosen Körper des Tieres hochhebt, murmelt er vor sich hin: 'Irre, sogar das Gefieder hab ich ihr weggeschossen!'")
    jokes.append("Zwei Frösche sitzen am Teich, als es plötzlich anfängt zu regnen. Da sagt der eine zum anderen: 'Komm, wir springen ins Wasser. Sonst werden wir noch nass!'")
    jokes.append("Kommt ein Mann mit einen Frosch auf dem Kopf zum Arzt. Fragt der Arzt: 'Was ist denn mit Ihnen passiert?' 'Ach', sagt der Frosch, 'ich weiß auch nicht, wo ich mir den eingetreten habe.'")
    jokes.append("'Herr Ober, haben Sie Froschschenkel?' 'Ja.' 'Dann hüpfen Sie mal und bringen Sie mir ein Bier!'")
    jokes.append("Fragt der Psychiater seinen Patienten: 'Halten Sie sich schon lange für einen Prinzen?' - 'Nein, erst seitdem ich kein Frosch mehr bin!'")
    jokes.append("Der Fotograf will vom Breitmaulfrosch ein Foto machen, doch er passt einfach nicht aufs Foto! Da hat er eine Idee: 'Sag mal Konfitüüüre!' - 'Konfitüüüre' - 'Okay, jetzt machen wir das Foto!' - 'Marmelade!' ")
	
    message = _(jokes[randomjokenr])
    yield from bot.coro_send_message(event.conv_id, message)
