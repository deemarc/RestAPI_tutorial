from user import User

# user = [
#     {
#     'id':1,
#         'username':'bob',
#         'password': 'asdf'
#     }
# ]
        
# users = [
#     User(1,'bob','asdf')
# ]

# {
#     'bob':{
#         'id':1,
#         'username':'bob',
#         'password': 'asdf'
#     }

# }
# username_mapping = {u.username: u for u in users}
# userid_mapping = {u.id: u for u in users}

# userid_mapping = {
#     1: {
#         'id':1,
#         'username':'bob', 
#         'password': 'asdf'
#     }
# }

def authenticate(username, password):
    # user = username_mapping.get(username, None
    user = User.find_by_username(username)
    if user and user.password == password:
        return user

def identity(payload):
    user_id = payload['identity']
    return User.find_by_id (user_id )