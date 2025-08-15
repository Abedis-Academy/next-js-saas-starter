"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix."""
    return "un" + word


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended."""
    prefix = vocab_words[0]
    return " :: ".join([prefix] + [prefix + word for word in vocab_words[1:]])


def remove_suffix_ness(word):
    """Remove the suffix 'ness' from the word while keeping spelling in mind."""
    if word.endswith("ness"):
        root = word[:-4]  # remove 'ness'
        if root.endswith("i"):
            return root[:-1] + "y"
        return root
    return word


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb."""
    words = sentence.strip().replace(".", "").split()
    return words[index] + "en"