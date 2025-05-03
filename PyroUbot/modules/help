import asyncio

from config import BOT_NAME, HELPABLE 
from Navy import bot, dB 
from Navy.helpers import CMD, ButtonUtils, Emoji 


__MODULES__ = "Set sticker"
__HELP__ = """Command Help **Set sticker**
    
**Set sticker ping**
    **You can set ping sticker with this command**
        `{0}setsping` (reply) 

**Set sticker help**
    **You can set help sticker with this command**
        `{0}setshelp` (reply) 
    
   {1}
""" 

@CMD.UBOT("setshelp|setpay")
async def _(client, message):
    em = Emoji(client)
    await em.get()
    reply = message.reply_to_message
    if not reply:
        return await message.reply_text(f"{em.gagal}**Reply to sticker!**")

    try:
        await dB.set_var(client.me.id, "help_sticker", reply.sticker.file_id)
        return await message.reply_text(f"{em.sukses}**Successfully set vars help stickers!**")
    except Exception as e:
        return await message.reply_text(f"{em.gagal}**error{str(e)}**")

 
@CMD.UBOT("help|pay") 
async def _(client, message): 
    data = await dB.get_var(client.me.id, "help_sticker") or "CAACAgUAAyEGAASMNRIdAAJYymgVNd9r1clFDKJfY31b61zrVtPgAAIXEQACGZcxVfl9ebXiDkmBHgQ" 
    sticker = await message.reply_sticker(data) 
    em = Emoji(client) 
    await em.get() 
    if not client.get_arg(message): 
        query = "help" 
        chat_id = ( 
            message.chat.id if len(message.command) < 2 else message.text.split()[1] 
        ) 
        try: 
            await asyncio.sleep(5) 
            await sticker.delete() 
            inline = await ButtonUtils.send_inline_bot_result( 
                message, 
                chat_id, 
                bot.me.username, 
                query, 
            ) 
            if inline: 
                return await message.delete() 
        except Exception as error: 
            return await message.reply(f"{em.gagal}Error: {str(error)}") 
    else: 
        nama = f"{client.get_arg(message)}" 
        pref = client.get_prefix(client.me.id) 
        x = next(iter(pref)) 
        text_help2 = f"ᴛᴇɪᴋᴏɴᴀɴ ᴜsᴇʀʙᴏᴛ ᴍᴜʟᴛɪᴅᴇᴠɪᴄᴇ" 
        await asyncio.sleep(7) 
        await sticker.delete() 
        if nama in HELPABLE: 
            return await message.reply( 
                f"{HELPABLE[nama].__HELP__.format(x, text_help2)}", 
            ) 
        else: 
            return await message.reply( 
                f"{em.gagal}Tidak ada modul bernama {nama}" 
            )
