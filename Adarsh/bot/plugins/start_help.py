# (c) adarsh-goel 
from Adarsh.bot import StreamBot
from Adarsh.vars import Var
import logging
logger = logging.getLogger(__name__)
from Adarsh.bot.plugins.stream import MY_PASS
from Adarsh.utils.human_readable import humanbytes
from Adarsh.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from Adarsh.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.SESSION_NAME)
from pyrogram.types import ReplyKeyboardMarkup

                      
@StreamBot.on_message(filters.command('start') & filters.private & ~filters.edited)
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{m.from_user.first_name}](tg://user?id={m.from_user.id}) Started !!"
        )
    usr_cmd = m.text.split("_")[-1]
    if usr_cmd == "/start":
        if Var.UPDATES_CHANNEL is not None:
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "banned":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="**ππΎπ π°ππ΄ π±π°π½π½π΄π³../**",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**πΉπΎπΈπ½ πΌπ ππΏπ³π°ππ΄π π²π·π°π½π½π΄π» ππΎ πππ΄ πΌπ΄..**\n\n**π³ππ΄ ππΎ πΎππ΄ππ»πΎπ°π³ πΎπ½π»π π²π·π°π½π½π΄π» πππ±ππ²ππΈπ±π΄ππ π²π°π½ πππ΄ ππ·πΈπ π±πΎπ..!**",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("πΉπΎπΈπ½ ππΏπ³π°ππ΄π π²π·π°π½π½π΄π»", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]
                        ]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**π°π³π³ π΅πΎππ²π΄ πππ± ππΎ π°π½π π²π·π°π½π½π΄π»**",
                    parse_mode="markdown",
                    disable_web_page_preview=True)
                return
        await m.reply_text(
            text="**π·π΄π»π»πΎ...β‘**\n\n**πΈπ°πΌ π° ππΈπΌπΏπ»π΄ ππ΄π»π΄πΆππ°πΌ π΅πΈπ»π΄/ππΈπ³π΄πΎ ππΎ πΏπ΄ππΌπ°π½π΄π½π π»πΈπ½πΊ πΆπ΄π½π΄ππ°ππΎπ π±πΎπ.**\n\n**πΈ π²π°π½ πΆπ΄π½π΄ππ°ππ΄ π³πΈππ΄π²π π³πΎππ½π»πΎπ°π³ π»πΈπ½πΊ π΅πΎπ π°π½π ππΈπ³π΄πΎ/π΅πΈπ»π΄π π΅πΎπ π³πΎππ½π»πΎπ°π³πΈπ½πΆ πΎπ½π»πΈπ½π΄ & π΅πΎπ ππππ΄π°πΌπΈπ½πΆ..\n\nπππ΄ /help π΅πΎπ πΌπΎππ΄ π³π΄ππ°πΈπ»π...\n\nππ΄π½π³ πΌπ΄ π°π½π ππΈπ³π΄πΎ/π΅πΈπ»π΄ ππΎ ππ΄π΄ πΌπ πΏπΎππ΄ππ....**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("β‘ ππΏπ³π°ππ΄π β‘", url="https://t.me/unique_coders_x"), InlineKeyboardButton("β‘ πππΏπΏπΎππ β‘", url="https://t.me/unique_coders_x")],
                    [InlineKeyboardButton("πΈ π³πΎπ½π°ππ΄ πΈ", url="https://t.me/unique_coders_x"), InlineKeyboardButton("π  πΆπΈππ·ππ± π ", url="https://github.com/Aadhi000")],
                    [InlineKeyboardButton("π πππ±ππ²ππΈπ±π΄ π", url="https://t.me/unique_coders_x")]
                ]
            ),
            disable_web_page_preview=True
        )
    else:
        if Var.UPDATES_CHANNEL is not None:
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "banned":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="**ππΎπ π°ππ΄ π±π°π½π½π΄π³../**",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**πΉπΎπΈπ½ πΌπ ππΏπ³π°ππ΄π π²π·π°π½π½π΄π» ππΎ πππ΄ πΌπ΄..**\n\n**π³ππ΄ ππΎ πΎππ΄ππ»πΎπ°π³ πΎπ½π»π π²π·π°π½π½π΄π» πππ±ππ²ππΈπ±π΄ππ π²π°π½ πππ΄ ππ·πΈπ π±πΎπ..!**",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("πΉπΎπΈπ½ ππΏπ³π°ππ΄π π²π·π°π½π½π΄π»", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]                           
                        ]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**π°π³π³ π΅πΎππ²π΄ πππ± ππΎ π°π½π π²π·π°π½π½π΄π»**",
                    parse_mode="markdown",
                    disable_web_page_preview=True)
                return

        get_msg = await b.get_messages(chat_id=Var.BIN_CHANNEL, message_ids=int(usr_cmd))

        file_size = None
        if get_msg.video:
            file_size = f"{humanbytes(get_msg.video.file_size)}"
        elif get_msg.document:
            file_size = f"{humanbytes(get_msg.document.file_size)}"
        elif get_msg.audio:
            file_size = f"{humanbytes(get_msg.audio.file_size)}"

        file_name = None
        if get_msg.video:
            file_name = f"{get_msg.video.file_name}"
        elif get_msg.document:
            file_name = f"{get_msg.document.file_name}"
        elif get_msg.audio:
            file_name = f"{get_msg.audio.file_name}"

        stream_link = "https://{}/{}".format(Var.FQDN, get_msg.message_id) if Var.ON_HEROKU or Var.NO_PORT else \
            "http://{}:{}/{}".format(Var.FQDN,
                                     Var.PORT,
                                     get_msg.message_id)

        msg_text = "**ππΎππ π»πΈπ½πΊ πΈπ πΆπ΄π½π΄ππ°ππ΄π³...β‘\n\nπ§ π΅πΈπ»π΄ π½π°πΌπ΄ :-\n{}\n {}\n\nπ π³πΎππ½π»πΎπ°π³ π»πΈπ½πΊ :- {}\n\nβ»οΈ ππ·πΈπ π»πΈπ½πΊ πΈπ πΏπ΄ππΌπ°π½π΄π½π π°π½π³ ππΈπ»π» π½πΎπ π΄ππΏπΈππ΄ β»οΈ\n\n@Unique_Coders_x**"
        await m.reply_text(
            text=msg_text.format(file_name, file_size, stream_link),
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("β‘ π³πΎππ½π»πΎπ°π³ π½πΎπ β‘", url=stream_link)]])
        )


