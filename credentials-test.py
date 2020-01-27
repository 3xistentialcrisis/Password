import unittest
from credentials import Credential

class TestCredential(unittest.TestCase):
    """
    Test Class which defines test cases for the Credential Class 

    Args:
        unittest.TestCase : Test case class used to create test cases
    """

    def setUp(self):
        """
        This setUp method runs before each test case
        """

        #Credential Object
        self.new_cred = Credential("mary","gmail","batwoman","bat") 

        #Credential Details Array
        Credential.credential_details = []

    def tearDown(self):
        """
        This tearDown method cleans up after each test case is run
        """

    #Test Cases
    
    def test_init(self):
        """
        This test case tests if the Credential Object is initialised correctly
        """

        self.assertEqual( self.new_cred.fname, "mary")
        self.assertEqual( self.new_cred.cred_account, "gmail")
        self.assertEqual( self.new_cred.cred_username, "batwoman")
        self.assertEqual( self.new_cred.cred_password, "bats")

    def test_save_new_credential(self):
        """
        This test case tests if the newly created credential is saved into the credential_details array
        """

        self.new_cred.save_new_credential()
        self.assertEqual(len(Credential.credential_details),1)

    def test_display_new_credential(self):
        """
        This test case tests if all the created credentials are displayed to the user
        """

        # self.new_cred.save_new_credential()
        # self.assertEqual(len(Credential.display_new_credentials))
    
    def test_generate_new_password(self):
        """
        This test case tests if the user can generate their own random password
        """

        gen_password = self.new_cred.generate_new_password()
        self.assertEqual(len(gen_password),10)

if __name__ == '__main__':
    unittest.main()