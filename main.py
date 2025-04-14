import streamlit as st

# Set basic config
st.set_page_config(page_title="Simple Calculator", layout="centered")
st.title("🧮 Simple Calculator")

# Expression state
if "expression" not in st.session_state:
    st.session_state.expression = ""

# Handle button press
def press(key):
    if key == "=":
        try:
            result = str(eval(st.session_state.expression.replace("x", "*")))
            st.session_state.expression = result
        except:
            st.session_state.expression = "Error"
    elif key == "C":
        st.session_state.expression = ""
    else:
        st.session_state.expression += key

# Display input box for typing (optional)
st.text_input("Expression", value=st.session_state.expression, key="input", label_visibility="collapsed")

# Layout for buttons (like mobile layout)
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "x"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
]

# Render buttons row by row
for row in buttons:
    cols = st.columns(4)
    for i, key in enumerate(row):
        if cols[i].button(key, use_container_width=True):
            press(key)

# Clear button
st.markdown("###")
st.button("Clear", on_click=lambda: press("C"), use_container_width=True)
