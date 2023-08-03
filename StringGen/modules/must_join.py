from pyrogram import Client, filters

ch = "spzohary"

@Client.on_message(filters.private)
async def me(client, message):
  if message.from_user.id not in [6199134030,6392010766,5839884860,5552799584]:
   try:
      await client.get_chat_member(ch, message.from_user.id)
   except:
      return await message.reply_text(f"يجب ان تشترك ف قناة السورس أولا \n https://t.me/{ch}")
  message.continue_propagation()
