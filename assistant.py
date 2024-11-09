import streamlit as st
from langchain_community.llms import Ollama

# Initialize the LLaMA model
llm = Ollama(model="llama3.1")

# Set page config
st.set_page_config(
    page_title="One-Day Tour Planner",
    page_icon="✴️",
    layout="centered"
)

# Predefined credentials (for simplicity)
USERNAME = "user123"
PASSWORD = "password123"

# Function to call Ollama with the prompt and conversation history
def call_ollama(prompt, conversation_history):
    # Combine conversation history into a single text input for context
    full_prompt = "\n".join([f"{user}: {message}" for user, message in conversation_history]) + f"\nUser: {prompt}"
    # Generate a response with Ollama
    response = llm(full_prompt)
    return response

# Helper to display chat history
def display_chat():
    for entry in st.session_state.conversation_history:
        user, message = entry
        st.write(f"**{user}**: {message}")

# Sidebar content
with st.sidebar:
    st.image(r"/Users/saranshtiwari/Documents/Placement Preperation/attention ai/logo.png", use_column_width=True)
    st.title('Tour Planner 💬')
    st.write('© Saransh Tiwari')

    # Reset button to clear conversation and logout user
    if st.button("Reset Conversation"):
        st.session_state.conversation_history.clear()
        st.session_state.user_preferences.clear()
        st.session_state.logged_in = False  # Reset login status
        st.write("Conversation reset! Please log in again.")

# Initialize session state for chat history, preferences, and login status
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []
if "user_preferences" not in st.session_state:
    st.session_state.user_preferences = []
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Login check function
def check_login():
    if not st.session_state.logged_in:
        # Login form
        st.title("User Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        if st.button("Login"):
            if username == USERNAME and password == PASSWORD:
                st.session_state.logged_in = True
                st.success("Logged in successfully!")
                check_login()
            else:
                st.error("Invalid credentials, please try again.")
    else:
        # Show chatbot functionality if logged in
        st.title("Tour Planner 💬")
        # Display chat interface
        display_chat()

        # Input field for user questions
        user_input = st.text_input("User:", placeholder="Type your message here...")

        if user_input:
            st.session_state.conversation_history.append(("User", user_input))
            
            # Collect user preferences
            if "city" not in st.session_state.user_preferences:
                if "city" in user_input.lower():
                    st.session_state.user_preferences["city"] = user_input.split("in ")[-1]
            if "budget" not in st.session_state.user_preferences:
                if "$" in user_input:
                    st.session_state.user_preferences["budget"] = int("".join([c for c in user_input if c.isdigit()]))
            if "interest" not in st.session_state.user_preferences:
                if any(interest in user_input.lower() for interest in ["historical", "food", "shopping"]):
                    st.session_state.user_preferences["interest"] = user_input.lower()

            # Generate response with LLM
            prompt = f"User preferences: {st.session_state.user_preferences}. User said: {user_input}"
            response = call_ollama(prompt, st.session_state.conversation_history)
            st.session_state.conversation_history.append(("Assistant", response))
            st.write(f" 🤖 **Assistant**: {response}")

# Display login or chatbot based on session state
check_login()