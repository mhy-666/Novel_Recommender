import streamlit as st

# 示例小说数据
novels = [
    {"title": "Pride and Prejudice", "author": "Jane Austen", "genre": "Romance"},
    {"title": "1984", "author": "George Orwell", "genre": "Dystopian"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Drama"},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Classic"},
    {"title": "Moby Dick", "author": "Herman Melville", "genre": "Adventure"},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "genre": "Classic"},
    {"title": "War and Peace", "author": "Leo Tolstoy", "genre": "Historical"},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "genre": "Fantasy"},
]

# Streamlit UI
st.title("Novel Recommender")

# 选择小说类型
genre_options = list(set(novel["genre"] for novel in novels))
selected_genre = st.selectbox("Select Genre", genre_options)

# 根据选择的类型推荐小说
recommended_novels = [novel for novel in novels if novel["genre"] == selected_genre]

# 显示推荐结果
st.subheader("Recommended Novels")
for novel in recommended_novels:
    st.write(f"**Title:** {novel['title']}")
    st.write(f"**Author:** {novel['author']}")
    st.write(f"**Genre:** {novel['genre']}")
    st.write("---")

# 搜索功能
search_query = st.text_input("Search by Title or Author")
if search_query:
    search_results = [novel for novel in novels if search_query.lower() in novel["title"].lower() or search_query.lower() in novel["author"].lower()]
    st.subheader("Search Results")
    if search_results:
        for novel in search_results:
            st.write(f"**Title:** {novel['title']}")
            st.write(f"**Author:** {novel['author']}")
            st.write(f"**Genre:** {novel['genre']}")
            st.write("---")
    else:
        st.write("No results found.")

# 添加新小说
with st.form("add_novel_form"):
    st.subheader("Add a New Novel")
    new_title = st.text_input("Title")
    new_author = st.text_input("Author")
    new_genre = st.selectbox("Genre", genre_options + ["Other"])
    new_genre_other = st.text_input("Other Genre") if new_genre == "Other" else None
    add_novel_button = st.form_submit_button("Add Novel")
    
    if add_novel_button:
        new_genre_final = new_genre_other if new_genre == "Other" else new_genre
        novels.append({"title": new_title, "author": new_author, "genre": new_genre_final})
        st.success("Novel added successfully!")

