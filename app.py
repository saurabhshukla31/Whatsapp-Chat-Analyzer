import streamlit as st
import preprocessor, helper
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import seaborn as sns

# Set page configuration
st.set_page_config(
    page_title="Whatsapp Chat Analyzer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS to style the app
st.markdown("""
<style>
    /* Global styles */
    body {
        color: #ffffff;
        background-color: #1e1e1e;
    }
    .stApp {
        background-color: #1e1e1e;
    }
    
    /* Sidebar styles */
    .css-1d391kg {
        background-color: #2b2b2b;
    }
    
    /* Header styles */
    h1, h2, h3 {
        color: #ffffff !important;
    }
    
    /* Button styles */
    .stButton>button {
        color: #ffffff;
        background-color: #4CAF50;
        border: none;
        border-radius: 4px;
        padding: 10px 24px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    
    /* File uploader styles */
    .stFileUploader {
        background-color: #2b2b2b;
        border: 1px solid #4CAF50;
        border-radius: 4px;
        padding: 10px;
    }
    
    /* Metric styles */
    .stMetric {
        background-color: #2b2b2b;
        border: 1px solid #4CAF50;
        border-radius: 4px;
        padding: 10px;
    }
    
    /* DataFrame styles */
    .dataframe {
        background-color: #2b2b2b;
        color: #ffffff;
    }
</style>
""", unsafe_allow_html=True)

# Welcome message
st.title("Welcome to the Whatsapp Chat Analyzer👋")
st.write("To get started, follow these steps:")
st.write("1. Open Whatsapp and go to the chat you want to analyze.")
st.write("2. Tap on the chat menu and select 'More'.")
st.write("3. Tap on 'Export chat' and choose 'Without media'.")
st.write("4. Upload the exported file to this app using the file uploader below.")

# Sidebar
st.sidebar.title("Whatsapp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file", key="file_uploader")

if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    mydata = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(mydata)

    # Fetch unique users
    user_list = df['user'].unique().tolist()
    user_list.remove("group_notification")
    user_list.sort()
    user_list.insert(0, "Overall")

    selected_user = st.sidebar.selectbox("Show Analysis with respect to", user_list)

if st.sidebar.button("Show Analysis"):
    st.title("Chat Analysis Results")
    
    # Top Statistics
    st.header("Top Statistics")
    num_messages, words, num_media_msg, links = helper.fetch_stats(selected_user, df)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Messages", num_messages)
    with col2:
        st.metric("Total Words", words)
    with col3:
        st.metric("Media Shared", num_media_msg)
    with col4:
        st.metric("Links Shared", links)
    
    # Monthly Timeline
    st.header("Monthly Activity Timeline")
    timeline = helper.monthly_timeline(selected_user, df)
    fig, ax = plt.subplots(figsize=(12, 6))
    
    palette = sns.color_palette("viridis", 1)
    sns.lineplot(x='time', y='message', data=timeline, palette=palette, linewidth=2.5)
    
    plt.xticks(rotation='vertical')
    plt.xlabel('Time', fontsize=12)
    plt.ylabel('Messages', fontsize=12)
    plt.title('Monthly Activity', fontsize=16)
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Set dark background for the plot
    fig.patch.set_facecolor('#1e1e1e')
    ax.set_facecolor('#1e1e1e')
    ax.tick_params(colors='white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.title.set_color('white')
    
    st.pyplot(fig)
    
    # Daily Timeline
    st.header("Daily Activity Timeline")
    d_timeline = helper.daily_timeline(selected_user, df)
    fig, ax = plt.subplots(figsize=(12, 6))
    
    palette = sns.color_palette("viridis", 1)
    sns.lineplot(x='only_date', y='message', data=d_timeline, palette=palette, linewidth=2.5)
    
    plt.xticks(rotation='vertical')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Messages', fontsize=12)
    plt.title('Daily Activity', fontsize=16)
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Set dark background for the plot
    fig.patch.set_facecolor('#1e1e1e')
    ax.set_facecolor('#1e1e1e')
    ax.tick_params(colors='white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.title.set_color('white')
    
    st.pyplot(fig)
    
    # Activity Map
    st.header("Activity Map")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Most Busy Day")
        busy_day = helper.week_activity_map(selected_user, df)
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(busy_day.index, busy_day.values)
        plt.xticks(rotation='vertical')
        plt.xlabel('Day of the Week', fontsize=12)
        plt.ylabel('Message Count', fontsize=12)
        plt.title('Most Busy Day', fontsize=14)
        plt.grid(True, linestyle='--', alpha=0.7)
        
        # Set dark background for the plot
        fig.patch.set_facecolor('#1e1e1e')
        ax.set_facecolor('#1e1e1e')
        ax.tick_params(colors='white')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.title.set_color('white')
        
        st.pyplot(fig)
    
    with col2:
        st.subheader("Most Busy Month")
        busy_month = helper.month_activity_map(selected_user, df)
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(busy_month.index, busy_month.values)
        plt.xticks(rotation='vertical')
        plt.xlabel('Month', fontsize=12)
        plt.ylabel('Message Count', fontsize=12)
        plt.title('Most Busy Month', fontsize=14)
        plt.grid(True, linestyle='--', alpha=0.7)
        
        # Set dark background for the plot
        fig.patch.set_facecolor('#1e1e1e')
        ax.set_facecolor('#1e1e1e')
        ax.tick_params(colors='white')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.title.set_color('white')
        
        st.pyplot(fig)
    
    # Most Busy Users
    if selected_user == 'Overall':
        st.header('Most Busy Users')
        x, new_df = helper.most_busy_user(df)
        
        col1, col2 = st.columns(2)
        
        with col1:
            colors = cm.viridis(np.linspace(0, 1, len(x.index)))
            fig, ax = plt.subplots(figsize=(6, 4))
            ax.bar(x.index, x.values, color=colors)
            plt.title('User Activity', fontsize=14)
            plt.xlabel('User', fontsize=12)
            plt.ylabel('Activity Count', fontsize=12)
            plt.xticks(rotation='vertical')
            plt.grid(True, linestyle='--', alpha=0.7)
            
            # Set dark background for the plot
            fig.patch.set_facecolor('#1e1e1e')
            ax.set_facecolor('#1e1e1e')
            ax.tick_params(colors='white')
            ax.xaxis.label.set_color('white')
            ax.yaxis.label.set_color('white')
            ax.title.set_color('white')
            
            st.pyplot(fig)
        
        with col2:
            st.write('## User Activity Data')
            st.dataframe(new_df.style.highlight_max(color='lightgreen'))
    
    # Weekly Activity Heatmap
    st.header("Weekly Activity Map")
    user_heatmap = helper.activity_heatmap(selected_user, df)
    fig, ax = plt.subplots(figsize=(12, 6))
    
    sns.heatmap(user_heatmap, cmap='viridis', linewidths=0.001, linecolor='white', cbar_kws={'label': 'Activity Level'}, ax=ax)
    plt.xlabel('Hour of the Day', fontsize=12)
    plt.ylabel('Day of the Week', fontsize=12)
    plt.title('Weekly Activity', fontsize=16)
    
    # Set dark background for the plot
    fig.patch.set_facecolor('#1e1e1e')
    ax.set_facecolor('#1e1e1e')
    ax.tick_params(colors='white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.title.set_color('white')
    
    st.pyplot(fig)
    
    # Emoji Analysis
    st.header("Emoji Analysis")
    col1, col2 = st.columns(2)
    
    with col1:
        emoji_df = helper.emoji_helper(selected_user, df)
        st.dataframe(emoji_df)
    
    with col2:
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.pie(emoji_df["Frequency"].head(), labels=emoji_df["Emoji"].head(), autopct="%0.2f")
        plt.title('Top Emojis', fontsize=14)
        plt.axis('equal')
        
        # Set dark background for the plot
        fig.patch.set_facecolor('#1e1e1e')
        ax.set_facecolor('#1e1e1e')
        ax.tick_params(colors='white')
        ax.title.set_color('white')
        
        st.pyplot(fig)
    
    # Sentiment Analysis
    st.header("Sentiment Analysis")
    user_sentiments = helper.analyze_sentiment(selected_user, df)
    
    if selected_user == 'Overall':
        overall_sentiment = {key: sum([user[key] for user in user_sentiments.values()])/len(user_sentiments) for key in ['pos', 'neu', 'neg', 'compound']}
        st.subheader("Overall Sentiment")
        
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.barh(list(overall_sentiment.keys()), list(overall_sentiment.values()), color=['green' if v >= 0 else 'red' for v in overall_sentiment.values()])
        ax.set_xlabel('Score')
        ax.set_title('Overall Sentiment Scores', fontsize=14)
        
        # Set dark background for the plot
        fig.patch.set_facecolor('#1e1e1e')
        ax.set_facecolor('#1e1e1e')
        ax.tick_params(colors='white')
        ax.xaxis.label.set_color('white')
        ax.title.set_color('white')
        
        st.pyplot(fig)
    elif selected_user in user_sentiments:
        sentiment_scores = user_sentiments[selected_user]
        st.subheader(f"Sentiment for {selected_user}")
        
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.barh(list(sentiment_scores.keys()), list(sentiment_scores.values()), color=['green' if v >= 0 else 'red' for v in sentiment_scores.values()])
        ax.set_xlabel('Score')
        ax.set_title(f'Sentiment Scores for {selected_user}', fontsize=14)
        
        # Set dark background for the plot
        fig.patch.set_facecolor('#1e1e1e')
        ax.set_facecolor('#1e1e1e')
        ax.tick_params(colors='white')
        ax.xaxis.label.set_color('white')
        ax.title.set_color('white')
        
        st.pyplot(fig)
    else:
        st.write(f"No sentiment analysis results for {selected_user}")
    
    # Display the overall sentiment score
    sentiment = helper.sentiment_score(user_sentiments, selected_user)
    st.subheader(f"The overall sentiment of {selected_user} is {sentiment}")