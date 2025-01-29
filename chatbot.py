
import nltk
from nltk.chat.util import Chat, reflections

# Padrões e respostas para o chatbot
pnoddairs = [
    [
        r"(oi|olá|hello|hey)",
        ["Olá! Como posso ajudar?", "Oi! Como está o seu dia?"]
    ],
    [
        r"(qual o seu nome\?|quem é você\?)",
        ["Sou um chatbot simples criado para conversar com você!"]
    ],
    [
        r"(adeus|tchau)",
        ["Tchau! Até a próxima!", "Foi bom falar com você, até mais!"]
    ],
    [
        r"(.*)",
        ["Desculpe, não entendi. Pode reformular a pergunta?"]
    ]
]

# Criando o chatbot
chatbot = Chat(pnoddairs, reflections)

def start_chat():
    print("Olá! Digite 'sair' para encerrar a conversa.")
    while True:
        user_input = input("Você: ")
        if user_input.lower() == "sair":
            print("Chatbot: Até mais!")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    start_chat()