# Assignment (21/03/2026)
# Assignment Name: Build a Text Cleaner
# Description: Write code to remove punctuation, lowercase text, remove stopwords and test it

import string

# Sample text
text = "Hello!!! This is an Example sentence, showing how THE text cleaner works 😊."

# Define simple stopwords list
stopwords = ["is", "an", "the", "how", "this"]

# Step 1: Convert to lowercase
text_lower = text.lower()

# Step 2: Remove punctuation
text_no_punct = text_lower.translate(str.maketrans('', '', string.punctuation))

# Step 3: Tokenization (split into words)
words = text_no_punct.split()

# Step 4: Remove stopwords
cleaned_words = [word for word in words if word not in stopwords]

# Step 5: Join words back
cleaned_text = " ".join(cleaned_words)

# Output
print("Original Text:\n", text)
print("\nCleaned Text:\n", cleaned_text)