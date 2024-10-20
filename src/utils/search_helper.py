from competitor_list import competitorList as data_list
from collections import defaultdict

def generate_trigrams(word):
    """
    Generate trigrams from a word.
    
    :param word: Input string
    :return: Set of trigrams
    """
    # Add padding at the beginning and end of the word for better matching
    padded_word = f"  {word}  "
    trigrams = {padded_word[i:i+3] for i in range(len(padded_word) - 2)}
    return trigrams

def build_trigram_index(data_list):
    """
    Build a trigram index for a list of strings.
    
    :param data_list: List of strings
    :return: Dictionary mapping trigrams to a list of words containing them
    """
    trigram_index = defaultdict(list)
    
    for word in data_list:
        word_trigrams = generate_trigrams(word.lower())
        for trigram in word_trigrams:
            trigram_index[trigram].append(word)
    
    return trigram_index

def trigram_search(query, data_list = data_list):
    """
    Perform trigram-based search.
    
    :param query: The search query string
    :param trigram_index: Trigram index built from the data
    :return: List of matching results
    """
    if not query:
        return data_list
    
    trigram_index = build_trigram_index(data_list)
    query_trigrams = generate_trigrams(query.lower())
    
    # Get potential matches by finding common trigrams in the index
    potential_matches = defaultdict(int)
    for trigram in query_trigrams:
        for word in trigram_index.get(trigram, []):
            potential_matches[word] += 1
    
    # Sort potential matches by the number of matching trigrams (best match first)
    sorted_matches = sorted(potential_matches.items(), key=lambda x: x[1], reverse=True)
    
    return [match[0] for match in sorted_matches]