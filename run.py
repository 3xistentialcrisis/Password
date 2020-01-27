from user import User
from credentials import Credential


#Create User A/C
def create_user_account(fname,username,password,confirm_password):
    """
    This function creates the user account

    Args:
        fname : This is the user's real first name
        username : This is the user's name on the platform/account
        password : This is the password chosen by the user
        confirm_password : This confirms the user's password
    """

    new_user = User(fname,username,password,confirm_password) 

    return new_user

#Save User A/C
def save_users(user):
    """
    This function saves the user account

    Args:
        user: This is the user whose account shall be saved
    """

    user.save_user()

#Display User A/Cs
def display_users():
    """
    This function displays all the created user accounts
    """
    return User.display_users()


