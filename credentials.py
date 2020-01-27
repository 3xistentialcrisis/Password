import string
from random import choice

class Credential:
    """
    Class that shall generate new instances of user credentials.
    """
    #Credentials details array
    credential_details = []

    def __init__(self,fname,cred_account,cred_username,cred_password):
        """
        This __init__ method defines the properties of the Credentials object

        Args:
            fname : the user's real first name
            cred_account: name of new credential
            cred_username : username of the credential account
            cred_password : password of the crential account

        """

        self.fname = fname
        self.cred_account = cred_account
        self.cred_username = cred_username
        self.cred_password = cred_password

    def save_new_credential(self):
        """
        This is a method that saves a new credential to the credential_details array
        """

        Credential.credential_details.append(self)

    @classmethod
    def display_new_credentials(cls, password):
        """
        This is a method that displays all the newly created credentials
        """
        #New credentials empty array
        all_credential_details = []

        for credential in cls.credential_details:
            if credential.cred_password == password:
                all_credential_details.append(credential)

        return all_credential_details
    
    @classmethod
    def generate_new_password(cls):
        """
        This method generates a random new mixed alphanumeric password
        """
        size = 10 #length of password

        alphanum = string.ascii_uppercase + string.digits + string.ascii_lowercase

        gen_password = ''.join( choice(alphanum) for num in range(size) )

        return gen_password