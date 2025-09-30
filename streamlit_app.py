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

    # Sidebar for navigation
    st.sidebar.title(t["categories"])
    category = st.sidebar.radio(
        t["select_category"],
        [
            t["arrays_hashing"],
            t["two_pointers"],
            t["stack"],
            t["binary_search"],
            t["sliding_window"],
            t["linked_list"],
            t["trees"],
            t["tries"],
            t["heap"],
            t["backtracking"],
            t["graphs"],
            t["advanced_graphs"],
            t["dp_1d"],
            t["dp_2d"],
            t["greedy"],
            t["intervals"],
            t["math_geometry"],
            t["bit_manipulation"]
        ]
    )

    # Content based on selection
    if category == t["arrays_hashing"]:
        st.header(t["arrays_hashing"])
        st.write(t["arrays_hashing_desc"])

    elif category == t["two_pointers"]:
        st.header(t["two_pointers"])
        st.write(t["two_pointers_desc"])

    elif category == t["stack"]:
        st.header(t["stack"])
        st.write(t["stack_desc"])

    elif category == t["binary_search"]:
        st.header(t["binary_search"])
        st.write(t["binary_search_desc"])

    elif category == t["sliding_window"]:
        st.header(t["sliding_window"])
        st.write(t["sliding_window_desc"])

    elif category == t["linked_list"]:
        st.header(t["linked_list"])
        st.write(t["linked_list_desc"])

    elif category == t["trees"]:
        st.header(t["trees"])
        st.write(t["trees_desc"])

    elif category == t["tries"]:
        st.header(t["tries"])
        st.write(t["tries_desc"])

    elif category == t["heap"]:
        st.header(t["heap"])
        st.write(t["heap_desc"])

    elif category == t["backtracking"]:
        st.header(t["backtracking"])
        st.write(t["backtracking_desc"])

    elif category == t["graphs"]:
        st.header(t["graphs"])
        st.write(t["graphs_desc"])

    elif category == t["advanced_graphs"]:
        st.header(t["advanced_graphs"])
        st.write(t["advanced_graphs_desc"])

    elif category == t["dp_1d"]:
        st.header(t["dp_1d"])
        st.write(t["dp_1d_desc"])

    elif category == t["dp_2d"]:
        st.header(t["dp_2d"])
        st.write(t["dp_2d_desc"])

    elif category == t["greedy"]:
        st.header(t["greedy"])
        st.write(t["greedy_desc"])

    elif category == t["intervals"]:
        st.header(t["intervals"])
        st.write(t["intervals_desc"])

    elif category == t["math_geometry"]:
        st.header(t["math_geometry"])
        st.write(t["math_geometry_desc"])

    elif category == t["bit_manipulation"]:
        st.header(t["bit_manipulation"])
        st.write(t["bit_manipulation_desc"])

if __name__ == "__main__":
    main()
