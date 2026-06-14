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
    padding-left: 1rem;
    padding-right: 1rem;
}

[data-testid="stAppViewContainer"] > .main {
    margin-left: 0 !important;
    width: 100% !important;
    max-width: 100% !important;
}

/* ===== DRAWER SIDEBAR ===== */
#intellexa-drawer {
    position: fixed;
    top: 0;
    left: -290px;
    width: 270px;
    height: 100vh;
    background: linear-gradient(180deg, #0f0f1a 0%, #130d0d 100%);
    border-right: 1px solid rgba(255, 60, 60, 0.2);
    z-index: 10000;
    transition: left 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    display: flex;
    flex-direction: column;
    overflow-y: auto;
    box-shadow: 4px 0 30px rgba(0,0,0,0.5);
}

#intellexa-drawer.open {
    left: 0;
}

#drawer-overlay {
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(0,0,0,0.6);
    z-index: 9999;
    display: none;
    backdrop-filter: blur(2px);
}

#drawer-overlay.open {
    display: block;
}

.drawer-header {
    padding: 28px 20px 20px 20px;
    border-bottom: 1px solid rgba(255, 60, 60, 0.15);
    display: flex;
    align-items: center;
    gap: 14px;
}

.drawer-logo {
    width: 48px;
    height: 48px;
    border: 2px solid #ff3c3c;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 22px;
    background: #0a0a0f;
    box-shadow: 0 0 18px rgba(255, 60, 60, 0.5);
    flex-shrink: 0;
}

.drawer-brand {
    display: flex;
    flex-direction: column;
}

.drawer-brand-name {
    font-size: 18px;
    font-weight: 800;
    letter-spacing: 3px;
    color: #ffffff;
    line-height: 1.1;
}

.drawer-brand-sub {
    font-size: 10px;
    font-weight: 600;
    color: #ff3c3c;
    letter-spacing: 2px;
    margin-top: 3px;
}

.drawer-close-btn {
    margin-left: auto;
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.1);
    color: #aaa;
    border-radius: 8px;
    width: 32px;
    height: 32px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    font-size: 16px;
    transition: all 0.2s;
}

.drawer-close-btn:hover {
    background: rgba(255, 60, 60, 0.2);
    color: #ff6666;
    border-color: rgba(255,60,60,0.4);
}

.drawer-nav {
    padding: 16px 14px;
    display: flex;
    flex-direction: column;
    gap: 6px;
}

.drawer-nav-btn {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 12px 16px;
    border-radius: 12px;
    border: 1px solid rgba(255,255,255,0.06);
    background: rgba(255,255,255,0.04);
    color: #d7d7e0;
    font-family: 'Poppins', sans-serif;
    font-size: 14px;
    font-weight: 500;
    cursor: pointer;
    text-align: left;
    transition: all 0.2s;
    width: 100%;
}

.drawer-nav-btn:hover,
.drawer-nav-btn.active {
    background: rgba(255, 60, 60, 0.12);
    border-color: rgba(255, 60, 60, 0.35);
    color: #ffffff;
}

.drawer-nav-icon {
    font-size: 18px;
    width: 24px;
    text-align: center;
}

.drawer-divider {
    height: 1px;
    background: rgba(255,255,255,0.07);
    margin: 8px 14px;
}

.drawer-section-label {
    padding: 8px 16px 4px;
    font-size: 10px;
    font-weight: 700;
    color: #555;
    letter-spacing: 2.5px;
    text-transform: uppercase;
}

.drawer-recent-list {
    padding: 0 14px;
    display: flex;
    flex-direction: column;
    gap: 4px;
    flex: 1;
    overflow-y: auto;
}

.drawer-recent-item {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 10px 14px;
    border-radius: 10px;
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.05);
    color: #aaa;
    font-size: 13px;
    cursor: pointer;
    transition: all 0.2s;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    width: 100%;
    text-align: left;
}

.drawer-recent-item:hover {
    background: rgba(255, 60, 60, 0.08);
    border-color: rgba(255, 60, 60, 0.2);
    color: #ddd;
}

.drawer-recent-dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: #ff3c3c;
    flex-shrink: 0;
    opacity: 0.6;
}

.drawer-bottom {
    padding: 14px;
    border-top: 1px solid rgba(255,255,255,0.07);
    margin-top: auto;
}

.drawer-delete-btn {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 10px 14px;
    border-radius: 10px;
    background: rgba(255, 60, 60, 0.06);
    border: 1px solid rgba(255, 60, 60, 0.15);
    color: #ff6666;
    font-family: 'Poppins', sans-serif;
    font-size: 13px;
    font-weight: 500;
    cursor: pointer;
    width: 100%;
    transition: all 0.2s;
}

