import aiofiles, asyncio, io, logging, os, re, sys
import plugins


logger = logging.getLogger(__name__)

def _initialise(bot):
    plugins.register_user_command(["sendpic"])

@asyncio.coroutine
def sendpic(bot, event):

        filename = "~/picture.png"

        r = yield from aiofiles.open(filename, mode='rb')
        try:
            raw = yield from r.read()
        finally:
            yield from r.close()

        image_data = io.BytesIO(raw)
        image_id = yield from bot._client.upload_image(image_data, filename=filename)
        yield from bot.coro_send_message(event.conv.id_, None, image_id=image_id)