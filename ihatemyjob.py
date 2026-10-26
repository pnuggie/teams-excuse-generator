import tkinter as bajoingus
import random

excuses = [
    "I apologise, but it seems that my computer is in a superposition, and I cannot touch it until I am 100% able to confirm it did not turn into a bomb.",
    "What?",
    "Ich kann nur Deutsch sprechen. Wenn du jedoch auf Deutsch antwortest, werde ich die gesamte deutsche Sprache vergessen. Danach werde ich mein OS löschen. Bitte kontaktiere mich nicht.",
    "I don't want to.",
    "I am unable to proceed, due to an infinite number of factors in which I am still in the process in organising their importance in my project hierarchy.",
    "I am going on a flight tomorrow, I cannot give details, if you ask me anything you will get no answer, I am not sure of my return date.",
    "I want to preserve my spot in the line. The line for what? Confidential.",
    "I am currently debugging a program written in Mandarin. My proficiency level is A1.",
    "ahdd6478jzbxmsvCSBDXNZXJSWJsxjdx7vevvr85r9",
    "We can circle back to that, once my Linkedin profile is completed. I'm currently in the process of advertising my AI workflow optimiser app. Do you want to try?",
    "I am currently reading an article about rejecting people. It says we should all get more confident in saying no to things that go against our boundaries. I'm setting one now, with you.",
    "BECAUSE I FUCKING HATE YOU LOSER",
    "What time are you unavailable? I'll make sure to prioritise completing my work during those hours.",
    "I am unable to attend because I have not been informed of the meeting in a way that makes me want to attend.",
    "I am unable to attend because I am unable to attend. Kesesesesese...",
]

window = bajoingus.Tk()
window.title("Teams Excuse Generator")
window.geometry("600x500")

excuselabel = bajoingus.Label(
    window,
    text="Welcome! Do you no longer have excuses to decline corporate events? Or anything, for that matter? Then don't worry, because this will make everything easy for you! Just click the button below and paste whichever response you like the best.",
    wraplength=520,
    font=("Arial", 18),
    justify="center"
)
excuselabel.pack(expand=True, fill="both", padx=30, pady=30)

def generateexcuse():
    excuselabel.config(text=random.choice(excuses))

def copyexcuse(): # honestly didnt even know this was possible
    window.clipboard_clear()
    window.clipboard_append(excuselabel.cget("text"))

excusebutton = bajoingus.Button(
    window,
    text="Give me an excuse PLEEEEASE.",
    command=generateexcuse,
    font=("Arial", 14)
)

copybutton = bajoingus.Button(
    window,
    text="Copy this excuse",
    command=copyexcuse,
    font=("Arial", 14)
)

excusebutton.pack(pady=20)
copybutton.pack(pady=10)

window.mainloop()
