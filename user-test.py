import unittest
from user import User

class TestUser(unittest.TestCase):
    """
    Test Class which defines test cases for the User Class Behaviours

    Args:
        unittest.TestCase : Test case class used to create test cases
    """

    def setUp(self):
        """
        This setUp method runs before each test case
        """

        #User Object
        self.new_user = User("mary","catwoman","cat") 

        #User Details Array
        User.user_details = []

    def tearDown(self):
        """
        This tearDown method cleans up after each test case is run
        """

    #Test Cases 

    def test_init(self):
        """
        This test case tests if the User object is initialised properly
        """

        self.assertEqual( self.new_user.fname,"mary")
        self.assertEqual( self.new_user.username, "catwoman" )
        self.assertEqual( self.new_user.password, "cat" )
    
    def test_save_user(self):
        """
        This test case tests if the user object is saved in the user_details array
        """

        self.new_user.save_user()
        self.assertEqual(len(User.user_details),1)

    def test_display_users(self):
        """
        This test case tests if the details of all user accounts created is displayed
        """

        self.assertEqual(User.display_users(), User.user_details)

if __name__ == '__main__':
    unittest.main()