@StreamBot.on_message(filters.command('help') & filters.private & ~filters.edited)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) Started !!"
        )
    if Var.UPDATES_CHANNEL is not None:
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "banned":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="**ππΎπ π°ππ΄ π±π°π½π½π΄π³../**",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**πΉπΎπΈπ½ πΌπ ππΏπ³π°ππ΄π π²π·π°π½π½π΄π» ππΎ πππ΄ πΌπ΄..**\n\n**π³ππ΄ ππΎ πΎππ΄ππ»πΎπ°π³ πΎπ½π»π π²π·π°π½π½π΄π» πππ±ππ²ππΈπ±π΄ππ π²π°π½ πππ΄ ππ·πΈπ π±πΎπ..!**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("πΉπΎπΈπ½ ππΏπ³π°ππ΄π π²π·π°π½π½π΄π»", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**π°π³π³ π΅πΎππ²π΄ πππ± ππΎ π°π½π π²π·π°π½π½π΄π»**",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text="**β£βͺΌ ππ΄π½π³ πΌπ΄ π°π½π π΅πΈπ»π΄/ππΈπ³π΄πΎ ππ·π΄π½ πΈ ππΈπ»π» πΆπΈππ΄ ππΎπ πΏπ΄ππΌπ°π½π΄π½π ππ·π°ππ°π±π»π΄ π»πΈπ½πΊ πΎπ΅ πΈπ...\n\nβ£βͺΌ ππ·πΈπ π»πΈπ½πΊ π²π°π½ π±π΄ πππ΄π³ ππΎ π³πΎππ½π»πΎπ°π³ πΎπ ππΎ ππππ΄π°πΌ πππΈπ½πΆ π΄πππ΄ππ½π°π» ππΈπ³π΄πΎ πΏπ»π°ππ΄ππ ππ·ππΎππΆπ· πΌπ ππ΄πππ΄π.\n\nβ£βͺΌ π΅πΎπ ππππ΄π°πΌπΈπ½πΆ πΉπππ π²πΎπΏπ ππ·π΄ π»πΈπ½πΊ π°π½π³ πΏπ°πππ΄ πΈπ πΈπ½ ππΎππ ππΈπ³π΄πΎ πΏπ»π°ππ΄π ππΎ πππ°ππ ππππ΄π°πΌπΈπ½πΆ.\n\nβ£βͺΌ ππ·πΈπ π±πΎπ πΈπ π°π»ππΎ πππΏπΏπΎππ πΈπ½ π²π·π°π½π½π΄π»π. π°π³π³ πΌπ΄ ππΎ ππΎππ π²π·π°π½π½π΄π» π°π π°π³πΌπΈπ½ ππΎ πΆπ΄π ππ΄π°π»ππΈπΌπ΄ π³πΎππ½π»πΎπ°π³ π»πΈπ½πΊ π΅πΎπ π΄ππ΄ππ π΅πΈπ»π΄/ππΈπ³π΄πΎ πΏπΎππ../\n\nβ£βͺΌ π΅πΎπ πΌπΎππ΄ πΈπ½π΅πΎππΌπ°ππΈπΎπ½ :- /about\n\n\nπΏπ»π΄π°ππ΄ ππ·π°ππ΄ π°π½π³ πππ±ππ²ππΈπ±π΄**", 
  parse_mode="Markdown",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("β‘ ππΏπ³π°ππ΄π β‘", url="https://t.me/unique_coders_x"), InlineKeyboardButton("β‘ πππΏπΏπΎππ β‘", url="https://t.me/unique_coders_x")],
                [InlineKeyboardButton("πΈ π³πΎπ½π°ππ΄ πΈ", url="https://t.me/unique_coders_x"), InlineKeyboardButton("π  πΆπΈππ·ππ± π ", url="https://github.com/Aadhi000")],
                [InlineKeyboardButton("π πππ±ππ²ππΈπ±π΄ π", url="https://t.me/unique_coders_x")]
            ]
        )
    )

