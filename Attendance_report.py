from google.colab import files
import csv

def mark_attendance():
  """
  This function prompts the teacher to enter student data (if not already saved)
  and then allows marking attendance (absent or present) for existing students.

  Student data is saved to a file named 'student_data.csv' in the Colab runtime.
  """

  # Check if student data file exists
  student_data = []
  try:
    with open('student_data.csv', 'r') as csvfile:
      reader = csv.reader(csvfile)
      student_data = list(reader)
  except FileNotFoundError:
    print("Student data file not found. Please enter student details first.")
    # Get student data (name and section) from the teacher
    while True:
      student_name = input("Enter student name (or 'q' to quit): ").strip()
      if student_name.lower() == 'q':
        break
      student_section = input("Enter student section: ").strip()
      new_student_data = [student_name, student_section]
      student_data.append(new_student_data)

    # Save student data to file
    with open('student_data.csv', 'w', newline='') as csvfile:
      writer = csv.writer(csvfile)
      writer.writerows(student_data)
      print("Student data saved successfully.")

  # Mark attendance for existing students
  if student_data:
    student_name = input("Enter student name for attendance (or 'q' to quit): ").strip()
    while student_name.lower() != 'q':
      student_found = False
      for i, row in enumerate(student_data):
        if row[0].lower() == student_name.lower():
          student_found = True
          attendance = input("Mark attendance (present/absent): ").strip().lower()
          if attendance in ['present', 'absent']:
            row.append(attendance)
            student_data[i] = row
            print(f"Attendance marked for {student_name}.")
          else:
            print("Invalid attendance status. Please enter 'present' or 'absent'.")
          break

      if not student_found:
        print(f"Student {student_name} not found in the list.")

      student_name = input("Enter student name for attendance (or 'q' to quit): ").strip()

    # Save updated student data with attendance marks
    with open('student_data.csv', 'w', newline='') as csvfile:
      writer = csv.writer(csvfile)
      writer.writerows(student_data)

if __name__ == "__main__":
  mark_attendance()

