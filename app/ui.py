import streamlit as st

from app.llm_client import generate_response
from app.validators import validate_response


st.set_page_config(
    page_title="AI Customer Support",
    page_icon="🤖",
    layout="centered"
)


# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("🤖 AI Customer Support Assistant")

st.write(
    "Welcome! I can help you with orders, returns, refunds, "
    "payments, delivery, and product questions."
)


# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.header("⚙️ Chat Controls")

    st.write(
        "Use the controls below to manage your conversation."
    )

    if st.button(
        "🗑️ Clear Chat",
        use_container_width=True
    ):

        st.session_state.messages = []

        st.rerun()

    st.divider()

    st.subheader("🛡️ AI Safety")

    st.write("Response validation is enabled.")

    st.write(
        "The assistant checks responses for "
        "basic sensitive-information leakage."
    )

    st.divider()

    st.caption(
        "AI Customer Support Chatbot"
    )

    st.caption(
        "Gemini API • Langfuse • Streamlit"
    )


st.divider()


# --------------------------------------------------
# Conversation Memory
# --------------------------------------------------

if "messages" not in st.session_state:

    st.session_state.messages = []


# --------------------------------------------------
# Display Conversation
# --------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# --------------------------------------------------
# Customer Input
# --------------------------------------------------

user_input = st.chat_input(
    "Type your customer support question..."
)


if user_input:

    # ----------------------------------------------
    # Display Customer Message
    # ----------------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):

        st.markdown(user_input)


    # ----------------------------------------------
    # Generate AI Response
    # ----------------------------------------------

    with st.chat_message("assistant"):

        with st.spinner("AI is thinking..."):

            result = generate_response(
                user_input
            )


        # ------------------------------------------
        # API Failure Handling
        # ------------------------------------------

        if not result["success"]:

            assistant_response = result["response"]

            st.error(
                f"System Status: {result['status']}"
            )


        # ------------------------------------------
        # Successful AI Response
        # ------------------------------------------

        else:

            assistant_response = result["response"]


            # --------------------------------------
            # Response Validation
            # --------------------------------------

            validation = validate_response(
                assistant_response
            )


            if validation["valid"]:

                st.success(
                    "✅ Response validation: PASSED"
                )

            else:

                st.warning(
                    "⚠️ Response validation: FAILED"
                )

                st.warning(
                    validation["reason"]
                )


        # ------------------------------------------
        # Display AI Response
        # ------------------------------------------

        st.markdown(
            assistant_response
        )


    # ----------------------------------------------
    # Save AI Response
    # ----------------------------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": assistant_response
        }
    )