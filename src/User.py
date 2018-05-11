class User():
    def __init__(self, user_dict):
        self.id = user_dict['id']
        self.name = user_dict['name']
        self.location = user_dict['location']
        self.password = user_dict['password']
