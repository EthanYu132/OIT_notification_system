import requests

login_url = 'https://help.rice.edu/'

# login_data = {
#     'username' : ####
#     'password' : ####
# }

# main function for this script
def main():
    OAuth()
    return None

# function for Oauth
def OAuth():    
    
    responseBool1 = requests.get("site")
    response = requests.post("site", auth = ("user","pass%"))

    print(print("Login No work") if responseBool1.text == response.text else print("Login worked"))

    #print(response.text)

    # return print(isDiffPage)
    

main()