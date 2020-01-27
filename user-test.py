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
        self.new_user = User("instagram","mary","cat","cat") 

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

        self.assertEqual(self.new_user.account_name,"instagram")
        self.assertEqual( self.new_user.username, "mary" )
        self.assertEqual( self.new_user.password, "cat" )
        self.assertEqual( self.new_user.confirm_password, "cat" )
    
    def test_save_user(self):
        """
        This test case tests if the user object is saved in the user_details array
        """

        self.new_user.save_user()
        self.assertEqual(len(User.user_details),1)

if __name__ == '__main__':
    unittest.main()