from app import app
import unittest
import os
import tempfile

class BasicTestCase(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type="html/text")
        self.assertEqual(response.status_code, 404)
        #self.assertEqual(response.data, b"Hello World!")


    def test_database(self):
        tester = os.path.exists("flaskr.db")
        self.assertTrue(tester)


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        """ Setup a blank temp database before each test """
        self.db_fd, app.app.config['DATABASE'] = tempfile.mkstemp()
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()
        app.init_db()

    def tearDown(self):
        """Destroy blank temp db after each test"""
        os.close(self.db_fd)
        os.unlink(app.app.config['DATABASE'])
    
    def login(


if __name__ == '__main__':
    unittest.main()


