from app import app, db, User
import unittest


class UserTests(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/test_db'
        db.create_all()
        user1 = User(
            username="user1",
            password="aaaaaa",
            location="sdada",
            email="dsadsa@gmail.com",
            bio="dsada",
            image_url="www.google.com/23131.jpg",
            header_image_url="dsasdadsa")
        # user2 = User(username="user2", password="aaaaaa")
        # user3 = User(username="user3", password="aaaaaa")
        db.session.add(user1)
        db.session.commit()

    def tearDown(self):
        db.session.close()
        db.drop_all()

    def test_login(self):
        client = app.test_client()
        response = client.post(
            "/login",
            data=dict(username="user1", password="aaaaaa"),
            follow_redirects=True)
        self.assertIn(b'Message', response.data)

    def test_logout(self):
        client = app.test_client()
        response = client.get("/logout")
        self.assertEqual(response.status_code, 302)


if __name__ == '__main__':
    unittest.main()
