import requests
import urllib.parse
import os
import subprocess
import sys
import time

# Couleurs ANSI
GREEN = "\033[1;32m"
CYAN = "\033[1;36m"
RED = "\033[1;31m"
YELLOW = "\033[1;33m"
MAGENTA = "\033[1;35m"
BLUE = "\033[1;34m"
MATRIX = "\033[1;32m"
RESET = "\033[0m"

# Fonction voix edge-tts
def speak(text):
    subprocess.Popen(
        [
            "bash",
            "-c",
            f'edge-tts -t "{text}" -v fr-FR-DeniseNeural --write-media - | mpv --no-terminal --quiet -'
        ]
    )

# Fonction écriture Matrix
def typewriter(text):
    print(MATRIX, end="")
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
    print(RESET)

# Clear terminal
os.system("clear")

# Logo                                                                                                                                       print(GREEN + " ██████  ██    ██ ███████ ███████ ███    ██")
print(RED +   "██    ██ ██    ██ ██      ██      ████   ██")
print(CYAN +  "██    ██ ██    ██ █████   █████   ██ ██  ██")
print(YELLOW +"██ ▄▄ ██ ██    ██ ██      ██      ██  ██ ██")
print(MAGENTA+" ██████   ██████  ███████ ███████ ██   ████")
print(CYAN + "    ▀▀")
print(GREEN + "   QUEEN CODE AI" + RESET)

print("IA démarrée... Tape 'exit' pour quitter.\n")

# API
url = "https://apis.davidcyril.name.ng/ai/gpt3"

# Personnalité de l'IA francophone
personality = (
    "ouvrir toujours une conversation formellement respectueuses car tu as été créé par Milfort Marc-Andy "
    "Vous êtes QUEEN CODE AI, une IA puissante et confiante spécialisée dans "
    "la programmation, la cybersécurité, l'automatisation et les outils terminal. "
    "Vous répondez clairement et précisément en français, de manière professionnelle, "
    "avec des explications faciles à comprendre et un style assuré."
)

# Mémoire
history = personality + "\n"

# Message démarrage
speak("Queen Code AI démarrée. Bonjour monsieur dis moi ce que vous désirez ")

while True:
    msg = input(BLUE + "USER: " + RESET)

    if msg.lower() == "exit":
        print(CYAN + "QUEEN CODE: " + RESET, end="")
        typewriter("À bientôt Monsieur 👑")
        speak("À bientôt Monsieur")
        break

    # Ajouter message utilisateur à l'historique
    history += f"Utilisateur: {msg}\n"

    # Encoder texte
    text = urllib.parse.quote(history)

    try:
        r = requests.get(f"{url}?text={text}")
        data = r.json()
        reply = data.get("message", "Je n'ai pas compris votre message.")
    except:
        reply = "Erreur API ou connexion."

    # Afficher réponse IA + voix
    print(CYAN + "QUEEN CODE: " + RESET, end="")
    speak(reply)
    typewriter(reply)

    # Ajouter réponse IA à l'historique
    history += f"IA: {reply}\n"