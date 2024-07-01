# Sentiment Analysis and Data Extraction Script

This Python script utilizes web scraping techniques to extract text data from URLs, performs sentiment analysis using predefined lists of positive and negative words, and calculates various linguistic metrics. It is designed to automate the process of analyzing textual content from web pages and generate insightful metrics for further analysis.

## Features

- **Web Scraping**: Utilizes `requests` and `BeautifulSoup` to fetch and parse HTML content from specified URLs.
- **Sentiment Analysis**: Computes sentiment scores including positive score, negative score, polarity score, subjectivity score, and more.
- **Linguistic Metrics**: Calculates average sentence length, percentage of complex words, FOG index, average words per sentence, syllables per word, personal pronouns count, and average word length.
- **Data Processing**: Integrates with `pandas` for reading input data from CSV and updating output data to Excel files.
- **Google Drive Integration**: Downloads necessary files ("positive-words.txt" and "negative-words.txt") from Google Drive using `gdown.download`.

## Requirements

- Python 3.x
- Libraries:
  - `requests`
  - `BeautifulSoup` (bs4)
  - `pandas`
  - `nltk`
  - `syllapy`
  - `gdown`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your/repository.git
   cd repository
   ```
2. Install dependencies:
   ```bash
   pip install requests beautifulsoup4 pandas nltk syllapy
   ```
3. Download positive and negative word lists manually or integrate with Google Drive using gdown.download.
## Usage
1. Ensure Input.csv contains the necessary URLs for analysis.
2. Update positive-words.txt and negative-words.txt with relevant word lists for sentiment analysis.
3. Run the script
```bash
python sentiment_analysis.py
```
4. View processed data in Output Data Structure.xlsx with updated sentiment metrics.
