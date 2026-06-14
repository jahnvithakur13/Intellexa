import streamlit as st
import streamlit.components.v1 as components
from chatbot import get_ai_response, extract_text_from_file, get_ai_response_with_image

st.set_page_config(page_title="Intellexa", page_icon="🎓", layout="wide")

# ---------- Custom styling ----------
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

/* Hide Streamlit Cloud's Fork/GitHub/menu/footer, but keep header so the
   sidebar toggle (collapsedControl) remains visible and functional */
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

/* Native sidebar toggle: kept in DOM (so JS can still .click() it) but
   visually hidden — our custom hamburger button replaces it */
[data-testid="collapsedControl"] {
    opacity: 0 !important;
    pointer-events: none !important;
    width: 1px !important;
    height: 1px !important;
    overflow: hidden !important;
}

.block-container {
    padding-top: 1rem;
    padding-bottom: 0rem;
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
.stButton button, button[kind="formSubmit"] {
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

.mic-btn {
    background: rgba(255,255,255,0.08) !important;
    color: white !important;
    border-radius: 50% !important;
    width: 44px !important;
    height: 44px !important;
    font-size: 18px !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    flex-shrink: 0;
}
.mic-btn:hover {
    border: 1px solid #ff3c3c !important;
    background: rgba(255, 60, 60, 0.15) !important;
}
.mic-btn.listening {
    background: #ff3c3c !important;
    box-shadow: 0 0 12px rgba(255, 60, 60, 0.7);
    animation: pulse 1s infinite;
}
@keyframes pulse {
    0% { box-shadow: 0 0 5px rgba(255, 60, 60, 0.5); }
    50% { box-shadow: 0 0 18px rgba(255, 60, 60, 0.9); }
    100% { box-shadow: 0 0 5px rgba(255, 60, 60, 0.5); }
}

#intellexa-hamburger {
    position: fixed;
    top: 14px;
    left: 14px;
    z-index: 999999;
    width: 42px;
    height: 42px;
    display: none;
    align-items: center;
    justify-content: center;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255, 80, 80, 0.35);
    border-radius: 10px;
    color: #fff;
    font-size: 20px;
    cursor: pointer;
    backdrop-filter: blur(4px);
}
#intellexa-hamburger:active {
    background: #ff3c3c;
}
@media (max-width: 768px) {
    #intellexa-hamburger {
        display: flex;
    }
}

