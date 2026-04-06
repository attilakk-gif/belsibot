from telegram.ext import Updater, MessageHandler, Filters
import os
import random

TOKEN = os.getenv("TOKEN")

# Dizionario TRIGGER → LISTA DI RISPOSTE
TRIGGERS = {
    "bidet": [
        "pagliaccio 🤡🤡🤡",
        "vecchio rincoglionito"      
    ],
    "russi": [
        "popolo di merde!",
        "schiavi",
        "pellai"        
    ],
    "fattura": [
        "ma c'aa fattura",
    ],
    "sara": [ 
        "posa codesti ciottoli e vieni vì"
    ],

    "trump": [
        "🥰 💦💦"
    ],
    "bibi": [
        "bibi mon amour"
],
    "prova": [
        " ping "
    ],
    "esperto": [
        "beeeeeeeeeeehhhhhhh"
    ],
}
def ascolta(update, context):
    if update.message and update.message.text:
        testo = update.message.text.lower()

        for trigger, risposte in TRIGGERS.items():
            if trigger in testo:
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
