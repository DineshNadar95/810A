from HW09_Dinesh_Nadar import Repository, Student, Instructor
import unittest


class TestCollege(unittest.TestCase):
    def test_college1(self):
        """Test for student and instructor values"""
        directory = "C:\Dinesh\Assgnments\SSW 10\HomeWork09"
        college1 = Repository(directory)
        expected_students = [['10103', 'Baldwin, C', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687']], ['10115', 'Wyatt, X', ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687']], ['10172', 'Forbes, I', ['SSW 555', 'SSW 567']], ['10175', 'Erickson, D', ['SSW 564', 'SSW 567', 'SSW 687']], ['10183', 'Chapman, O', ['SSW 689']], ['11399', 'Cordova, I', ['SSW 540']], ['11461', 'Wright, U', ['SYS 611', 'SYS 750', 'SYS 800']], ['11658', 'Kelly, P', ['SSW 540']], ['11714', 'Morton, A', ['SYS 611', 'SYS 645']], ['11788', 'Fuller, E', ['SSW 540']]]
                             

        expected_instructors = [['98765', 'Einstein, A', 'SFEN', 'SSW 567', 4], ['98765', 'Einstein, A', 'SFEN', 'SSW 540', 3], ['98764', 'Feynman, R', 'SFEN', 'SSW 564', 3], ['98764', 'Feynman, R', 'SFEN', 'SSW 687', 3], ['98764', 'Feynman, R', 'SFEN', 'CS 501', 1], ['98764', 'Feynman, R', 'SFEN', 'CS 545', 1], ['98763', 'Newton, I', 'SFEN', 'SSW 555', 1], ['98763', 'Newton, I', 'SFEN', 'SSW 689', 1], ['98760', 'Darwin, C', 'SYEN', 'SYS 800', 1], ['98760', 'Darwin, C', 'SYEN', 'SYS 750', 1], ['98760', 'Darwin, C', 'SYEN', 'SYS 611', 2], ['98760', 'Darwin, C', 'SYEN', 'SYS 645', 1]]

        students = [student_list.student_table() for student_list in college1._students.values()]
        print(students)
        self.assertEqual(students, expected_students)
        instructors = [row for instructor_list in college1._instructors.values() for row in instructor_list.instructor_table()]
        self.assertEqual(instructors, expected_instructors)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
