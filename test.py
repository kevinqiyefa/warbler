from app import app, db, User
import unittest


class UserTests(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/test_db'
        # app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False

        db.create_all()
        user1 = User(
            username='user111',
            password=User.hash_password('aaaaaa'),
            location="sdada",
            email="dsadsa@gmail.com",
            bio="dsada",
            image_url="www.google.com/23131.jpg",
            header_image_url="dsasdadsa")

        db.session.add(user1)
        db.session.commit()

    def tearDown(self):
        db.session.close()
        db.drop_all()

    def test_login(self):
        client = app.test_client()
        response = client.post(
            "/login",
            data=dict(username='user111', password='aaaaaa'),
            follow_redirects=True)

        self.assertIn(b'user111', response.data)

    def test_logout(self):
        client = app.test_client()

        response = client.post(
            "/login",
            data=dict(username='user111', password='aaaaaa'),
            follow_redirects=True)

        response = client.get('/logout', follow_redirects=True)

        self.assertIn(b'successfully', response.data)
        self.assertEqual(response.status_code, 200)

    def test_signup(self):
        client = app.test_client()
        headerurl = "https://blog.eat24.com/wp-content/uploads/2017/11/Criminal-Animals_header.jpg"
        imgurl = 'http://s11.favim.com/mini/170328/baby-animals-cats-cute-animals-kitten-Favim.com-5140341.jpeg'

        response = client.post(
            "/signup",
            data=dict(
                username="user2",
                password="123456",
                location="san francisco",
                email="test@gmail.com",
                bio="no story",
                image_url=imgurl,
                header_image_url=headerurl),
            follow_redirects=True)
        self.assertIn(b'@user2', response.data)

    def test_edit_profile(self):
        headerurl = "https://blog.eat24.com/wp-content/uploads/2017/11/Criminal-Animals_header.jpg"
        imgurl = 'http://s11.favim.com/mini/170328/baby-animals-cats-cute-animals-kitten-Favim.com-5140341.jpeg'

        client = app.test_client()

        response = client.post(
            "/login",
            data=dict(username='user111', password='aaaaaa'),
            follow_redirects=True)

        response = client.patch(
            "/users/1",
            data=dict(
                username="user2",
                password="aaaaaa",
                location="san francisco",
                email="test@gmail.com",
                bio="I have story now",
                image_url=imgurl,
                header_image_url=headerurl),
            follow_redirects=True)

        # self.assertEqual(response.status_code, 200)
        self.assertIn(b'I have story now', response.data)
        self.assertNotIn(b'no story', response.data)

    def test_404_html(self):
        client = app.test_client()
        response = client.get("/users/10000000000", follow_redirects=True)
        self.assertEqual(response.status_code, 404)

    def test_delete_user(self):
        client = app.test_client()

        response = client.post(
            "/login",
            data=dict(username='user111', password='aaaaaa'),
            follow_redirects=True)

        response = client.delete('/users/1', follow_redirects=True)

        self.assertIn(b'Join Warbler today.', response.data)
        self.assertEqual(200, response.status_code)

    def test_create_message(self):
        client = app.test_client()

        client.post(
            "/login",
            data=dict(username='user111', password='aaaaaa'),
            follow_redirects=True)

        response = client.post(
            "/users/1/messages",
            data=dict(text='user111', user_id=1),
            follow_redirects=True)

        self.assertIn(b'user111', response.data)


if __name__ == '__main__':
    unittest.main()
