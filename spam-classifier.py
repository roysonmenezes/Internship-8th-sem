# Assignment (10/03/2026)
# Assignment Name: Spam Classifier Thinking
# Description: Design a spam detection system: features, data needed, possible mistakes

# Designing a simple spam detection concept

spam_system = {
    "Features": [
        "Presence of suspicious words (free, win, offer)",
        "Number of links in the message",
        "Sender email address",
        "Message length",
        "Frequency of capital letters"
    ],
    
    "Data Needed": [
        "Collection of spam emails",
        "Collection of legitimate emails",
        "Email metadata such as sender and time",
        "Text content of messages"
    ],
    
    "Possible Mistakes": [
        "Important emails may be marked as spam (False Positive)",
        "Spam emails may pass as normal emails (False Negative)",
        "Short promotional emails may confuse the model",
        "New spam patterns may not be recognized"
    ]
}

print("Spam Detection System Design\n")

for key, values in spam_system.items():
    print(key + ":")
    for item in values:
        print("-", item)
    print()