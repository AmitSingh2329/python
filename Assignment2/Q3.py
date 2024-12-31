score = int(input("Enter the student's score (0-100): "))

if 90 <= score <= 100:
    grade = "A"
    comment = "Excellent"
elif 80 <= score < 90:
    grade = "B"
    comment = "Good"
elif 70 <= score < 80:
    grade = "C"
    comment = "Average"
elif 60 <= score < 70:
    grade = "D"
    comment = "Needs Improvement"
elif score < 60:
    grade = "F"
    comment = "Failing"
else:
    grade = None
    comment = "Invalid score"

# Output the result
if grade:
    print(f"Letter Grade: {grade}")
    print(f"Comment: {comment}")
else:
    print(comment)  # Invalid score message