@StreamBot.on_message(filters.command('about') & filters.private & ~filters.edited)
async def about_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) Started !!"
        )
    if Var.UPDATES_CHANNEL is not None:
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "banned":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="**ππΎπ π°ππ΄ π±π°π½π½π΄π³../**",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**πΉπΎπΈπ½ πΌπ ππΏπ³π°ππ΄π π²π·π°π½π½π΄π» ππΎ πππ΄ πΌπ΄..**\n\n**π³ππ΄ ππΎ πΎππ΄ππ»πΎπ°π³ πΎπ½π»π π²π·π°π½π½π΄π» πππ±ππ²ππΈπ±π΄ππ π²π°π½ πππ΄ ππ·πΈπ π±πΎπ..!**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("πΉπΎπΈπ½ ππΏπ³π°ππ΄π π²π·π°π½π½π΄π»", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**π°π³π³ π΅πΎππ²π΄ πππ± ππΎ π°π½π π²π·π°π½π½π΄π»**",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text="""<b>ππΎπΌπ΄ππ·πΈπ½πΆ π°π±πΎππ πΌπ΄</b>

<b>β­βββββββγπ΅πΈπ»π΄-ππΎ-π»πΈπ½πΊ π±πΎπγ</b>
β
β£βͺΌ<b>π±πΎπ-π½π°πΌπ΄ : <a href='https://github.com/Aadhi000/File-To-Link'>π΅πΈπ»π΄-ππΎ-π»πΈπ½πΊ</a></b>
β£βͺΌ<b>ππΏπ³π°ππ΄π : <a href='https://t.me/unique_coders_x'>Unique_Coders</a></b>
β£βͺΌ<b>πππΏπΏπΎππ : <a href='https://t.me/unique_coders_x'>Unique_coders</a></b>
β£βͺΌ<b>ππ΄πππ΄π : π·π΄πππΊπΎ</b>
β£βͺΌ<b>π»πΈπ±ππ°ππ : πΏππΎπΆππ°πΌ</b>
β£βͺΌ<b>π»π°π½πΆππ°πΆπ΄: πΏπππ·πΎπ½ 3</b>
β£βͺΌ<b>ππΎπππ²π΄-π²πΎπ³π΄ : <a href='https://github.com/Aadhi000/File-To-Link'>π΅πΈπ»π΄-ππΎ-π»πΈπ½πΊ</a></b>
β£βͺΌ<b>ππ-π²π·π°π½π½π΄π» : <a href='https://youtube.com/channel/UCf_dVNrilcT0V2R--HbYpMA'>Unique_Coders_x</a></b>
β
<b>β°βββββββγπΏπ»π΄π°ππ΄ πππΏπΏπΎππγ</b>""",
  parse_mode="html",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("β‘ ππΏπ³π°ππ΄π β‘", url="https://t.me/unique_coders_x"), InlineKeyboardButton("πΈ π³πΎπ½π°ππ΄ πΈ", url="https://paypal.me/114912Aadil")],
                [InlineKeyboardButton("π πππ±ππ²ππΈπ±π΄ π", url="https://t.me/unique_coders_x")]
            ]
        )
    )
