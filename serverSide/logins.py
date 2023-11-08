import requests
from flask import request, Flask

app = Flask(__name__)

#database of private keys
passport = dict(user='private_key', user1='private_key_1')


'''
NICKNAME = input("nickname")
PASSWORD = input("password")
'''

# encryption model


def encrypt(nickname, password):
  encrypted_nickname = ""
  encrypted_password = ""
  for char in nickname:
    encrypted_char = chr(ord(char) + 3)
    encrypted_nickname += encrypted_char
  for char in password:
    encrypted_char = chr(ord(char) + 3)
    encrypted_password += encrypted_char
    private_key: True = encrypted_nickname + encrypted_password
  return private_key

def login(private_key: object) -> object:
  if private_key in passport.values():
    return "Access Granted"
  else:
    return "Access Denied"

  @app.route('/login', methods=['GET'])
  def login_route():
    nickname = request.get('nickname')
    password = request.get('password')
    private_key = encrypt(nickname, password)
    return login(private_key)

if __name__ == '__main__':
  app.run(debug=True)


''' 
  if model is true, then let client access to the server
  '''


#I am going to create an encryption model for passports

"""""
I will combine the names and passwords in a static model
which of the outputs will be the private keys to access if
the passwords and nicknames are correct.
this is how one is to access server.
#! if one of the names or passwords are incorrect, no entrance.
"""


