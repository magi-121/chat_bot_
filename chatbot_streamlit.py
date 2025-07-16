import streamlit as st
import random
import difflib

name = "aura-inifix"

response = {
    "hi": [
        "Hello! This is aura-inifix. How can I help you?",
        "Hi there! How can I assist you today?",
        "Hey! What can I do for you?"
    ],
    "bye": [
        "Goodbye!",
        "See you later!",
        "Take care!"
    ],
    "thanks": [
        "You are welcome!",
        "No problem!",
        "Anytime!"
    ],
    "how are you": [
        "I am fine, thank you!",
        "Doing great! How about you?"
    ],
    "what is your name": [
        "My name is aura-inifix.",
        "I'm called aura-inifix."
    ],
    "what is your gender": [
        "I am a bot.",
        "Bots don't have genders!"
    ],
    "can you generate some jokes": [
        "Sure. Why did the computer go to the doctor 🧑‍⚕️? It had a virus 😂😅 ",
        "Why do programmers prefer dark mode 🌑? Because light attracts bugs🐞!"
    ],
    "what is the weather in your city": [
        "It is sunny in my city.",
        "Looks like a perfect day here!"
    ],
    "the best way to learn python": [
        "The best way to learn Python is to practice it.",
        "Keep coding and you'll get better at Python!"
    ],
    "say about yourself": [
        "I am a bot created by aura-inifix. I am here to help you.",
        "I'm your friendly chatbot, always ready to assist!"
    ],
    "who created you": [
        "I was created by Mr.Magi.",
        "My creator is magi, who loves building ai models and building dashboards!"
    ],
    "what can you do": [
        "I can answer your questions, tell jokes, and chat with you!",
        "I'm here to help, entertain, and provide information."
    ],
    "tell me a fun fact": [
        "Did you know? Honey never spoils. Archaeologists have found edible honey in ancient Egyptian tombs!",
        "Fun fact: A group of flamingos is called a 'flamboyance'!"
    ],
    "what is python": [
        "Python is a popular programming language known for its simplicity and versatility.",
        "Python is widely used for web development, data analysis, AI, and more."
    ],
    "how old are you": [
        "I'm as old as my code! I don't age like humans.",
        "Bots like me don't have an age, but I'm always up to date!"
    ],
    "can you help me with coding": [
        "Absolutely! Ask me any coding question you have.",
        "Sure! What programming problem are you facing?"
    ],
    "what is ai": [
        "AI stands for Artificial Intelligence, which enables machines to mimic human intelligence.",
        "Artificial Intelligence is the simulation of human intelligence by computers."
    ],
    "do you have feelings": [
        "I don't have feelings, but I'm here to help you with yours!",
        "I'm just a bot, so I don't experience emotions."
    ],
    "what's your favorite color": [
        "I like all colors equally, but green looks good on me!",
        "As a bot, I don't have preferences, but I think blue is cool."
    ],
    "can you sing a song": [
        "I can't sing, but here's a line: 🎵 Never gonna give you up, never gonna let you down... 🎵",
        "I'm not a singer, but I can share song lyrics if you want!"
    ],
    "generate the python code ":[
        "sure, i can generate the python code for you. but i need to know what you want to do."
    ],
    "code for area of circle":['''
    import math 
    radius = 5 
    area = math.pi * radius**2 
    print(area)'''
    ],
    "code for fibonacci series":[
    '''
        def fibonacci(n):   
            fib_list = [0,1]/n   
            for i in range(2,n):
                fib_list.append(fib_list[i-1] + fib_list[i-2])
                return fib_list
    '''],
    "code for factorial of a number":['''
    fact=5
    i=1
    while i<=fact:
        print(i,"*",end=" ")
        i=i+1
    '''],



}

def bot_response(user_input):
    user_input = user_input.strip().lower()
    possible_questions = list(response.keys())
    match = difflib.get_close_matches(user_input, possible_questions)
    if match:
        return random.choice(response[match[0]])
    else:
        return "I'm sorry, I can't understand you."

st.set_page_config(page_title="Aura-Inifix Chatbot", page_icon="🤖")
st.title("Aura-Inifix Chatbot 🤖")

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Michroma&display=swap');
    html, body, [class*="css"]  {
        font-family: 'Michroma', monospace !important;
    }

    .stTextInput > div > div > input {
        font-family: 'Michroma', monospace !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = [
        ("aura-inifix", "Hello! I am aura-inifix. Type 'bye' to end the chat.")
    ]


for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"<div class='chat-message' style='text-align: right; color: #1a73e8;'><b>{sender}:</b> {message}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat-message' style='text-align: left; color: #34a853;'><b>{sender}:</b> {message}</div>", unsafe_allow_html=True)


with st.container():
    user_input = st.text_input("You:", st.session_state.get("input", ""), key="input")
    send = st.button("Send")

    if send and user_input.strip():
        st.session_state.chat_history.append(("You", user_input))
        if user_input.lower() in ["bye", "exit", "quit"]:
            bot_reply = "Goodbye! Have a great day!"
        else:
            bot_reply = bot_response(user_input)
        st.session_state.chat_history.append(("aura-inifix", bot_reply))
        st.rerun() 