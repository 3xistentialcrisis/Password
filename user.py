class User:
    """
    Class that shall generate new instances of user accounts.
    """

    #User Details Array 
    user_details = []

    def __init__(self,account_name,username,password,confirm_password):
        """
        This __init__ method defines the properties of the User object

        Args:
            account_name : name of account in use
            username : associated with the user's account
            password : user's password
            confirm_password : confirm user's password

        """

        self.account_name = account_name
        self.username = username
        self.password = password
        self.confirm_password = confirm_password

    def save_user(self):
        """
        This is a method that saves a user to the user_details array
        """
        User.user_details.append(self)