/* ---------- Fixed footer ---------- */
.fixed-footer {
    position: fixed;
    bottom: 0;
    left: 280px;
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

/* spacer so chat content doesn't get hidden behind fixed footer */
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

section[data-testid="stSidebar"] {
    background: #08080c;
    background-color: #08080c !important;
    border-right: 1px solid rgba(255, 80, 80, 0.15);
    min-width: 280px !important;
    width: 280px !important;
    z-index: 1000;
}

section[data-testid="stSidebar"] > div {
    background-color: #08080c !important;
}

section[data-testid="stSidebar"] .block-container {
    padding-top: 1rem;
}

section[data-testid="stSidebar"] div[data-testid="stVerticalBlock"] {
    gap: 0.35rem !important;
}

section[data-testid="stSidebar"] .stButton button {
    white-space: nowrap !important;
    width: 100% !important;
    text-align: left !important;
    padding: 10px 14px !important;
    font-size: 14px !important;
    border-radius: 10px !important;
    font-weight: 500 !important;
    background: rgba(255,255,255,0.04) !important;
    color: #cfcfcf !important;
    border: 1px solid transparent !important;
    margin: 0 !important;
}

section[data-testid="stSidebar"] .stButton {
    margin-bottom: 0px !important;
}

section[data-testid="stSidebar"] .stButton button:hover {
    border: 1px solid #ff3c3c !important;
    color: white !important;
}

.nav-active button {
    background: linear-gradient(135deg, #ff3c3c, #ff8c00) !important;
    color: white !important;
    font-weight: 700 !important;
}

.sidebar-logo {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 10px 0px 16px 0px;
}
.sidebar-logo .emblem-sm {
    width: 42px;
    height: 42px;
    border: 2px solid #ff3c3c;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    background: #0a0a0f;
    flex-shrink: 0;
}
.sidebar-logo .text h2 {
    margin: 0px;
    font-size: 18px;
    color: white;
    letter-spacing: 2px;
}
.sidebar-logo .text p {
    margin: 0px;
    font-size: 10px;
    color: #ff3c3c;
    letter-spacing: 2px;
}

.quote-box {
    border: 1px solid rgba(255, 80, 80, 0.25);
    border-radius: 10px;
    padding: 12px;
    margin-top: 20px;
    font-size: 12px;
    color: #ccc;
    line-height: 1.6;
}
.quote-box .author {
    color: #ff3c3c;
    font-size: 11px;
    margin-top: 6px;
    display: block;
}

.history-item {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255, 80, 80, 0.12);
    border-radius: 8px;
    padding: 8px 10px;
    margin-bottom: 6px;
    font-size: 13px;
    color: #d7d7e0;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

@media (max-width: 768px) {
    .stApp { height: auto; overflow: auto; }
    .hero h1 { font-size: 32px; letter-spacing: 3px; }
    .hero .subtitle { font-size: 12px; letter-spacing: 2px; }
    .hero .desc { font-size: 13px; }
    .main-card { padding: 16px; margin: 10px; max-height: none; overflow-y: visible; }
    .chat-bubble-user, .chat-bubble-bot { max-width: 90%; font-size: 14px; }
    .welcome-text h3 { font-size: 17px; }
    .fixed-footer { left: 0; }

    /* ---- ChatGPT/Claude-style sliding drawer sidebar ---- */
    section[data-testid="stSidebar"] {
        position: fixed !important;
        top: 0;
        left: 0;
        height: 100vh !important;
        width: 80% !important;
        max-width: 320px !important;
        min-width: 0 !important;
        z-index: 1000;
        box-shadow: 4px 0 24px rgba(0,0,0,0.6);
        transition: transform 0.25s ease-in-out;
        transform: translateX(0%);
    }

    /* When collapsed, slide fully off-screen */
    section[data-testid="stSidebar"][aria-expanded="false"] {
        transform: translateX(-100%);
    }

    /* Dark backdrop behind the open drawer */
    section[data-testid="stSidebar"][aria-expanded="true"]::after {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background: rgba(0,0,0,0.55);
        z-index: -1;
    }

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

# ---------- JS: fix mobile viewport, hide Streamlit Cloud badges,
#             and add a custom hamburger button to toggle the sidebar ----------
components.html("""
<script>
(function(){
    var doc = window.parent.document;

    // 1. Ensure a proper mobile viewport so the page isn't rendered as
    //    a shrunken desktop layout on phones.
    var meta = doc.querySelector('meta[name="viewport"]');
    if(!meta){
        meta = doc.createElement('meta');
        meta.name = 'viewport';
        doc.head.appendChild(meta);
    }
    meta.setAttribute('content', 'width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no');

    // 2. Hide Streamlit Cloud's profile/"Hosted with Streamlit" badges.
    function hideBadges(){
        doc.querySelectorAll('a, div, span').forEach(function(el){
            var txt = (el.textContent || '').trim();
            if(txt === 'Hosted with Streamlit' || txt.indexOf('Created by') === 0){
                el.style.setProperty('display', 'none', 'important');
            }
        });
    }
    hideBadges();
    setInterval(hideBadges, 1500);

    // 3. Custom hamburger button that triggers Streamlit's native sidebar toggle.
    function ensureHamburger(){
        if(doc.getElementById('intellexa-hamburger')) return;
        var btn = doc.createElement('div');
        btn.id = 'intellexa-hamburger';
        btn.innerHTML = '&#9776;';
        btn.title = 'Menu';
        btn.onclick = function(){
            var native = doc.querySelector('[data-testid="collapsedControl"] button')
                       || doc.querySelector('[data-testid="collapsedControl"]');
            if(native){ native.click(); }
        };
        doc.body.appendChild(btn);
    }
    ensureHamburger();
    setInterval(ensureHamburger, 1500);
})();
</script>
""", height=0, width=0)

# ---------- Helper: escape text for safe use in JS onclick string ----------
def js_escape(text):
    return (
        text.replace("\\", "\\\\")
            .replace("'", "\\'")
            .replace('"', '\\"')
            .replace("\n", " ")
            .replace("\r", " ")
    )


# ---------- Session state ----------
if "messages" not in st.session_state:
    st.session_state.messages = []
if "page" not in st.session_state:
    st.session_state.page = "Chat"
if "past_chats" not in st.session_state:
    st.session_state.past_chats = []

# ---------- Sidebar ----------
with st.sidebar:
    st.markdown("""
    <div class='sidebar-logo'>
        <div class='emblem-sm'>🔥</div>
        <div class='text'>
            <h2>INTELLEXA</h2>
            <p>AI STUDY ASSISTANT</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    nav_items = {
        "Chat": "💬 Chat",
        "Quick Notes": "📝 Quick Notes",
    }

    for key, label in nav_items.items():
        is_active = st.session_state.page == key
        wrapper_class = "nav-active" if is_active else ""
        st.markdown(f"<div class='{wrapper_class}'>", unsafe_allow_html=True)
        if st.button(label, key=f"nav_{key}"):
            st.session_state.page = key
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

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

    st.markdown("#### 🕓 Recent Chats")
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
    <div class='quote-box'>
        "Push forward, even one step at a time. Every bit of effort sharpens your skills."
        <span class='author'>— Inspired by Demon Slayer</span>
    </div>
    """, unsafe_allow_html=True)

# ---------- Hero Header ----------
st.markdown("""
<div class='hero'>
    <div class='hero-icon'>🔥</div>
    <h1>INTELLEXA</h1>
    <p class='subtitle'>YOUR STUDY COMPANION</p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# PAGE: CHAT
# ============================================================
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

# ============================================================
# PAGE: QUICK NOTES
# ============================================================
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

# ---------- Fixed Footer (always at bottom of page) ----------
st.markdown("""
<div class='fixed-footer'>
    <p class='disclaimer'>Intellexa only answers questions about education, careers, jobs, and industry trends.</p>
    <p class='tag'>◆ KNOWLEDGE IS POWER ◆</p>
</div>
""", unsafe_allow_html=True)