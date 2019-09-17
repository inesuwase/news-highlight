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


class Articles:
    '''
    Articles class to define news oblects
    '''
    def __init__(self,id,name,author,title,description,url,urlToImage,publishedAt):
         self.id = id
         self.name = name
         self.author = author
         self.title = title
         self.description = description
         self.url = url
         self.urlToImage = urlToImage
         self.publishedAt = publishedAt