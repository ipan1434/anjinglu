import aiohttp
import filetype
from io import BytesIO
from PyroUbot import *

__MODULE__ = "ᴛᴏᴜʀʟ"
__HELP__ = """
<blockquote><b>Bantuan untuk tourl

Perintah : <code>{0}tourl</code> [reply media/text]
    Mengupload media ke uguu.se dan memberikan link.</b></blockquote>
"""

async def upload_file(buffer: BytesIO) -> str:
    kind = filetype.guess(buffer)
    if kind is None:
        raise ValueError("Cannot determine file type")
    ext = kind.extension

    buffer.seek(0)
    form = aiohttp.FormData()
    form.add_field(
        'files[]',
        buffer,
        filename='file.' + ext,
        content_type=kind.mime
    )

    async with aiohttp.ClientSession() as session:
        async with session.post('https://uguu.se/upload.php', data=form) as response:
            if response.status != 200:
                raise Exception(f"Failed to upload file: {response.status}")
            json_response = await response.json()
            return json_response["files"][0]["url"]

@PY.UBOT("tourl|tg")
async def _(client, message):
    reply_message = message.reply_to_message
    if reply_message and reply_message.media:
        downloaded_file = await reply_message.download()
        
        with open(downloaded_file, 'rb') as f:
            buffer = BytesIO(f.read())
            try:
                media_url = await upload_file(buffer)
                await message.reply(
                    f"<b>Berhasil diupload ke: <a href='{media_url}'>uguu.se</a></b>",
                    disable_web_page_preview=False
                )
            except Exception as e:
                await message.reply(f"Error: {e}")
    else:
        await message.reply("Balas pesan media untuk diupload ke uguu.se.")
