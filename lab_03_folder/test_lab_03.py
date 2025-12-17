import unittest
from student import Student
from studentlist import StudentList

class TestStudentSystem(unittest.TestCase):

    def setUp(self):
        self.group_list = StudentList()

    def test_add_student(self):
        self.group_list.add_student("Bob", "0631112233", "bob@test.com", "kb-241")
        
        all_students = self.group_list.get_all()

        self.assertEqual(len(all_students), 1)

        added_student = all_students[0]
        self.assertIsInstance(added_student, Student) 
        self.assertEqual(added_student.name, "Bob")
        self.assertEqual(added_student.phone, "0631112233")
        self.assertEqual(added_student.email, "bob@test.com")
        self.assertEqual(added_student.group, "kb-241")

    def test_delete_student(self):

        self.group_list.add_student("Zak", "0634445566", "zak@test.com", "KB-242")
        
        result = self.group_list.delete_student("Zak")
        
        self.assertTrue(result)
        
        self.assertEqual(len(self.group_list.get_all()), 0)

    def test_delete_student_not_exists(self):
        self.group_list.add_student("Emma", "0632223344", "emma@test.com", "KB-241")
        
        initial_count = len(self.group_list.get_all())
        
        result = self.group_list.delete_student("Sasha")
        
        self.assertFalse(result)

        self.assertEqual(len(self.group_list.get_all()), initial_count)

    def test_sorting_logic(self):
        self.group_list.add_student("Zak", "1", "1", "1")
        self.group_list.add_student("Alex", "2", "2", "2")
        
        self.assertEqual(self.group_list.get_all()[0].name, "Alex")

if __name__ == '__main__':
    unittest.main()