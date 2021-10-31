import unittest
from models import article
Article = article.Article

class ArticleTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the Article class
    '''
    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_article = Article(self,'William Keegan','Johnson’s foreign quarrels can’t conceal the truth about Brexit','Fishing rows notwithstanding, much of Europe looks on at the UK’s plight with astonishment – and even, still, sympathyAt the recent celebration of the life and achievements of my friend and fellow Remainer John le Carré, I was asked by a leading academic whet…','https://amp.theguardian.com/business/2021/oct/31/johnsons-foreign-quarrels-cant-conceal-the-truth-about-brexit','https://i.guim.co.uk/img/media/5d53d6fc6963868c7a0567d624a08e237cf56985/0_412_8192_4915/master/8192.jpg?width=1200&height=630&quality=85&auto=format&fit=crop&overlay-align=bottom%2Cleft&overlay-width=100p&overlay-base64=L2ltZy9zdGF0aWMvb3ZlcmxheXMvdG8tb3BpbmlvbnMucG5n&enable=upscale&s=2a2abf09964c1b2733b4ea0d8af9c904',"2021-10-31T07:00:21Z","At the recent celebration of the life and achievements of my friend and fellow Remainer John le Carré, I was asked by a leading academic whether I was absolutely certain that we could rejoin the Euro… [+4510 chars]")