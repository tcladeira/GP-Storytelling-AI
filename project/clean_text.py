import re
import unicodedata

def clean_text(text):

    text = unicodedata.normalize("NFKC", text)

    # 4. Remove Gutenberg boilerplate text
    text = re.sub(r"Project Gutenberg.*?(\n\n|\Z)", "", text, flags=re.DOTALL|re.IGNORECASE)
    text = re.sub(r"End of the Project Gutenberg.*", "", text, flags=re.IGNORECASE)

    # 5. Remove multiple newlines → single newline
    text = re.sub(r"\n{2,}", "\n", text)

    # 6. Fix spacing (remove excess spaces)
    text = re.sub(r"[ ]{2,}", " ", text)

    # 7. Ensure punctuation spacing is correct
    text = re.sub(r"\s+([,.!?;:])", r"\1", text)   # no space before punctuation
    text = re.sub(r"([,.!?;:])([^\s])", r"\1 \2", text)  # space after punctuation

    # 8. Remove weird symbols
    text = re.sub(r"[^a-zA-Z0-9,.!?;:'\"\-\n ]+", " ", text)

    # 9. Trim whitespace
    text = text.strip()

    return text