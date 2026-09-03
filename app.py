import streamlit as st


st.set_page_config(
    page_title="Highly Confidential",
    page_icon="🕵️",
    layout="centered",
)

st.title("🕵️ Highly Confidential")
st.caption("A competitive Cold War investigation game")

st.markdown(
    """
    ### Operation Cold Turkey

    **Berlin, 1978.**

    During a diplomatic reception at Hotel Europa, a microfilm containing
    the identity of a valuable informant disappeared from a locked pouch.

    At 22:17, the hotel suffered a six-minute blackout.

    Five suspects were present. Everyone has an explanation.
    Most of the explanations are terrible.
    """
)

agent_name = st.text_input(
    "Agent codename",
    placeholder="For example: Agent Badger",
)

if st.button(
    "Open classified file",
    type="primary",
    use_container_width=True,
):
    if agent_name.strip():
        st.success(f"Clearance confirmed. Welcome, {agent_name.strip()}.")
    else:
        st.warning("Enter your agent codename first.")
