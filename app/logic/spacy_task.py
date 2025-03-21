import spacy
import pandas as pd
from pandas import DataFrame
from collections import Counter
from typing import List, Dict
import logging

import spacy
from spacy.lang.en.stop_words import STOP_WORDS

from collections import Counter
import pandas as pd


# Function to extract keywords from a text
def extract_keywords(text):
    nlp = spacy.load("en_core_web_sm")
    # List of stopwords to exclude (e.g., "paper")
    stopwords_to_exclude = {"paper", "study", "research", "method", "results", "data"}
    keywords = []
    doc = nlp(text)

    for token in doc:
        # Exclude stopwords and punctuation
        if token.text.lower() not in stopwords_to_exclude and not token.is_punct:
            if token.pos_ in [
                "NOUN",
                "ADJ",
                "PROPN",
            ]:  # Focus on nouns, adjectives, and proper nouns
                keywords.append(token.text.lower())

    # Also consider multi-word noun chunks (collocations)
    for chunk in doc.noun_chunks:
        keywords.append(chunk.text.lower())

    return keywords


def extract_keys(df: DataFrame) -> Dict[str, List[str]]:
    """
    Extract keywords from the titles and abstracts of papers in the DataFrame.
    Args:
        df (DataFrame): Input DataFrame containing 'title' and 'abstract'
    Returns:
        Dict[str, List[str]]: A dictionary containing the most common keywords in titles and abstracts
    """

    # Extract keywords separately from titles and abstracts
    title_keywords = []
    abstract_keywords = []

    # Extract keywords for each title and abstract
    try:
        for _, row in df.iterrows():

            title_keywords.extend(extract_keywords(row["title"]))
            abstract_keywords.extend(extract_keywords(row["abstract"]))

        # Count the frequency of keywords in titles and abstracts
        title_keyword_freq = Counter(title_keywords)
        abstract_keyword_freq = Counter(abstract_keywords)

        # Get the most common keywords
        most_common_title_keywords = title_keyword_freq.most_common(10)
        most_common_abstract_keywords = abstract_keyword_freq.most_common(10)
    except Exception as e:
        logging.error(f"Error extracting keywords: {e}")
        return {}

    # Display the most common keywords
    logging.info("Most common keywords in titles:")
    for keyword, freq in most_common_title_keywords:
        logging.info(f"{keyword}: {freq}")

    logging.info("\nMost common keywords in abstracts:")
    for keyword, freq in most_common_abstract_keywords:
        logging.info(f"{keyword}: {freq}")
