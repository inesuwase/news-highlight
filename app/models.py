class Sources:
    '''
    Sources class to define news Objects
    '''

    def __init__(self, id,name,description,url,category):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category


# class Review:

#    	'''
# 	Review Class to define Review Objects
# 	'''
# 	def __init__(self,author,title,description,url,image,date):
# 		'''
# 		Function to initialize Review Objects
# 		It defines the properties each Review object will hold.
	
# 		Args: 
# 			1. author
# 			2. title
# 			3. description
# 			4. url
# 			5. image
# 			6. date
# 		'''
# 		self.author = author
# 		self.title = title
# 		self.description = description
# 		self.url = url
# 		self.image = image
#         self.date = date