import json


def calculate_average_and_deviation(students):
  """
  Calculates the average grade for each student, subject, and overall, as well as the standard deviation of grades.

  Args:
    students: A list of JSON objects representing student data.

  Returns:
    A dictionary containing the following information:
      - average_grades: A list of floats representing the average grade for each student.
      - average_subjects: A list of floats representing the average grade for each subject across all students.
      - overall_average: A float representing the overall average grade across all students.
      - std_deviation: A float representing the standard deviation of grades across all students.
  """

  # Initialize variables
  student_grades = []
  subject_grades = {subject: [] for subject in set(grade["subject"] for student in students for grade in student["grades"])}
  all_grades = []

  # Iterate through students and collect grades
  for student in students:
    student_average = sum(grade["grade"] for grade in student["grades"]) / len(student["grades"])
    student_grades.append(student_average)
    for grade in student["grades"]:
      subject_grades[grade["subject"]].append(grade["grade"])
      all_grades.append(grade["grade"])

  # Calculate average grades for each subject and overall
  average_subjects = [sum(grades) / len(grades) for grades in subject_grades.values()]
  overall_average = sum(all_grades) / len(all_grades)

  # Calculate standard deviation
  from statistics import stdev
  std_deviation = stdev(all_grades)

  # Return results
  return {
      "average_grades": student_grades,
      "average_subjects": average_subjects,
      "overall_average": overall_average,
      "std_deviation": std_deviation,
  }


# Example usage
students = [
  {
    "name": "John Doe",
    "grades": [
      {"subject": "Math", "grade": 90},
      {"subject": "English", "grade": 85},
      {"subject": "Science", "grade": 92},
      {"subject": "History", "grade": 88},
      {"subject": "Art", "grade": 95},
    ]
  },
  {
    "name": "Jane Doe",
    "grades": [
      {"subject": "Math", "grade": 88},
      {"subject": "English", "grade": 92},
      {"subject": "Science", "grade": 85},
      {"subject": "History", "grade": 95},
      {"subject": "Art", "grade": 90},
    ]
  },
]

results = calculate_average_and_deviation(students)
print(results)