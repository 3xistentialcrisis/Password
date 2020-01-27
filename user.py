class User:
    """
    Class that shall generate new instances of user accounts.
    """

    #User Details Array 
    user_details = []

    def __init__(self,account_name,username,user_password,confirm_password):
        """
        This __init__ method defines the properties of the User object
        """

        self.account_name = account_name
        self.username = username
        self.user_password = user_password
        self.confirm_password = confirm_password