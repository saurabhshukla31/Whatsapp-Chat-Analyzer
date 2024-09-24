# 📊 Whatsapp Chat Analyzer

**Whatsapp Chat Analyzer** built with **Python** and **Streamlit** that allows users to analyze chat logs for key insights. This tool offers a comprehensive breakdown of chat statistics, activity timelines, word clouds, emoji usage, and sentiment analysis. You can perform analysis for a specific user or view overall chat trends.

## 🚀 Features
- Top statistics on message activity
- Activity timelines and heatmaps
- Word cloud visualization
- Most common words analysis
- Emoji usage breakdown
- Sentiment analysis for users and the overall chat

## 📦 Installation

1. **Clone the repository:**
   ```bash
   gh repo clone saurabhshukla31/Whatsapp-Chat-Analyzer
   ```

2. **Navigate to the project directory:**
   ```bash
   cd Whatsapp-chat-analyzer
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

1. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser and visit:**
   ```
   http://localhost:8501
   ```

3. **Upload your chat log file** through the file uploader in the sidebar.

4. **Select a user** from the dropdown menu (or analyze the overall chat).

5. **Click "Show Analysis"** to view the chat insights.

## 🗂 Project Structure
- **`app.py`**: Main Streamlit application
- **`preprocessor.py`**: Preprocessing functions for cleaning and preparing the chat log
- **`helper.py`**: Helper functions for various analyses
- **`stopwords.txt`**: Contains common stopwords to exclude from word cloud and common words analysis
