import re
import nltk
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer


def translate(compound):
    if compound < -0.25:
        return "negative"
    elif -0.25 < compound < 1.25:
        return "neutral"
    else:
        return "positive"


def analyse_lyrics(lyrics):
    # sentiment analysis
    sia = SentimentIntensityAnalyzer()
    compound = sia.polarity_scores(lyrics)["compound"]
    compound_translated = translate(compound)

    # stats
    chorus_count = lyrics.count("Chorus")
    love_count = lyrics.count("love")
    hate_count = lyrics.count("hate")
    pattern_n_words = re.compile("[a-zA-Z]+")
    number_of_words = re.findall(pattern_n_words, lyrics.lower())

    d = {}

    for word in number_of_words:
        if word in d.keys():
            d[word] = d[word] + 1
        else:
            d[word] = 1

    d_list = [(value, key) for (key, value) in d.items()]
    filtered_words = []
    for count, word in d_list:
        if word not in stopwords.words("english"):
            filtered_words.append((word, count))

    d_list_sorted = sorted(filtered_words, reverse=True)

    return_statement = f"""
    This song is mostly {compound_translated} \n
    The chorus repeats {chorus_count} times \n
    The word 'love' was mentioned {love_count} times \n
    The word 'hate' was mentioned {hate_count} times \n
    The total number of words is {len(number_of_words)} \n
    The most used words (non-articles or pronouns) 
    were '{d_list_sorted[0][0]}' 
    (used {d_list_sorted[0][1]} times) and 
    {d_list_sorted[1][0]}' (used {d_list_sorted[1][1]}
    times)
    """
    return return_statement

