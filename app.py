import streamlit as st
import requests
import openai


def generate_message(prompt: str):
    openai.api_key = st.secrets["OPENAI_API_KEY"]

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt = prompt,
        temperature=0.7,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    message = response.choices and response.choices[0] and response.choices[0].text.strip();
    st.text(message)

st.title("Card Genie")
occasion = st.text_input("What is the occasion?", placeholder="birthday", max_chars=50)
recipient = st.text_input("Who is the card for?", placeholder="neighbor", max_chars=50)
tone = st.text_input("What tone would you like the card to take?", value="friendly", max_chars=120)
personal_message = st.text_input("Add a personal detail if you'd like it to be incorporated in the card message", 
    placeholder="thanks for helping us move in!", max_chars=100)

if st.button("Generate") and occasion != "" and recipient !="":
    with st.spinner("Generating message..."):
        message_prompt = f"You're a professional card writer. Write a {occasion} card for my {recipient}.\
            The card should be {tone}. Don't include any salutations or sign offs. In cases where gender is\
                 ambiguous, use gender neutral terminology."
        if personal_message != "":
            message_prompt += f" Incorporate the following information to make it more personal: {personal_message}."
        generate_message(message_prompt)
        