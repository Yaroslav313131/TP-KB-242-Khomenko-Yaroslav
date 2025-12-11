import unittest
import lab_02 

class TestStudentSystem(unittest.TestCase):

    def setUp(self):
        self.list = []

    def test_add_student(self):
        
        expected_student = {
            "name": "Bob",
            "phone": "0631112233",
            "email": "bob@test.com",
            "group": "kb-241"
        }

        lab_02.add_student(
            self.list, 
            "Bob", 
            "0631112233",
            "bob@test.com", 
            "kb-241"
        )
        
    
        # 1. Перевірка кількості елементів
        self.assertEqual(len(self.list), 1)
        # 2. Перевірка, що доданий елемент відповідає очікуваному
        self.assertEqual(self.list[0], expected_student)

    def test_delete_student(self):

        self.list = [{
            "name": "Zak", 
            "phone": "0634445566",
            "email": "zak@test.com", 
            "group": "KB-242"
        }]
        
        result = lab_02.delete_student(self.list, "Zak")
        
        # 1. Перевірка, чи функція повернула True
        self.assertTrue(result)
        
        # 2. Перевірка, чи список став порожнім
        self.assertEqual(len(self.list), 0)

    def test_delete_student_not_exists(self):
        # 3 Перевірка, що неіснуючий студент не видаляється.
        
        self.list = [{
            "name": "Emma", 
            "phone": "0632223344",
            "email": "emma@test.com", 
            "group": "KB-241"
        }]
        
        initial_count = len(self.list)
        
        # Намагаємося видалити неіснуючого студента
        result = lab_02.delete_student(self.list, "Sasha")
        
        # 1. Перевірка, чи функція повернула False
        self.assertFalse(result)
        
        # 2. Перевірка, що список залишився без змін
        self.assertEqual(len(self.list), initial_count)


if __name__ == '__main__':
    unittest.main()