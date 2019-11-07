from prettytable import PrettyTable
from collections import defaultdict
import os


class Student:
    """Class to handle student details"""

    def __init__(self, std_cwid, std_name, major):
        """initializing the student values"""
        self._std_cwid = std_cwid
        self._std_name = std_name
        self._major = major

        self._courses = dict()

    def add_course(self, course, grade):
        """adds course to the student dict"""
        self._courses[course] = grade

    def student_table(self):
        """creates a pretty table for student"""
        return[self._std_cwid, self._std_name, sorted(self._courses.keys())]


class Instructor:
    """Class to handle instructor details"""

    def __init__(self, in_cwid, in_name, dept):
        """initializing the student values"""
        self._in_cwid = in_cwid
        self._in_name = in_name
        self._dept = dept

        self._courses = defaultdict(int)

    def incr_student(self,course):
        """adds no of student attending the course"""
        self._courses[course] += 1

    def instructor_table(self):
        """creates a pretty table for instructor"""
        for course, count in self._courses.items():
            yield [self._in_cwid, self._in_name, self._dept, course, count]


def file_reading_gen(path, fields, sep, header):
    """ reading the file and creating the output as requested."""
    line_count = 0
    try:
        fp = open(path, 'r')
    except FileNotFoundError:
        raise("Error File not found", path)
    else:
        with fp:
            for line in fp:
                line_count = line_count+1
                f = line.strip('\n').split(sep)
                if len(f) != fields:
                    raise ValueError(
                        f"ValueError:{path} has {len(f)} fields on the line {line_count} but expected {fields}")
                else:
                    if header == False:
                        header = True
                    else:
                        yield(tuple(f))


class Repository:
    """This class handles all the data of studdent as well a instructor"""

    def __init__(self, directory):
        """ Initialize directory and dictionary """
        self._directory = directory
        self._students = dict()
        self._instructors = dict()
        self._retrive_students(os.path.join(self._directory, 'students.txt'))
        self._retrive_instructors(os.path.join(self._directory, 'instructors.txt'))
        self._retrive_grades(os.path.join(self._directory, 'grades.txt'))
        self.instructor_pretty_table()
        self.student_pretty_table()
        

    def _retrive_students(self,dir):
        """ Retrive values and create a proper dictionary for the pretty table """
        for cwid, name, major in file_reading_gen(dir, 3, sep='\t', header=True):
            self._students[cwid] = Student(cwid, name, major)
     

    def _retrive_instructors(self,dir):
        """ Retrive values and create a proper dictionary for the pretty table """ 
        for cwid, name, dept in file_reading_gen(dir, 3, sep='\t', header=True):
            self._instructors[cwid] = Instructor(cwid, name, dept)
   

    def _retrive_grades(self,dir):
        """ Retrive values and create a proper dictionary for the pretty table """
        for stu_cwid, course, grade, in_cwid in file_reading_gen(dir, 4, sep='\t', header=True):
            if stu_cwid in self._students:
                self._students[stu_cwid].add_course(course, grade)
            else:
                print(
                    f'This grade is for unknown Student whose id is {stu_cwid}')

            if in_cwid in self._instructors:
                self._instructors[in_cwid].incr_student(course)
            else:
                print(
                    f'This grade is for unknown instrcutor whose id is {in_cwid}')
         

    def student_pretty_table(self):
        """ Student Pretty table print """
        p = PrettyTable(field_names=['CWID', 'Name', 'Completed Courses'])
        for student in self._students.values():
            p.add_row(student.student_table())
        print(p)

    def instructor_pretty_table(self):
        """Instructor Pretty table print"""
        p = PrettyTable(
            field_names=['CWID', 'Name', 'Dept', 'Course', 'Students'])
        for instructor in self._instructors.values():
            for row in instructor.instructor_table():
                p.add_row(row)
        print(p)


def main():
    """ Main Function """
    directory = 'C:\Dinesh\Assgnments\SSW 10\HomeWork09'
    Repository(directory)
   
if __name__ == '__main__':
    """called main fucntion"""
    main()
