class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,id,title,overview,poster):
        self.id =id
        self.title = title
        self.overview = overview
        self.poster = "https://www.newsbtc.com/wp-content/uploads/2019/09/shutterstock_387276601-1200x780.jpg" + poster



class Review:

    all_reviews = []

    def __init__(self,news_id,title,imageurl,review):
        self.news_id = news_id
        self.title = title
        self.imageurl = imageurl
        self.review = review


    def save_review(self):
        Review.all_reviews.append(self)


    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

    @classmethod
    def get_reviews(cls,id):

        response = []

        for review in cls.all_reviews:
            if review.news_id == id:
                response.append(review)

        return response