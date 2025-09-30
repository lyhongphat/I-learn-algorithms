import streamlit as st
from utils import load_translation

def main():
    st.set_page_config(
        page_title="I Learn Algorithms",
        page_icon="🧮",
        layout="wide"
    )
    
    # Language selector in the sidebar
    language = st.sidebar.selectbox(
        "Language / Ngôn ngữ / 言語 / 언어",
        ["English", "Vietnamese", "Japanese", "Korean"]
    )
    
    # Get translations for the selected language and any missing keys
    t, missing_keys = load_translation(language)

    # Show notification if there are missing translations
    if missing_keys and language != "English":
        warnings = {
            "Vietnamese": "Một số nội dung chưa được dịch sang tiếng Việt và sẽ được hiển thị bằng tiếng Anh.",
            "Japanese": "一部のコンテンツは日本語に完全には翻訳されておらず、英語で表示されます。",
            "Korean": "일부 내용은 아직 한국어로 완전히 번역되지 않아 영어로 표시됩니다。",
            "English": "Some content is not yet fully translated and will be shown in English."
        }
        st.warning(warnings[language])

    st.title(f"{t['page_title']} 🧮")
    st.markdown("---")

    # Define categories list
    categories = [
        "arrays_hashing",
        "two_pointers",
        "stack",
        "binary_search",
        "sliding_window",
        "linked_list",
        "trees",
        "tries",
        "heap",
        "backtracking",
        "graphs",
        "advanced_graphs",
        "dp_1d",
        "dp_2d",
        "greedy",
        "intervals",
        "math_geometry",
        "bit_manipulation"
    ]

    def on_category_change():
        st.session_state.selected_category_index = st.session_state.temp_category_index

    # Initialize session states if not exists
    if 'selected_category_index' not in st.session_state:
        st.session_state.selected_category_index = 0
    if 'temp_category_index' not in st.session_state:
        st.session_state.temp_category_index = st.session_state.selected_category_index

    # Sidebar for navigation
    st.sidebar.title(t["categories"])
    _ = st.sidebar.radio(
        t["select_category"],
        range(len(categories)),
        format_func=lambda x: t[categories[x]],
        key="temp_category_index",
        on_change=on_category_change,
        index=st.session_state.selected_category_index
    )

    # Get current category key
    current_category = categories[st.session_state.selected_category_index]
    
    # Display content
    st.header(t[current_category])
    if f"{current_category}_desc" in t:
        st.write(t[f"{current_category}_desc"])

if __name__ == "__main__":
    main()
