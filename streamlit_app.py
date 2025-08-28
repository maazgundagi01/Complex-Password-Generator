import streamlit as st
import random

# Configure the page
st.set_page_config(
    page_title="PyPassword Generator",
    page_icon="🔐",
    layout="centered"
)

# Title and header
st.title("🔐 PyPassword Generator")
st.markdown("### Generate secure passwords with custom requirements!")

# Character sets (keeping your original logic)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Create columns for better layout
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🔤 Letters")
    nr_letters = st.number_input(
        "How many letters?",
        min_value=0,
        max_value=50,
        value=8,
        step=1
    )

with col2:
    st.markdown("### 🔢 Numbers")
    nr_numbers = st.number_input(
        "How many numbers?",
        min_value=0,
        max_value=50,
        value=2,
        step=1
    )

with col3:
    st.markdown("### 🎯 Symbols")
    nr_symbols = st.number_input(
        "How many symbols?",
        min_value=0,
        max_value=50,
        value=2,
        step=1
    )

# Generate password button
if st.button("🚀 Generate Password", type="primary", use_container_width=True):
    if nr_letters == 0 and nr_numbers == 0 and nr_symbols == 0:
        st.error("❌ Please select at least one character type!")
    else:
        # Your original logic for password generation
        letters_picked = []
        numbers_picked = []
        symbols_picked = []

        # Note: Fixed the bug in your original code where random.randint(0,len(letters))
        # could cause IndexError. Should be random.randint(0,len(letters)-1)
        for number in range(0, nr_letters):
            random_index = random.randint(0, len(letters) - 1)
            letter_pick = letters[random_index]
            letters_picked.append(letter_pick)

        for number in range(0, nr_numbers):
            random_index = random.randint(0, len(numbers) - 1)
            number_pick = numbers[random_index]
            numbers_picked.append(number_pick)

        for number in range(0, nr_symbols):
            random_index = random.randint(0, len(symbols) - 1)
            symbol_pick = symbols[random_index]
            symbols_picked.append(symbol_pick)

        password = letters_picked + numbers_picked + symbols_picked
        random.shuffle(password)
        generated_password = "".join(password)

        # Display the generated password
        st.success("🎉 Password Generated Successfully!")
        st.markdown("### Your randomized password:")

        # Create a copy-friendly text area
        st.code(generated_password, language=None)

        # Password strength indicator
        password_length = len(generated_password)
        if password_length < 8:
            strength = "🔴 Weak"
        elif password_length < 12:
            strength = "🟡 Medium"
        else:
            strength = "🟢 Strong"

        st.info(f"Password Length: {password_length} characters | Strength: {strength}")

# Add some helpful information
with st.expander("ℹ️ Password Security Tips"):
    st.markdown("""
    - **🔒 Use unique passwords** for each account
    - **📏 Longer passwords** are generally more secure
    - **🔄 Mix different character types** for better security
    - **🚫 Avoid personal information** in passwords
    - **💾 Use a password manager** to store passwords safely
    """)

# Footer
st.markdown("---")
st.markdown("*Built with ❤️ by Maaz Gundagi*")