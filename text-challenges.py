# Assignment (20/03/2026)
# Assignment Name: Text Challenges
# Description: Collect 20 messy sentences and identify slang, emojis, typos; explain preprocessing needed

# List of messy sentences
sentences = [
    "hey brooo!!! what's up 😂😂",
    "I luv this movie sooo much!!! ❤️",
    "gud mrng!!! hv a gr8 day 😊",
    "this is awsm!!! totally worth it 👍",
    "omg!!! this is lit 🔥🔥",
    "plz send me d notes asap",
    "idk what u mean 🤔",
    "thnx for ur help!! 😊",
    "cant waittt for d party 🎉",
    "yesss!!! finally done 😎",
    "this place is sooo coool 😍",
    "wtf was that 😡",
    "hahaha lol 😂😂",
    "brb will msg u later",
    "okiee see u soon 👋",
    "dis is nt gud at all",
    "feeling happiee today 😊",
    "sooo tired rn 😴",
    "gr8 job dude 👍",
    "luv u all ❤️"
]

print("---- Text Challenges ----\n")

for s in sentences:
    print("Sentence:", s)
    print("Issues: slang / emojis / typos present")
    print("Preprocessing Needed: remove emojis, correct spelling, normalize text\n")