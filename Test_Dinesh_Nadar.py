from HW10_Dinesh_Nadar import Repository, Student, Instructor,Major
import unittest


class TestCollege(unittest.TestCase):
    def test_college1(self):
        """Test for student and instructor values"""
        directory = "C:\Dinesh\Assgnments\SSW 10\HomeWork10"
        college1 = Repository(directory)
        expected_students = [['10103', 'Baldwin, C', 'SFEN', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687'], {'SSW 540', 'SSW 555'}, None], ['10115', 
'Wyatt, X', 'SFEN', ['CS 545', 'SSW 567', 'SSW 687'], {'SSW 540', 'SSW 555', 'SSW 564'}, None], ['10172', 'Forbes, I', 'SFEN', ['SSW 555', 'SSW 567'], {'SSW 540', 'SSW 564'}, {'CS 501', 'CS 545', 'CS 513'}], ['10175', 'Erickson, D', 'SFEN', ['SSW 564', 'SSW 567', 'SSW 687'], {'SSW 540', 'SSW 555'}, {'CS 501', 'CS 545', 'CS 513'}], ['10183', 'Chapman, O', 'SFEN', ['SSW 689'], {'SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'}, {'CS 501', 'CS 545', 'CS 513'}], ['11399', 'Cordova, I', 'SYEN', ['SSW 540'], {'SYS 671', 'SYS 800', 'SYS 612'}, None], ['11461', 'Wright, U', 'SYEN', ['SYS 611', 'SYS 750', 'SYS 800'], {'SYS 671', 'SYS 612'}, {'SSW 540', 'SSW 810', 'SSW 565'}], ['11658', 'Kelly, P', 'SYEN', [], {'SYS 671', 'SYS 800', 'SYS 612'}, {'SSW 540', 'SSW 810', 'SSW 565'}], ['11714', 'Morton, A', 'SYEN', ['SYS 611', 'SYS 645'], {'SYS 671', 'SYS 800', 'SYS 612'}, {'SSW 540', 'SSW 810', 'SSW 565'}], ['11788', 'Fuller, E', 'SYEN', ['SSW 540'], {'SYS 671', 'SYS 800', 'SYS 612'}, None]]
                             

        expected_instructors = [['98765', 'Einstein, A', 'SFEN', 'SSW 567', 4], ['98765', 'Einstein, A', 'SFEN', 'SSW 540', 3], ['98764', 'Feynman, R', 'SFEN', 'SSW 564', 3], ['98764', 'Feynman, R', 'SFEN', 'SSW 687', 3], ['98764', 'Feynman, R', 'SFEN', 'CS 501', 1], ['98764', 'Feynman, R', 'SFEN', 'CS 545', 1], ['98763', 'Newton, I', 'SFEN', 'SSW 555', 1], ['98763', 'Newton, I', 'SFEN', 'SSW 689', 1], ['98760', 'Darwin, C', 'SYEN', 'SYS 800', 1], ['98760', 'Darwin, C', 'SYEN', 'SYS 750', 1], ['98760', 'Darwin, C', 'SYEN', 'SYS 611', 2], ['98760', 'Darwin, C', 'SYEN', 'SYS 645', 1]]

        expected_majors = [['SFEN', {'SSW 567', 'SSW 564', 'SSW 540', 'SSW 555'}, {'CS 501', 'CS 545', 'CS 513'}], ['SYEN', {'SYS 671', 'SYS 612', 'SYS 800'}, {'SSW 540', 'SSW 565', 'SSW 810'}]]
        
        students = [student_list.student_table() for student_list in college1._students.values()]
        
        self.assertEqual(students, expected_students)
        instructors = [row for instructor_list in college1._instructors.values() for row in instructor_list.instructor_table()]
        
        self.assertEqual(instructors, expected_instructors)
        majors = [major.major_table() for major in college1._majors.values()]
        
        self.assertEqual(majors,expected_majors)
        
if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
