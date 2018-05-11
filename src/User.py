class User(ABC):
	def __init__(self,id,name,location,password):
		self._id = id
		self._name = name
		self._location = location
		self._password = password
	@property
	def get_user_id(self):
		return self._id
	@property
	def get_user_name(self):
		return self._name
	@property
	def get_user_location(self):
		return self._location


class Company(User):
	def __init__(self,id,name,location,password):
		super().__init__(id,name,location,password)
class Individual(User):
	def __init__(self,id,name,location,star,streak,password):
		super().__init__(id,name,location,password)
		self._star = star
		self._streak = streak

	
	
		
		

