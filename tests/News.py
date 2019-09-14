import unittest
from app.models import News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News(null,'Bitcoin to Boom As Macroeconomic Backdrop Worsens; Here’s Why','For most of its life, Bitcoin (BTC) was seen as a volatile gamble that was most likely to fail. Just look to the countless obituaries detailing the “death” of the cryptocurrency on this site. But, this narrative has started to change. Year to date','\r\n')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))