.drawer-delete-btn:hover {
    background: rgba(255, 60, 60, 0.18);
    border-color: rgba(255, 60, 60, 0.4);
    color: #ff9999;
}

/* Motivational quote box */
.drawer-quote {
    margin: 10px 14px;
    padding: 12px 14px;
    background: rgba(255, 60, 60, 0.05);
    border-left: 3px solid #ff3c3c;
    border-radius: 0 10px 10px 0;
    color: #bbb;
    font-size: 12px;
    font-style: italic;
    line-height: 1.5;
}

.drawer-quote-author {
    color: #ff6666;
    font-size: 11px;
    font-style: normal;
    font-weight: 600;
    margin-top: 4px;
}

/* ===== HAMBURGER BUTTON ===== */
#hamburger-btn {
    position: fixed;
    top: 14px;
    left: 14px;
    z-index: 9998;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255, 60, 60, 0.25);
    border-radius: 12px;
    width: 44px;
    height: 44px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: all 0.2s;
    backdrop-filter: blur(10px);
}

#hamburger-btn:hover {
    background: rgba(255, 60, 60, 0.2);
    border-color: rgba(255, 60, 60, 0.5);
}

.hamburger-lines {
    display: flex;
    flex-direction: column;
    gap: 5px;
}

.hamburger-lines span {
    display: block;
    width: 20px;
    height: 2px;
    background: #ff3c3c;
    border-radius: 2px;
    transition: all 0.3s;
}

/* ===== HERO ===== */
.hero {
    text-align: center;
    padding: 60px 10px 10px 10px;
    position: relative;
    z-index: 1;
}

.hero-icon-wrap {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 0 auto 18px auto;
}

.hero-icon {
    width: 80px;
    height: 80px;
    border: 2px solid #ff3b3b;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 38px;
    background: #0a0a0f;
    box-shadow: 0 0 20px rgba(255, 59, 59, 0.5);
}

.hero h1 {
    font-size: 50px;
    font-weight: 800;
    letter-spacing: 6px;
    color: #ffffff;
    margin: 0 0 6px 0;
    line-height: 1.1;
    text-align: center;
}

.hero .subtitle {
    color: #ff3c3c;
    font-weight: 700;
    font-size: 14px;
    letter-spacing: 4px;
    margin: 0 0 10px 0;
    text-align: center;
}

.hero .desc {
    color: #b3b3b3;
    font-size: 15px;
    margin-top: 10px;
    line-height: 1.6;
}

/* ===== MAIN CARD ===== */
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

/* ===== CHAT BUBBLES ===== */
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

/* ===== FORM ===== */
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

[data-testid="stPopover"] button {
    background: rgba(255,255,255,0.08) !important;
    color: white !important;
    border-radius: 50% !important;
    width: 44px !important;
    height: 44px !important;
    font-size: 18px !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
}

/* ===== FOOTER ===== */
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
    margin: 0 0 4px 0;
}
.fixed-footer .tag {
    color: #aaa;
    font-size: 11px;
    letter-spacing: 3px;
    margin: 0;
}

.bottom-spacer { height: 120px; }

.input-row-wrapper { margin-bottom: 10px; }

.chat-scroll-area {
    max-height: 55vh;
    overflow-y: auto;
    padding-right: 6px;
    margin-bottom: 10px;
}
.chat-scroll-area::-webkit-scrollbar { width: 6px; }
.chat-scroll-area::-webkit-scrollbar-thumb {
    background: rgba(255, 60, 60, 0.4);
    border-radius: 10px;
}
.chat-scroll-area::-webkit-scrollbar-track { background: transparent; }

/* ===== MOBILE ===== */
@media (max-width: 768px) {
    .stApp { height: auto; overflow: auto; }
    .hero { padding-top: 70px; }
    .hero h1 { font-size: 32px; letter-spacing: 3px; }
    .hero .subtitle { font-size: 11px; letter-spacing: 3px; }
    .hero .desc { font-size: 13px; }
    .main-card { padding: 10px; }
    .chat-bubble-user, .chat-bubble-bot { max-width: 90%; font-size: 14px; }
    .welcome-text h3 { font-size: 17px; }
    .hero-icon { width: 64px; height: 64px; font-size: 30px; }
    #intellexa-drawer { width: 260px; }
}
</style>

<!-- DRAWER OVERLAY -->
<div id="drawer-overlay" onclick="closeDrawer()"></div>

