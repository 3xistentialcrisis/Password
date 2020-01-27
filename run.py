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

    gen_password = Credential.generate_new_password()

    return gen_password

#Log-in Feature
def log_in(username,password):
    """
    This function enables users to login to their password locker account

    Args:
        username : This is the user's name on the password locker platform/account
        password : This is the password locker password chosen by the user 
    """
    log_in = User.log_in(username, password)
    if log_in != False:
        return User.log_in(username, password)

# ------------------------------------->
def main():
    """
    This function runs the password locker application
    """

    print("Welcome to the Password Locker Application!\n")

    while True:
        print("""Use the following short codes: \n
        ac - Create your Password Locker account \n
        lg - Login to your Password Locker account \n
        du - Display User Accounts \n
        nc - Create New Credential \n
        gp - Generate New Password \n

        """)

        print(" ")

        #User Inputs their short code
        short_code = input("Enter : ").lower().strip()

        #Create & Save Password Locker User A/C
        if short_code == "ac":
            print("\n")
            print("To create a new password locker account:")
            fname = input("Enter your first name:")
            username = input("Enter your username:")
            password = input("Enter your password:")

            save_users = (User(fname, username,password))

            print(save_users + "\n" + "congratulations! You have succesfully created your account")

        #Login into Password Locker User A/C
        elif short_code == "lg":
            print("Log into your Password Locker Account")
            username = input("Enter your username:")
            password = input("Enter your password:")

            if log_in(username,password):
                print(log_in + "Welcome to your password locker account")
                
            else:
                print("Please use shortcode lg to input your login details again")      
        
        #Display User Account
        elif short_code == "du":
            print("\n")
            
            display_users = User.display_users()
            print(display_users)

        # else:
        #     print("")
        #     print("You have not yet created your user account")

        #Create a New Credential
        elif short_code == "nc":
            print("Add a new credential to your password locker account")
            print("\n")

            cred_account = input("Enter the credential name e.g. Facebook, Gmail")
            cred_username = input("Enter your credential username:")
            cred_password = input("Enter your credential password:")

            save_new_credential = (cred_account,cred_username,cred_password)
            print(save_new_credential)
            print("\n")
            print("Your credentials for {cred_username} have been saved")

        #Display New Credential w/ password
        elif short_code == "dc":
            for Credential in display_new_credentials(cred_account):
                print(f"Username is {Credential.cred_username}")
                print("\n")
                print(f"Password is {Credential.cred_password}")
        
        elif short_code == "gp":
            print("Please enter the name of the credential that you would like to generate a password")
            cred_account = input()

            #Update Credential with new password
            print("Your new credential password has been saved")
            print(create_new_password(cred_password))
            # save_new_credential = (Credential(cred_account,cred_password,cred_username, (create_new_password(cred_username)))
            
if __name__ == '__main__':
    main()