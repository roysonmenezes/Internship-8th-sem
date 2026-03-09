# Assignment (28/02/2026)
# Assignment Name : Storytelling with Graphs Description : Create bar chart, pie chart, histogram and write a short data story explaining trends..



import matplotlib.pyplot as plt

# Sample dataset (students marks)
subjects = ["Maths", "Science", "English", "Computer", "History"]
marks = [85, 90, 78, 95, 70]

# Bar Chart
plt.bar(subjects, marks)
plt.title("Marks Distribution (Bar Chart)")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

# Pie Chart
plt.pie(marks, labels=subjects, autopct='%1.1f%%')
plt.title("Marks Distribution (Pie Chart)")
plt.show()

# Histogram
data = [85, 90, 78, 95, 70, 88, 92, 76, 84, 89]

plt.hist(data, bins=5)
plt.title("Marks Frequency Distribution (Histogram)")
plt.xlabel("Marks Range")
plt.ylabel("Frequency")
plt.show()