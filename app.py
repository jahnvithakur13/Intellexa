import streamlit as st
from chatbot import get_ai_response, extract_text_from_file, get_ai_response_with_image

st.set_page_config(page_title="Intellexa", page_icon="🎓", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"]  {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: linear-gradient(160deg, #0a0a0f, #1a0d0d, #0a0a0f);
    color: #f5f5f5;
}

[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"],
#MainMenu,
footer,
.viewerBadge_container__1QSob,
.stDeployButton {
    display: none !important;
    visibility: hidden !important;
}

header[data-testid="stHeader"] {
    background: transparent !important;
    height: 2.5rem !important;
}

[data-testid="collapsedControl"] {
    display: none !important;
}

.block-container {
    padding-top: 1rem;
    padding-bottom: 0rem;
}

[data-testid="stAppViewContainer"] > .main {
    margin-left: 0 !important;
    width: 100% !important;
    max-width: 100% !important;
}

div[data-testid="stVerticalBlock"]:empty,
div[data-testid="stHorizontalBlock"]:has(> div:empty):not(:has(button)):not(:has(input)) {
    display: none !important;
}

.hero {
    text-align: center;
    padding: 24px 10px 10px 10px;
    position: relative;
    z-index: 1;
}
.hero h1 {
    font-size: 50px;
    font-weight: 800;
    letter-spacing: 6px;
    color: #ffffff;
    margin-bottom: 0px;
}
.hero .subtitle {
    color: #ff3c3c;
    font-weight: 700;
    font-size: 16px;
    letter-spacing: 3px;
    margin-top: 6px;
}
.hero .desc {
    color: #b3b3b3;
    font-size: 15px;
    margin-top: 10px;
    line-height: 1.6;
}

.main-card {
    background: transparent;
    border: none;
    border-radius: 0;
    padding: 10px;
    max-width: 800px;
    width: 100%;
    margin: 0 auto;
    position: relative;
    z-index: 1;
    box-shadow: none;
    max-height: none;
    overflow: visible;
}

.welcome-row {
    display: flex;
    align-items: flex-start;
    gap: 16px;
    margin-bottom: 20px;
}
.welcome-icon {
    width: 50px;
    height: 50px;
    border: 2px solid #ff3c3c;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    background: #0a0a0f;
    box-shadow: 0px 0px 15px rgba(255, 60, 60, 0.4);
    flex-shrink: 0;
}
.welcome-text h3 {
    color: #ff3c3c;
    margin: 0px;
    font-size: 20px;
}
.welcome-text p {
    color: #d7d7e0;
    margin-top: 6px;
    font-size: 14px;
    line-height: 1.6;
}

.chat-bubble-user {
    background: linear-gradient(135deg, rgba(0, 188, 212, 0.85), rgba(30, 30, 60, 0.85));
    color: white;
    padding: 12px 18px;
    border-radius: 18px 18px 4px 18px;
    margin: 8px 0px;
    max-width: 75%;
    margin-left: auto;
    font-size: 15px;
    word-wrap: break-word;
}
.chat-bubble-bot {
    background: rgba(255, 255, 255, 0.06);
    color: #f1f1f1;
    padding: 12px 18px;
    border-radius: 18px 18px 18px 4px;
    margin: 8px 0px;
    max-width: 75%;
    border: 1px solid rgba(255, 80, 80, 0.18);
    font-size: 15px;
    word-wrap: break-word;
}
.chat-row {
    display: flex;
    align-items: flex-end;
    gap: 8px;
}
.avatar {
    width: 34px;
    height: 34px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 17px;
    flex-shrink: 0;
}
.avatar-user { background: linear-gradient(135deg, #00bcd4, #1a1a2e); }
.avatar-bot { background: linear-gradient(135deg, #ff3c3c, #ff8c00); }

div[data-testid="stForm"] {
    background: transparent !important;
    padding: 0 !important;
    border-radius: 0 !important;
    border: none !important;
    box-shadow: none !important;
}
.stTextInput input {
    background-color: transparent !important;
    color: white !important;
    border: none !important;
}
div[data-testid="stForm"] .stButton button, button[kind="formSubmit"] {
    background: #ff3c3c !important;
    color: white !important;
    border: none !important;
    border-radius: 50% !important;
    width: 48px !important;
    height: 48px !important;
    font-weight: 700 !important;
}

.top-nav-row .stButton button,
.top-nav-row [data-testid="stExpander"] summary {
    background: rgba(255,255,255,0.05) !important;
    color: #d7d7e0 !important;
    border: 1px solid rgba(255, 80, 80, 0.18) !important;
    border-radius: 10px !important;
    font-size: 13px !important;
    font-weight: 500 !important;
    padding: 8px 14px !important;
    width: 100% !important;
}
.top-nav-row .stButton button:hover {
    border: 1px solid #ff3c3c !important;
    color: #ffffff !important;
}
.top-nav-row [data-testid="stExpander"] {
    background: transparent !important;
    border: none !important;
}
.top-nav-row [data-testid="stExpander"] summary {
    display: flex;
    align-items: center;
}

[data-testid="stPopover"] button {
    background: rgba(255,255,255,0.08) !important;
    color: white !important;
    border-radius: 50% !important;
    width: 44px !important;
    height: 44px !important;
    font-size: 18px !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
}

.speak-btn {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255, 80, 80, 0.25);
    color: #ff8c8c;
    border-radius: 50%;
    width: 30px;
    height: 30px;
    min-width: 30px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 14px;
    cursor: pointer;
    flex-shrink: 0;
    align-self: flex-end;
}
.speak-btn:hover {
    background: #ff3c3c;
    color: white;
}

.fixed-footer {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    text-align: center;
    padding: 8px 10px 14px 10px;
    background: linear-gradient(180deg, rgba(10,10,15,0) 0%, rgba(10,10,15,0.85) 35%, rgba(10,10,15,0.97) 100%);
    z-index: 999;
    pointer-events: none;
}
.fixed-footer .disclaimer {
    color: #888;
    font-size: 12px;
    margin: 0 0 8px 0;
}
.fixed-footer .flame {
    width: 36px;
    height: 36px;
    border: 2px solid #ff3c3c;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    margin: 0 auto 6px auto;
    background: #0a0a0f;
    box-shadow: 0px 0px 15px rgba(255, 60, 60, 0.4);
}
.fixed-footer .tag {
    color: #aaa;
    font-size: 11px;
    letter-spacing: 3px;
    margin: 0;
}

.bottom-spacer {
    height: 160px;
}

.input-row-wrapper {
    margin-bottom: 10px;
}

.chat-scroll-area {
    max-height: 55vh;
    overflow-y: auto;
    padding-right: 6px;
    margin-bottom: 10px;
}
.chat-scroll-area::-webkit-scrollbar {
    width: 6px;
}
.chat-scroll-area::-webkit-scrollbar-thumb {
    background: rgba(255, 60, 60, 0.4);
    border-radius: 10px;
}
.chat-scroll-area::-webkit-scrollbar-track {
    background: transparent;
}


@media (max-width: 768px) {
    .stApp { height: auto; overflow: auto; }
    .hero h1 { font-size: 32px; letter-spacing: 3px; }
    .hero .subtitle { font-size: 12px; letter-spacing: 2px; }
    .hero .desc { font-size: 13px; }
    .main-card { padding: 16px; margin: 10px; max-height: none; overflow-y: visible; }
    .chat-bubble-user, .chat-bubble-bot { max-width: 90%; font-size: 14px; }
    .welcome-text h3 { font-size: 17px; }
}

.hero {
    text-align: center;
    margin-top: 20px;
}

.hero-icon {
    font-size: 50px;
    margin-bottom: 15px;
    display: flex;
    justify-content: center;
    align-items: center;

    width: 80px;
    height: 80px;
    margin-left: auto;
    margin-right: auto;

    border: 2px solid #ff3b3b;
    border-radius: 50%;
    box-shadow: 0 0 15px #ff3b3b;
    transform: translateX(-15px);
}
</style>
""", unsafe_allow_html=True)

def js_escape(text):
    return (
        text.replace("\\", "\\\\")
            .replace("'", "\\'")
            .replace('"', '\\"')
            .replace("\n", " ")
            .replace("\r", " ")
    )


if "messages" not in st.session_state:
    st.session_state.messages = []
if "page" not in st.session_state:
    st.session_state.page = "Chat"
if "past_chats" not in st.session_state:
    st.session_state.past_chats = []

col_nav1, col_nav2, col_nav3, col_nav4 = st.columns([1, 1, 1, 2])

with col_nav1:
    if st.button("💬 Chat", key="nav_Chat"):
        st.session_state.page = "Chat"
        st.rerun()

with col_nav2:
    if st.button("📝 Quick Notes", key="nav_QuickNotes"):
        st.session_state.page = "Quick Notes"
        st.rerun()

with col_nav3:
    if st.button("➕ New Chat"):
        if st.session_state.messages:
            first_user_msg = next(
                (m["content"] for m in st.session_state.messages if m["role"] == "user"),
                "Conversation"
            )
            st.session_state.past_chats.append({
                "preview": first_user_msg,
                "messages": st.session_state.messages
            })
        st.session_state.messages = []
        st.session_state.page = "Chat"
        st.rerun()

with col_nav4:
    with st.expander("🕓 Recent Chats"):
        if not st.session_state.past_chats:
            st.caption("No past chats yet.")
        else:
            for idx, chat in enumerate(reversed(st.session_state.past_chats[-10:])):
                preview = chat["preview"]
                preview = preview if len(preview) <= 30 else preview[:30] + "..."
                real_idx = len(st.session_state.past_chats) - 1 - idx
                if st.button(preview, key=f"history_{real_idx}"):
                    if st.session_state.messages:
                        first_user_msg = next(
                            (m["content"] for m in st.session_state.messages if m["role"] == "user"),
                            "Conversation"
                        )
                        st.session_state.past_chats.append({
                            "preview": first_user_msg,
                            "messages": st.session_state.messages
                        })
                    st.session_state.messages = st.session_state.past_chats[real_idx]["messages"]
                    st.session_state.page = "Chat"
                    st.rerun()

        if st.button("🗑️ Delete All History"):
            st.session_state.past_chats = []
            st.session_state.messages = []
            st.success("History cleared!")
            st.rerun()

st.markdown("""
<div class='hero'>
    <div class='hero-icon'>🔥</div>
    <h1>INTELLEXA</h1>
    <p class='subtitle'>YOUR STUDY COMPANION</p>
</div>
""", unsafe_allow_html=True)

if st.session_state.page == "Chat":

    st.markdown("<div class='main-card'>", unsafe_allow_html=True)

    if not st.session_state.messages:
        st.markdown("""
        <div class='welcome-row'>
            <div class='welcome-icon'>🔥</div>
            <div class='welcome-text'>
                <h3>👋 Hello, I'm Intellexa!</h3>
                <p>Ask your academic questions here and I'll provide clear and simple answers.<br>
                I specialize in <strong>education, careers, job opportunities, and industry trends</strong>.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    chat_html = "<div class='chat-scroll-area'>"
    for msg in st.session_state.messages:
        content_html = msg['content'].replace("\r\n", "\n").replace("\n", "<br>")
        if msg["role"] == "user":
            chat_html += (
                "<div class='chat-row' style='justify-content: flex-end;'>"
                f"<div class='chat-bubble-user'>{content_html}</div>"
                "<div class='avatar avatar-user'>🧑</div>"
                "</div>"
            )
        else:
            chat_html += (
                "<div class='chat-row'>"
                "<div class='avatar avatar-bot'>🔥</div>"
                f"<div class='chat-bubble-bot'>{content_html}</div>"
                "</div>"
            )

    chat_html += "</div>"
    st.markdown(chat_html, unsafe_allow_html=True)


    st.markdown("<div class='input-row-wrapper'>", unsafe_allow_html=True)
    col_upload, col_form = st.columns([0.7, 6], gap="small")

    with col_upload:
        with st.popover("📎"):
            uploaded_file = st.file_uploader(
                "Upload an image or document",
                type=["png", "jpg", "jpeg", "pdf", "docx", "txt"],
                label_visibility="collapsed"
            )
            if uploaded_file is not None:
                st.caption(f"📎 {uploaded_file.name}")

    with col_form:
        with st.form(key="chat_form", clear_on_submit=True):
            c1, c2 = st.columns([6, 1])
            with c1:
                user_input = st.text_input("Message", label_visibility="collapsed", placeholder="Type your question here...")
            with c2:
                submitted = st.form_submit_button("➤")
    st.markdown("</div>", unsafe_allow_html=True)

    if submitted and (user_input.strip() or uploaded_file is not None):
        display_text = user_input if user_input.strip() else "[Uploaded a file]"
        st.session_state.messages.append({"role": "user", "content": display_text})

        if uploaded_file is not None:
            file_type = uploaded_file.type
            if file_type in ["image/png", "image/jpeg", "image/jpg"]:
                image_bytes = uploaded_file.read()
                response = get_ai_response_with_image(user_input, image_bytes)
            else:
                extracted_text = extract_text_from_file(uploaded_file)
                if extracted_text:
                    combined_prompt = f"Here is the content of a document:\n\n{extracted_text}\n\nUser question: {user_input or 'Summarize and explain this document.'}"
                    recent_history = st.session_state.messages[-10:-1]
                    response = get_ai_response(combined_prompt, recent_history)
                else:
                    response = "Sorry, I couldn't read that file format."
        else:
            recent_history = st.session_state.messages[-10:-1]
            response = get_ai_response(user_input, recent_history)

        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()

    st.markdown("<div class='bottom-spacer'></div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.page == "Quick Notes":
    st.markdown("<div class='main-card'>", unsafe_allow_html=True)
    st.markdown("""
    <div class='welcome-row'>
        <div class='welcome-icon'>📝</div>
        <div class='welcome-text'>
            <h3>Quick Notes</h3>
            <p>Note down anything you want to remember — saved for this session.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    if "quick_notes" not in st.session_state:
        st.session_state.quick_notes = ""

    st.session_state.quick_notes = st.text_area(
        "Notes",
        value=st.session_state.quick_notes,
        height=250,
        label_visibility="collapsed",
        placeholder="Type your notes here..."
    )

    st.markdown("<div class='bottom-spacer'></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("""
<div class='fixed-footer'>
    <p class='disclaimer'>Intellexa only answers questions about education, careers, jobs, and industry trends.</p>
    <p class='tag'>◆ KNOWLEDGE IS POWER ◆</p>
</div>
""", unsafe_allow_html=True)