# CantarellaBots
# Don't Remove Credit
# Telegram Channel @CantarellaBots
#Supoort group @rexbotschat
from pyrogram import Client, filters
from pyrogram.types import Message
from database import db
# CantarellaBots
# Don't Remove Credit
# Telegram Channel @CantarellaBots
#Supoort group @rexbotschat
@Client.on_message(filters.command("history"))
async def history(client: Client, message: Message):
    if not db:
        return await message.reply_text("**⚠️ Dᴀᴛᴀʙᴀꜱᴇ Nᴏᴛ Cᴏɴɴᴇᴄᴛᴇᴅ!**")
    
    msg = await message.reply_text("⏳ Fᴇᴛᴄʜɪɴɢ Hɪsᴛᴏʀʏ...")
    
    uploads = await db.get_history(message.from_user.id)
    
    if not uploads:
        return await msg.edit_text("**📂 Yᴏᴜ ʜᴀᴠᴇ ɴᴏ ᴜᴘʟᴏᴀᴅ ʜɪꜱᴛᴏʀʏ ʏᴇᴛ.**")
    
    txt = "**🗂️ Yᴏᴜʀ Lᴀꜱᴛ 10 Uᴘʟᴏᴀᴅꜱ:**\n\n"
    
    for i, item in enumerate(reversed(uploads), 1):
        link = item['link']
        txt += f"{i}. {link}\n"
        
    await msg.edit_text(txt, disable_web_page_preview=True)
# CantarellaBots
# Don't Remove Credit
# Telegram Channel @CantarellaBots
#Supoort group @rexbotschat