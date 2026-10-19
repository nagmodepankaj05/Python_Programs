marks = {
    "Maths": 80,
    "English": 75,
    "Science": 90
}

high = max(marks, key=marks.get)

print("Highest marks :", high)
print("Marks:", marks[high])