<!-- DRAWER SIDEBAR -->
<div id="intellexa-drawer">
    <div class="drawer-header">
        <div class="drawer-logo">🔥</div>
        <div class="drawer-brand">
            <div class="drawer-brand-name">INTELLEXA</div>
            <div class="drawer-brand-sub">AI STUDY ASSISTANT</div>
        </div>
        <button class="drawer-close-btn" onclick="closeDrawer()">✕</button>
    </div>

    <div class="drawer-nav">
        <button class="drawer-nav-btn active" onclick="navTo('Chat')">
            <span class="drawer-nav-icon">💬</span> Chat
        </button>
        <button class="drawer-nav-btn" onclick="navTo('QuickNotes')">
            <span class="drawer-nav-icon">📝</span> Quick Notes
        </button>
        <button class="drawer-nav-btn" onclick="navTo('NewChat')">
            <span class="drawer-nav-icon">➕</span> New Chat
        </button>
    </div>

    <div class="drawer-divider"></div>
    <div class="drawer-section-label">Recent Chats</div>
    <div class="drawer-recent-list" id="recent-chats-list">
        <div style="color:#555; font-size:13px; padding: 8px 14px;">No past chats yet.</div>
    </div>

    <div class="drawer-quote">
        "Push forward, even one step at a time. Every bit of effort sharpens your skills."
        <div class="drawer-quote-author">— Inspired by Demon Slayer</div>
    </div>

    <div class="drawer-bottom">
        <button class="drawer-delete-btn" onclick="navTo('DeleteHistory')">
            🗑️ Delete All History
        </button>
    </div>
</div>

<!-- HAMBURGER BUTTON -->
<div id="hamburger-btn" onclick="openDrawer()">
    <div class="hamburger-lines">
        <span></span><span></span><span></span>
    </div>
</div>

<script>
function openDrawer() {
    document.getElementById('intellexa-drawer').classList.add('open');
    document.getElementById('drawer-overlay').classList.add('open');
}
function closeDrawer() {
    document.getElementById('intellexa-drawer').classList.remove('open');
    document.getElementById('drawer-overlay').classList.remove('open');
}
function navTo(page) {
    closeDrawer();
    // Use Streamlit's query params to communicate page change
    const url = new URL(window.location.href);
    url.searchParams.set('nav', page);
    window.location.href = url.toString();
}
// Keyboard: close on Escape
document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') closeDrawer();
});
</script>
""", unsafe_allow_html=True)


def js_escape(text):
    return (
        text.replace("\\", "\\\\")
            .replace("'", "\\'")
            .replace('"', '\\"')
            .replace("\n", " ")
            .replace("\r", " ")
    )


# Handle navigation via query params
query_params = st.query_params
nav_target = query_params.get("nav", None)

if "messages" not in st.session_state:
    st.session_state.messages = []
if "page" not in st.session_state:
    st.session_state.page = "Chat"
if "past_chats" not in st.session_state:
    st.session_state.past_chats = []

# Process nav from query param
if nav_target:
    if nav_target == "Chat":
        st.session_state.page = "Chat"
    elif nav_target == "QuickNotes":
        st.session_state.page = "Quick Notes"
    elif nav_target == "NewChat":
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
    elif nav_target == "DeleteHistory":
        st.session_state.past_chats = []
        st.session_state.messages = []
        st.session_state.page = "Chat"
    elif nav_target and nav_target.startswith("history_"):
        idx = int(nav_target.replace("history_", ""))
        if 0 <= idx < len(st.session_state.past_chats):
            if st.session_state.messages:
                first_user_msg = next(
                    (m["content"] for m in st.session_state.messages if m["role"] == "user"),
                    "Conversation"
                )
                st.session_state.past_chats.append({
                    "preview": first_user_msg,
                    "messages": st.session_state.messages
                })
            st.session_state.messages = st.session_state.past_chats[idx]["messages"]
            st.session_state.page = "Chat"
    # Clear nav param after processing
    st.query_params.clear()
    st.rerun()

# Inject recent chats into drawer via JS
if st.session_state.past_chats:
    chats_js = ""
    for idx, chat in enumerate(reversed(st.session_state.past_chats[-10:])):
        preview = chat["preview"]
        preview = preview if len(preview) <= 32 else preview[:32] + "..."
        real_idx = len(st.session_state.past_chats) - 1 - idx
        escaped = js_escape(preview)
        chats_js += f"""
        <div class="drawer-recent-item" onclick="navTo('history_{real_idx}')">
            <div class="drawer-recent-dot"></div>
            {escaped}
        </div>
        """
    st.markdown(f"""
    <script>
    (function() {{
        var list = document.getElementById('recent-chats-list');
        if (list) list.innerHTML = `{chats_js}`;
    }})();
    </script>
    """, unsafe_allow_html=True)

# ===== HERO =====
st.markdown("""
<div class='hero'>
    <div class='hero-icon-wrap'>
        <div class='hero-icon'>🔥</div>
    </div>
    <h1>INTELLEXA</h1>
    <p class='subtitle'>YOUR STUDY COMPANION</p>
</div>
""", unsafe_allow_html=True)

# ===== PAGES =====
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