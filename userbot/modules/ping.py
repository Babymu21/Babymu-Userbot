# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
# Ported by @mrismanaziz
# FROM Man-Userbot
# ReCode by @Pocongonlen

import random
import time
from datetime import datetime
from speedtest import Speedtest
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, StartTime, bot, DEVS
from userbot.events import register
from userbot.utils import edit_or_reply, humanbytes, poci_cmd

absen = [
    "**Hadir Cantik** π",
    "**Hadir kak** π",
    "**Hadir dong** π",
    "**Hadir Cantik** π₯΅",
    "**Hadir bro** π",
    "**Hadir kak Cantik maap telat** π₯Ί",
]


misi = [
    "**Silahkan lewat cantik** π",
    "**Kaka cantik mau kemana** ππ»",
    "**Monggo kaka cantik ** π₯΅",
    "**iya lewat Hati hati ya kaka cantikπ₯°**",
    "**Silahkan kaka cantik** π₯°",
    "**Iya kaka cantik lewat aja π**",
    "**Wih kaka cantik mau kemana niπ€­**",
    
]


hai = [
    "**Eh bang Zaen** π",
    "**Bang Zaen dari mana aja** π",
    "**Dari mana aja bang baru on ** π",
    "**Hai bang Zaen gmn kabarnyaπ₯°**",
    "**Lord Zaen datang ni** π₯΅",
    "**Hai juga bang Zaen π**"
    
]
async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@poci_cmd(pattern="ping$")
async def _(ping):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xx = await edit_or_reply(ping, "****")
    await xx.edit("**P**")
    await xx.edit("**Po**")
    await xx.edit("**Pon**")
    await xx.edit("**Pong**")
    await xx.edit("**Pong!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await bot.get_me()
    await xx.edit(
        f"**ππππππ-πππππππ!!**\n"
        f"β‘ **Ping**  `%sms`\n"
        f"β³ **BotUptime** `{uptime}` \n"
        f"π€ **BotOf** [{user.first_name}](tg://user?id={user.id})" % (duration)
    )

@poci_cmd(pattern="rping$")
async def _(pong):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    ram = await edit_or_reply(pong, "**Mengecek Sinyal...**")
    await ram.edit("**0% ββββββββββ**")
    await ram.edit("**20% ββββββββββ**")
    await ram.edit("**40% ββββββββββ**")
    await ram.edit("**60% ββββββββββ**")
    await ram.edit("**80% ββββββββββ**")
    await ram.edit("**100% ββββββββββ**")
    await ram.edit("β¨")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await pong.client.get_me()
    await ram.edit(
        f"**π₯ππ’π‘π§π’π-π πππππππ₯**\n"
        f"** β   SΙͺΙ’Ι΄α΄Κ   :** "
        f"`%sms` \n"
        f"** β   Uα΄α΄Ιͺα΄α΄  :** "
        f"`{uptime}` \n"
        f"** β   Oα΄‘Ι΄α΄Κ   :** [{user.first_name}](tg://user?id={user.id})" % (duration)
    )

#  .Coded by Ramadhani RAM-UBOT

@poci_cmd(pattern="tping$")
async def _(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**Kontol**")
    await pong.edit("__**Kontolβ‘**__")
    await pong.edit("__**kontoβ‘l**__")
    await pong.edit("__**konβ‘tol**__")
    await pong.edit("__**kβ‘ontol**__")
    await pong.edit("__**β‘kontolβ‘**__")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"**β‘Kontol α΄ΙͺΙ΄Ι’β‘**\n"
        f"β‘ **α΄ΙͺΙ΄Ι’:** "
        f"`%sms` \n"
        f"β‘ **α΄Ι΄ΚΙͺΙ΄α΄:** "
        f"`{uptime}` \n" % (duration))

#  .Coded by alvin Lord-Userbot

@poci_cmd(pattern="fping$")
async def _(pong):
    """ For .ping command, ping the userbot from any chat.  """
    start = datetime.now()
    await pong.edit("`Pong.....π`")
    await pong.edit("`Pong....π.`")
    await pong.edit("`Pong...π..`")
    await pong.edit("`Pong..π...`")
    await pong.edit("`Pong.π....`")
    await pong.edit("`Pongπ.....`")
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await pong.edit("β **Ping!**\n`%sms`" % (duration))

#  .Coded by alvin Lord-Userbot

@poci_cmd(pattern="speedtest$")
async def _(speed):
    """For .speedtest command, use SpeedTest to check server speeds."""
    xxnx = await edit_or_reply(speed, "`Running speed test...`")
    test = Speedtest()
    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()
    msg = (
        f"**Started at {result['timestamp']}**\n\n"
        "**Client**\n"
        f"**ISP :** `{result['client']['isp']}`\n"
        f"**Country :** `{result['client']['country']}`\n\n"
        "**Server**\n"
        f"**Name :** `{result['server']['name']}`\n"
        f"**Country :** `{result['server']['country']}`\n"
        f"**Sponsor :** `{result['server']['sponsor']}`\n\n"
        f"**Ping :** `{result['ping']}`\n"
        f"**Upload :** `{humanbytes(result['upload'])}/s`\n"
        f"**Download :** `{humanbytes(result['download'])}/s`"
    )
    await xxnx.delete()
    await speed.client.send_file(
        speed.chat_id,
        result["share"],
        caption=msg,
        force_document=False,
    )


@poci_cmd(pattern="pong$")
async def _(pong):
    """For .ping command, ping the userbot from any chat."""
    start = datetime.now()
    xx = await edit_or_reply(pong, "`Gass!`")
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await xx.edit("π **Ping!**\n`%sms`" % (duration))


@poci_cmd(pattern=r"kping$")
async def _(pong):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    kping = await edit_or_reply(pong, "8β===D")
    await kping.edit("8=β==D")
    await kping.edit("8==β=D")
    await kping.edit("8===βD")
    await kping.edit("8==β=D")
    await kping.edit("8=β==D")
    await kping.edit("8β===D")
    await kping.edit("8=β==D")
    await kping.edit("8==β=D")
    await kping.edit("8===βD")
    await kping.edit("8==β=D")
    await kping.edit("8=β==D")
    await kping.edit("8β===D")
    await kping.edit("8=β==D")
    await kping.edit("8==β=D")
    await kping.edit("8===βD")
    await kping.edit("8===βDπ¦")
    await kping.edit("8====Dπ¦π¦")
    await kping.edit("**CROOTTTT KONTOLLL PINGGGG!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await kping.edit(
        f"**KONTOllll NGENTOT!!!  π¨**\n**KAMPANG** : %sms\n**Bot Uptime** : {uptime}π" % (duration)
    )


@poci_cmd(pattern="keping$")
async def _(pong):
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    kopong = await edit_or_reply(pong, "**γβππππππγ**")
    await kopong.edit("**ββπππππππββ**")
    await kopong.edit("**ππππππππ ππππ πππ πππ**")
    await kopong.edit("**β¬ππππ πππππππ ππππππππ πππβ¬**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await pong.client.get_me()
    await kopong.edit(
        f"**β² πΊπΎπ½ππΎπ» πΌπ΄π»π΄π³ππΆ** "
        f"\n β«Έ α΄·α΅βΏα΅α΅Λ‘ `%sms` \n"
        f"**β² π±πΈπΉπΈ πΏπ΄π»π΄π** "
        f"\n β«Έ α΄·α΅α΅α΅α΅βΏα΅γ[{user.first_name}](tg://user?id={user.id})γ \n" % (duration)
    )


# .keping & kping Coded by Koala



# KALO NGEFORK absen ini GA USAH DI HAPUS YA GOBLOK π‘
@register(incoming=True, from_users=DEVS, pattern=r"^.absen$")
async def Zaen(ganteng):
    await ganteng.reply(random.choice(absen))

@register(incoming=True, from_users=1608831215, pattern=r"^.misi$")
async def Zaen(ganteng):
    await ganteng.reply(random.choice(misi))

@register(incoming=True, from_users=2010825200, pattern=r"^.hai$")
async def Zaen(ganteng):
    await ganteng.reply(random.choice(hai))



CMD_HELP.update(
    {
        "ping": f"**Plugin : **`ping`\
        \n\n  β’  **Syntax :** `{cmd}ping`\
        \n  β’  **Function : **Untuk menunjukkan ping userbot.\
        \n\n  β’  **Syntax :** `{cmd}keping`\
        \n  β’  **Function : **Untuk menunjukkan keping userbot.\
        \n\n  β’  **Syntax :** `{cmd}pong`\
        \n  β’  **Function : **Sama seperti perintah ping\
        \n\n  β’  **Syntax :** `{cmd}kping`\
        \n  β’  **Function : **Untuk menunjukkan kping userbot.\
        \n\n  β’  **Syntax :** `{cmd}rping`\
        \n  β’  **Function : **Untuk menunjukkan rping userbot.\
        \n\n  β’  **Syntax :** `{cmd}tping`\
        \n  β’  **Function : **Untuk menunjukkan tping userbot.\
        \n\n  β’  **Syntax :** `{cmd}fping`\
        \n  β’  **Function : **Untuk menunjukkan fping userbot.\
    "
    }
)


CMD_HELP.update(
    {
        "speedtest": f"**Plugin : **`speedtest`\
        \n\n  β’  **Syntax :** `{cmd}speedtest`\
        \n  β’  **Function : **Untuk Mengetes kecepatan server userbot.\
    "
    }
)
