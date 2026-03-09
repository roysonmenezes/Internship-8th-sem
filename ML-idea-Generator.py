# Assignment (02/03/2026) 
# Assignment Name : ML Idea Generator Description : Suggest ML problems in college, healthcare, shopping and describe input → output.


# # ML Idea Generator
# Dictionary storing ML ideas
ml_ideas = {
    "College": {
        "Problem": "Student Performance Prediction",
        "Input": "Attendance, Previous Marks, Study Hours",
        "Output": "Predicted Final Grade"
    },

    "Healthcare": {
        "Problem": "Disease Risk Prediction",
        "Input": "Age, Medical History, Symptoms",
        "Output": "Probability of Disease"
    },

    "Shopping": {
        "Problem": "Product Recommendation System",
        "Input": "User Purchase History, Browsing Behavior",
        "Output": "Recommended Products"
    }
}

print("---- ML Idea Generator ----\n")

for domain, details in ml_ideas.items():
    print("Domain:", domain)
    print("ML Problem:", details["Problem"])
    print("Input:", details["Input"])
    print("Output:", details["Output"])
    print()