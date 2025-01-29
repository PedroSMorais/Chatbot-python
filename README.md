# Chatbot Simples em Python

Um chatbot simples desenvolvido em Python usando a biblioteca NLTK (Natural Language Toolkit). Este chatbot é capaz de responder a saudações básicas e manter uma conversa simples.

## Funcionalidades

- Responde a saudações como "oi", "olá", "hello" e "hey".
- Identifica perguntas sobre o seu nome ou identidade.
- Encerra a conversa quando o usuário digita "sair".
- Responde a mensagens desconhecidas com uma mensagem padrão.

## Como Usar

### Pré-requisitos

1. **Python 3.x**: Certifique-se de ter o Python instalado. Você pode verificar a instalação com o comando:
           python --version
2. NLTK: Instale a biblioteca NLTK usando o pip:  
           pip install nltk
3. Baixar Dados do NLTK: O NLTK requer alguns dados adicionais. Execute o seguinte código Python para baixá-los:
           import nltk
           nltk.download('punkt')
Executando o Chatbot
a) Clone este repositório: 

git clone [https://github.com/PedroSMorais/Chatbot-python.git]

b) Execute o script chatbot.py:
            python chatbot.py

c) Interaja com o chatbot digitando mensagens. Para sair, digite sair.

Estrutura do Código
chatbot.py: Contém a lógica do chatbot, incluindo padrões de respostas e a função principal para iniciar a conversa.

README.md: Este arquivo, com instruções sobre o projeto.

Padrões de Resposta
O chatbot usa uma lista de padrões (pairs) para mapear entradas do usuário a respostas predefinidas. Exemplos de padrões incluem:

Saudações: Responde a "oi", "olá", "hello", etc.

Identificação: Responde a perguntas como "qual o seu nome?".

Despedida: Encerra a conversa quando o usuário digita "sair".

Padrão genérico: Responde a mensagens desconhecidas com "Desculpe, não entendi."


Contribuições são bem-vindas! Siga os passos abaixo:

Faça um fork do repositório.

Crie uma branch para sua feature (git checkout -b feature/nova-feature).

Faça commit das suas alterações (git commit -m 'Adicionando nova feature').

Faça push para a branch (git push origin feature/nova-feature).

Abra um Pull Request.

Divirta-se conversando com o chatbot! 😊
