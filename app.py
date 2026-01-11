import streamlit as st
from logic import (
    load_models,
    extract_text_from_pdf,
    generate_summary,
    generate_quiz,
    generate_flashcards
)

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="AI Study Buddy",
    page_icon="📘",
    layout="wide"
)

# =====================================================
# SESSION STATE
# =====================================================
for key in ["text", "summary", "generated"]:
    if key not in st.session_state:
        st.session_state[key] = ""

# =====================================================
# LOAD MODELS
# =====================================================
@st.cache_resource(show_spinner=False)
def get_models():
    return load_models()

with st.spinner("🔄 Loading AI models (first run may take a minute)..."):
    summarizer, generator = get_models()

# =====================================================
# HEADER
# =====================================================
st.title("📘 AI Study Buddy")
st.caption("Paste text or attach a PDF, then generate summaries, quizzes, or flashcards")

st.markdown("---")

# =====================================================
# INPUT AREA (TEXT + ATTACH ICON)
# =====================================================
st.subheader("✍️ Study Material")

col_text, col_attach = st.columns([10, 1])

with col_text:
    text_input = st.text_area(
        "",
        height=220,
        placeholder="Paste your notes, lecture content, or textbook text here..."
    )

with col_attach:
    pdf_file = st.file_uploader(
        "📎",
        type=["pdf"],
        label_visibility="collapsed"
    )

# =====================================================
# PROCESS INPUT
# =====================================================
if pdf_file:
    with st.spinner("📄 Extracting text from PDF..."):
        st.session_state.text = extract_text_from_pdf(pdf_file)
elif text_input.strip():
    st.session_state.text = text_input.strip()
else:
    st.session_state.text = ""

# =====================================================
# MODE NAVIGATION (TABS)
# =====================================================
st.markdown("---")
st.subheader("🎯 Study Modes")

tab_summary, tab_quiz, tab_flashcards = st.tabs(
    ["📄 Summary", "❓ Quiz", "🧠 Flashcards"]
)

# =====================================================
# GENERATE BUTTON
# =====================================================
st.markdown("")

generate = st.button(
    "🚀 Generate",
    use_container_width=True,
    disabled=not bool(st.session_state.text)
)

if generate:
    with st.spinner("✨ Generating content..."):
        st.session_state.summary = generate_summary(
            summarizer,
            st.session_state.text
        )
        st.session_state.generated = True

# =====================================================
# OUTPUT — SUMMARY
# =====================================================
with tab_summary:
    if st.session_state.generated:
        st.success("Summary generated successfully!")
        st.write(st.session_state.summary)
    else:
        st.info("Generate content to see the summary.")

# =====================================================
# OUTPUT — QUIZ
# =====================================================
with tab_quiz:
    if st.session_state.generated:
        st.success("Quiz generated successfully!")
        questions = generate_quiz(generator, st.session_state.summary)
        for i, q in enumerate(questions, 1):
            st.markdown(f"**Q{i}.** {q}")
    else:
        st.info("Generate content to see quiz questions.")

# =====================================================
# OUTPUT — FLASHCARDS
# =====================================================
with tab_flashcards:
    if st.session_state.generated:
        st.success("Flashcards generated successfully!")
        cards = generate_flashcards(generator, st.session_state.summary)
        for i, card in enumerate(cards, 1):
            with st.expander(f"🧠 Flashcard {i}"):
                st.write(card)
    else:
        st.info("Generate content to see flashcards.")

# =====================================================
# FOOTER
# =====================================================
st.markdown("---")
st.caption("Built with ❤️ using Streamlit & AI")
