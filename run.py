from user import User

def create_user_account(account_name,username,password,confirm_password):
    """
    This function creates the user account

    Args:
        account_name : This is the platform on which the user creates their account
        username : This is the user's name on the platform/account
        password : This is the password chosen by the user
        confirm_password : This confirms the user's password
    """

    new_user = User(account_name,username,password,confirm_password) 

    return new_user

def save_users(user):
    """
    This function saves the user account

    Args:
        user: This is the user whose account shall be saved
    """

    user.save_user()

    