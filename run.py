from user import User
from credentials import Credential


#Create User A/C
def create_user_account(fname,username,password):
    """
    This function creates the user account

    Args:
        fname : This is the user's real first name
        username : This is the user's name on the passworl locker platform/account
        password : This is the password locker password chosen by the user
    """

    new_user = User(fname,username,password) 

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


#New Credentials
def create_new_credential(fname,cred_account,cred_username,cred_password):
    """
    This function creates a new credential

    Args:
        fname : the user's real first name
        cred_account: name of new credential
        cred_username : username of the credential account
        cred_password : password of the credential account
    """
    new_cred = Credential(fname,cred_account,cred_username,cred_password)

    return new_cred

#Save New Credentials
def save_new_credential(Credential):
    """
    This function saves the newly created credential
    """

    Credential.save_new_credential()

#Display Created Credentials
def display_new_credentials(password):
    """
    This function displays all the created credentials
    """

    return Credential.display_new_credentials(password)

#Generate New Password
def create_new_password(cred_username):
    """
    This is a function that generates a new password for the user
    
    Args:
        cred_username: this is the username of the credential account
    """

    gen_password = Credential.generate_password()

    return gen_password



