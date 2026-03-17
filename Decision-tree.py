# Assignment (12/03/2026)
# Assignment Name: Decision Tree on Paper
# Description: Draw a decision tree predicting whether you should play outside

# Simple rule-based decision tree logic

weather = input("Enter weather (sunny/rainy/cloudy): ")
temperature = input("Enter temperature (hot/mild/cool): ")
humidity = input("Enter humidity (high/normal): ")

if weather == "rainy":
    print("Decision: Do NOT play outside.")
elif weather == "sunny" and humidity == "high":
    print("Decision: Do NOT play outside.")
else:
    print("Decision: You CAN play outside.")