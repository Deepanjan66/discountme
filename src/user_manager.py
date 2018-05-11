from src.User import User

class User_manager:
	def __init__(self):
		self._userList = []
		self._companyList = []

	def add_user(self,User):
		if User.is_company():
			self._companyList.append(User)
		else:
			self._userList.append(User)
	def rate_user(self,User,rating):
		User.add_rating(rating)

	
