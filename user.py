from credentials import Credential

#User Class
class User:
    """
    Class that shall generate new instances of user accounts.
    """

    #User Details Array 
    user_details = []

    def __init__(self,fname,username,password):
        """
        This __init__ method defines the properties of the User object

        Args:
            fname : the user's real first name
            username : associated with the user's account
            password : user's password
        """

        self.fname = fname
        self.username = username
        self.password = password

    def save_user(self):
        """
        This is a method that saves a user to the user_details array
        """
        User.user_details.append(self)
    
    @classmethod
    def display_users(cls):
        """
        This is a method that returns/displays the contents of the user_details array
        """
        return cls.user_details
    
    @classmethod
    def log_in(cls,username,password):
        """
        This is a method that enables users to login to their password locker account

        Args:
            username: user's password locker app username
            password: user's password locker app password
        """
        for User in cls.user_details:
            if User.username == username and User.password == password:
                return Credential.credential_details

        return False
        
