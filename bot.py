from telegram.ext import Updater, MessageHandler, Filters
from apscheduler.schedulers.background import BackgroundScheduler
import os
import random
import pytz

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

DISTRO_DEL_GIORNO = [
    "Arch Linux", "Gentoo", "Slackware", "Debian", "Ubuntu", "Fedora",
    "Linux Mint", "Manjaro", "Pop!_OS", "openSUSE", "Void Linux",
    "Alpine Linux", "NixOS", "Artix Linux", "EndeavourOS", "Garuda Linux",
    "Kali Linux", "Tails", "Whonix", "Qubes OS", "FreeBSD", "OpenBSD",
    "NetBSD", "Haiku", "ReactOS", "MX Linux", "Zorin OS", "elementary OS",
    "deepin", "Solus", "Clear Linux", "Bedrock Linux", "KISS Linux",
    "Chimera Linux", "Adelie Linux", "Devuan", "antiX", "Puppy Linux",
    "Tiny Core Linux", "DSL (Damn Small Linux)", "SliTaz", "TempleOS",
    "Hannah Montana Linux", "Gobolinux", "Linspire", "Yggdrasil Linux",
]

# Dizionario: TUPLA DI TRIGGER → LISTA DI RISPOSTE
TRIGGERS = {
    ("bidet", "biden"): [
        "pagliaccio 🤡🤡🤡",
        "vecchio rincoglionito",
        "rintrobidet"
    ],
    ("russi", "russia"): [
        "popolo di schiavi!",
        "merde",
        "pellai",
        "devono soffrire",
    ],
    ("fattura",): [
        "ma c'aa fattura"
    ],
    ("sara",): [ 
        "posa codesti ciottoli e vieni vì"
    ],
    ("trump",): [
        "🥰 💦💦",
        "Trump è meglio di Kamala che è meglio di rintrobidet",
        "Bidet pagliaccio!"
    ],
    ("bibi",): [
        "bibi mon amour"
    ],
    ("prova",): [
        " ping "
    ],
    ("esperto",): [
        "beeeeeeeeeeehhhhhhh",
        "quanta potenza!",
        "AAA",
        "assai!",
        "ce la so più del Kaiser",
        "Minchia!"
    ],
    ("numeri",): [
        "numeri di hamas, in tunnel di hamas pieni di attori di hamas"
    ],
    ("belsy",): [
        "beeeeeeeeeeehhhhhhh",
        "eccolo!",
        "quanta potenza!",
        "è tutto, tutto degradato",
        "fa fattura?",
        "ti frantumo le mucose",
        ": sangue a ettolitri"
    ],
}

def manda_distro(bot):
    distro = random.choice(DISTRO_DEL_GIORNO)
    bot.send_message(chat_id=CHAT_ID, text=f"🐧 Distro Linux del giorno: *{distro}*", parse_mode="Markdown")

def ascolta(update, context):
    if update.message and update.message.text:
        testo = update.message.text.lower()
        for triggers, risposte in TRIGGERS.items():
            # Controlla se almeno uno dei trigger è nel testo
            if any(trigger in testo for trigger in triggers):
                update.message.reply_text(random.choice(risposte))
                return

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, ascolta))

    fuso_orario = pytz.timezone("Europe/Rome")
    scheduler = BackgroundScheduler(timezone=fuso_orario)
    scheduler.add_job(manda_distro, trigger="cron", hour=15, minute=00, args=[updater.bot])
    scheduler.start()

    updater.start_polling()
    updater.idle()
    scheduler.shutdown()
