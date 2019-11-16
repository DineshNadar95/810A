from HW11_Dinesh_Nadar import Repository, Student, Instructor, Major
import sqlite3
import unittest


class TestCollege(unittest.TestCase):
    def test_college1(self):
        """Test for student and instructor values"""
        directory = "E:\Assgnments\SSW 10\HomeWork11"
        db_directory = 'E:\Assgnments\SSW 10\HomeWork11\810_HW11.db'
        college1 = Repository(directory,db_directory)
        db_con = sqlite3.connect(db_directory)
        expected_students = [['10103', 'Jobs, S', 'SFEN', ['CS 501', 'SSW 810'], {'SSW 555', 'SSW 540'}, None], ['10115', 'Bezos, J', 'SFEN', ['SSW 810'], {'SSW 555', 'SSW 540'}, {'CS 546', 'CS 501'}], ['10183', 'Musk, E', 'SFEN', ['SSW 555', 'SSW 810'], {'SSW 540'}, {'CS 546', 'CS 501'}], ['11714', 'Gates, B', 'CS', ['CS 546', 'CS 570', 'SSW 810'], set(), None]]

        expected_instructors = [['98764', 'Cohen, R', 'SFEN', 'CS 546', 1], ['98763', 'Rowland, J', 'SFEN', 'SSW 810', 4], ['98763', 'Rowland, J', 'SFEN', 'SSW 555', 1], ['98762', 'Hawking, S', 'CS', 'CS 501', 1], ['98762', 'Hawking, S', 'CS', 'CS 546', 1], ['98762', 'Hawking, S', 'CS', 'CS 570', 1]]

        expected_majors = [['SFEN', {'SSW 555', 'SSW 810', 'SSW 540'}, {'CS 501', 'CS 546'}], ['CS', {'CS 570', 'CS 546'}, {'SSW 565', 'SSW 810'}]]

        expected_instructors_db =[('98763', 'Rowland, J', 'SFEN', 'SSW 810', 4), ('98763', 'Rowland, J', 'SFEN', 'SSW 810', 2), ('98762', 'Hawking, S', 'CS', 'CS 501', 1), ('98763', 'Rowland, J', 'SFEN', 'SSW 810', 1), ('98762', 'Hawking, S', 'CS', 'CS 546', 1)]

        students = [student_list.student_table()
                    for student_list in college1._students.values()]
        self.assertEqual(students, expected_students)

        instructors = [row for instructor_list in college1._instructors.values(
        ) for row in instructor_list.instructor_table()]
        self.assertEqual(instructors, expected_instructors)
        
        majors = [major.major_table() for major in college1._majors.values()]
        self.assertEqual(majors, expected_majors)
        
        q = """ select instructors.CWID,instructors.Name,instructors.Dept,grades.Course,count(grades.Course) from instructors  join grades on CWID = InstructorCWID
                group by Grade; """
        instructors_db = [row for row in db_con.execute(q)]
        self.assertEqual(instructors_db, expected_instructors_db)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
