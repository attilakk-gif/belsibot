from telegram.ext import Updater, MessageHandler, Filters
import os
import random

TOKEN = os.getenv("TOKEN")

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
        "🥰 💦💦"
        "Trump è meglio di Kamala che è meglio di rintrobidet"
    ],
    ("bibi",): [
        "bibi mon amour"
    ],
    ("prova",): [
        " ping "
    ],
    ("esperto",): [
        "beeeeeeeeeeehhhhhhh",
        "quanta potenza!"
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

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
