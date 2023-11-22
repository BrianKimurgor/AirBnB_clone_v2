import unittest
import MySQLdb
from console import HBNBCommand
import io
from unittest.mock import patch
from os import getenv
from models.engine.db_storage import DBStorage


@unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', "Not DBStorage")
class TestMySQL(unittest.TestCase):
    """Test for the sql database"""

    conn = None
    curr = None

    def setUp(self):
        """Connecting mysqldb"""
        self.conn = MySQLdb.connect(
            host=getenv('HBNB_MYSQL_HOST'),
            user=getenv('HBNB_MYSQL_USER'),
            passwd=getenv('HBNB_MYSQL_PASSWORD'),
            db=getenv('HBNB_MYSQL_DB'),
        )
        self.curr = self.conn.cursor()

    def tearDown(self):
        """ Disconnect from mysqldb"""
        self.curr.close()
        self.conn.close()
        self.conn = None
        self.curr = None

    def test_create_state(self):
        """Test create state"""

        self.setUp()
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create State name="California"')
            self.curr.execute("SELECT COUNT(*) FROM states")
            result = self.curr.fetchone()[0]
            self.assertEqual(result, 1)
            self.tearDown()

    def test_create_city(self):
        """Test create city"""

        self.setUp()
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd('create State name="California"')
        id = f.getvalue()[:1]
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd(f'''create City state_id="{id}"
                                 name="San_Francisco"''')
            self.curr.execute("SELECT COUNT(*) FROM cities")
            result = self.curr.fetchone()[0]
            self.assertEqual(result, 1)
            self.tearDown()


if __name__ == '__main__':
    unittest.main()
