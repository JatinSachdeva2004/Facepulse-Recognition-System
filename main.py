
import csv
import os
from collections import defaultdict

    def mark_attendance(self, subject, student_name, picture_count):
        self.attendance_records[subject].append((student_name, picture_count))

    def calculate_attendance(self):
        attendance_summary = defaultdict(dict)

        for subject, records in self.attendance_records.items():
            total_classes = len(records)
            present_count = sum(1 for _, count in records if count == 2)
            absent_count = total_classes - present_count
            attendance_percentage = (present_count / total_classes) * 100 if total_classes != 0 else 0

            attendance_summary[subject]['Total Classes'] = total_classes
            attendance_summary[subject]['Present'] = present_count
            attendance_summary[subject]['Absent'] = absent_count
            attendance_summary[subject]['Percentage'] = attendance_percentage

        return attendance_summary


# Example usage:
if __name__ == "__main__":
    # Initialize the smart attendance system
    attendance_system = SmartAttendanceSystem()



    # Calculate and display attendance summary
    attendance_summary = attendance_system.calculate_attendance()
    print("\nAttendance Summary:")
    for subject, summary in attendance_summary.items():
        print(f"Subject: {subject}")
        print(f"Total Classes: {summary['Total Classes']}")
        print(f"Present: {summary['Present']}")
        print(f"Absent: {summary['Absent']}")
        print(f"Percentage: {summary['Percentage']:.2f}%")
        print()
