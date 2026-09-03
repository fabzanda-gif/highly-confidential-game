import random
import string

import streamlit as st


st.set_page_config(
    page_title="Highly Confidential",
    page_icon="🕵️",
    layout="centered",
    initial_sidebar_state="collapsed",
)


def initialize_state():
    defaults = {
        "screen": "home",
        "agent_name": "",
        "match_code": "",
        "match_role": "",
        "opponent_name": None,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def generate_match_code():
    alphabet = string.ascii_uppercase + string.digits
    return "".join(random.choices(alphabet, k=6))


def go_to(screen):
    st.session_state.screen = screen
    st.rerun()


def reset_prototype():
    for key in (
        "screen",
        "agent_name",
        "match_code",
        "match_role",
        "opponent_name",
    ):
        st.session_state.pop(key, None)
    st.rerun()


def render_header():
    st.title("🕵️ Highly Confidential")
    st.caption("A competitive Cold War investigation game")


def render_home():
    render_header()

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

    st.divider()

    with st.form("agent_clearance"):
        agent_name = st.text_input(
            "Agent codename",
            value=st.session_state.agent_name,
            placeholder="For example: Agent Badger",
            max_chars=30,
        )
        submitted = st.form_submit_button(
            "Open classified file",
            type="primary",
            use_container_width=True,
        )

    if submitted:
        clean_name = agent_name.strip()
        if not clean_name:
            st.warning("Enter your agent codename first.")
        else:
            st.session_state.agent_name = clean_name
            go_to("match_options")


def render_match_options():
    render_header()
    st.success(f"Clearance confirmed. Welcome, {st.session_state.agent_name}.")

    st.markdown("### Choose your assignment")
    st.write(
        "Create a new investigation or enter the code sent by the other agent."
    )

    if st.button(
        "Create a new match",
        type="primary",
        use_container_width=True,
    ):
        st.session_state.match_code = generate_match_code()
        st.session_state.match_role = "host"
        st.session_state.opponent_name = None
        go_to("lobby")

    st.markdown("#### Join an existing match")

    with st.form("join_match"):
        match_code = st.text_input(
            "Six-character match code",
            placeholder="Example: C0LD78",
            max_chars=6,
        ).upper()
        join_submitted = st.form_submit_button(
            "Join match",
            use_container_width=True,
        )

    if join_submitted:
        clean_code = match_code.strip()
        if len(clean_code) != 6 or not clean_code.isalnum():
            st.warning("Enter a valid six-character match code.")
        else:
            st.session_state.match_code = clean_code
            st.session_state.match_role = "guest"
            st.session_state.opponent_name = "Agent Nightingale"
            go_to("lobby")

    if st.button("← Change codename", use_container_width=True):
        go_to("home")


def render_lobby():
    render_header()

    st.markdown("### Secure operations room")
    st.metric("Match code", st.session_state.match_code)
    st.caption("Send this code to the second player.")

    st.markdown("#### Assigned agents")
    st.write(f"✅ **{st.session_state.agent_name}** — connected")

    if st.session_state.opponent_name:
        st.write(f"✅ **{st.session_state.opponent_name}** — connected")
    else:
        st.write("⏳ **Second agent** — awaiting clearance")

    st.info(
        "This version is a local interface prototype. The Supabase integration "
        "will make match codes and waiting rooms work between two devices."
    )

    if not st.session_state.opponent_name:
        if st.button(
            "Simulate second agent",
            use_container_width=True,
            help="Temporary testing control for the prototype.",
        ):
            st.session_state.opponent_name = "Agent Nightingale"
            st.rerun()

    if st.button(
        "Begin case briefing",
        type="primary",
        use_container_width=True,
        disabled=not bool(st.session_state.opponent_name),
    ):
        go_to("briefing")

    if st.button("Leave operations room", use_container_width=True):
        go_to("match_options")


def render_briefing():
    render_header()

    st.caption(f"CASE 001 · MATCH {st.session_state.match_code}")
    st.markdown("## Operation Cold Turkey")
    st.markdown(
        """
        **Hotel Europa, West Berlin — 22:36**

        Six minutes ago, the lights returned after an unexplained blackout.
        A diplomatic pouch remained locked, sealed and apparently untouched.

        The microfilm inside it did not share that good fortune.

        Your mission is to determine:

        - who took the microfilm;
        - how it was removed;
        - when the theft occurred;
        - where it is hidden;
        - and why it was stolen.

        You and the other investigator may exchange intelligence, but only one
        agent will receive the commendation.
        """
    )

    st.warning(
        "Prototype checkpoint reached. Suspects, Action Points and evidence "
        "will be introduced in the next version."
    )

    if st.button(
        "Acknowledge briefing",
        type="primary",
        use_container_width=True,
    ):
        st.toast("Briefing acknowledged. Awaiting case file authorisation.")

    if st.button("Restart prototype", use_container_width=True):
        reset_prototype()


initialize_state()

if st.session_state.screen == "home":
    render_home()
elif st.session_state.screen == "match_options":
    render_match_options()
elif st.session_state.screen == "lobby":
    render_lobby()
elif st.session_state.screen == "briefing":
    render_briefing()
else:
    reset_prototype()
