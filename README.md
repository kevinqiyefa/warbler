# Warbler

![Warbler Gif](warbler.gif)

A Twitter clone with a Rithm spin.

[Live site](https://warbler-app.herokuapp.com/)

### Installation

```sh
# make a virtual environment
mkvirtualenv warbler
# install python requirements
pip install -r requirements.txt

# set up database
dropdb warbler_db
createdb warbler_db
flask db upgrade

# The database must be freshly created before doing this command
# If you have already added data, make sure to follow the steps above
# to reset the database.
python seed.py

# start the server!
flask run
```

### Assignment

Try to understand the code. Look through and see what each route is doing. Take a look at the models. See what data you have in your database after running `python seed.py`.

When you're ready, address the following user stories:

1.  As a user, I want to see a custom 404 page when I try to go to an invalid URL.
1.  As a user, I want to see the location, bio, and my header image on a user's profile page. (Note: these fields already exist in the database, you just have to integrate them into the UI.)
1.  As a user, I want to see other users' bios and header images on the profile cards that appear on the following and follower pages, as well as in search results.
1.  As a user, I want to be able to edit my location, bio, and my header image on my profile edit page.
1.  As a user, I want to see the last 100 warbles **only from the users that I am following, and myself** rather than warbles from _all_ users.
1.  As a user, I want to be able to "like" a warble.
1.  As a user, I want to be able to see how many warbles I "liked" on my profile page.
1.  (_Technical_) - Add tests. Test features such as login, making sure you cannot edit someone else profile, etc. There is a sample test file [below](#appendix-test-example). You can also check out the [testing notes](https://github.com/rithmschool/python_curriculum/blob/master/Unit-02/08-testing_continued.md) in the python curriculum. To run the tests, `pip install green` then run `green` from the root of your project.

### Bonus

1.  As a user, I should not have to refresh the page when I like a warble.
1.  As a user, I should not have to refresh the page when I change my bio or name in my profile.
1.  As a user, I should not have to go to a new page to compose a warble (think modals and AJAX here!)
1.  (_Technical_) - Look for opportunities to refactor! In the templates especially, there are opportunities to DRY up the code.
1.  (_Technical_) - The application has an [n + 1 query](https://www.rithmschool.com/courses/flask-fundamentals/database-performance) issue. Set `app.config['SQLALCHEMY_ECHO'] = True` and try to fix the issue.

### Super Bonus

Fair warning: you won't have time to tackle all of these. Pick one or two that interest you!

1.  As a user, I should be able to send a direct message to another user which is only visible to the two of us.
1.  As a user, I should be able to respond to a direct message sent to me.
1.  As a user, I should be able to block another user, so that they are no longer visible to me and they cannot send me direct messages.
1.  As a user, I should be able to see a list of all of the users I've blocked.
1.  As a user, I should be able to unblock a user I've previously blocked.
1.  As an admin user, I should be able to delete anyone's messages.
1.  As an admin user, I should be able to delete users from the platform.
1.  As an admin user, I should be able to add or revoke admin privileges for any other user.

### Appendix: Seeding the DB

In the `generator` directory you'll see there are some Python files along with some CSVs. The `seed.py` file reads the CSV data in order to pre-populate the database. If you'd like to generate a new set of fake data, you can run

```sh
python generator/create_csvs.py
```

This will create a new set of fake data with which you can seed your database.

### Appendix: Testing

There are at LEAST two bugs in the application, but it's not necessarily obvious where it is (there's a hint at the bottom of the readme). This is why testing is so important!

Let's briefly discuss a couple of things related to tests: _how_ you should test, and _what_ you should test. First, let's talk about the how. You might organize your tests like this:

- test_user_model.py
- test_user_views.py
- test_message_model.py
- test_message_views.py

In this case, there are four test files: two for testing the models, and two for testing the routes/view-functions.

To run a file containing unittests, you can run the command `python -m unittest <name-of-python-file>`.

So that's _how_ you should test. But _what_, exactly, should you be testing? Let's take the above file structure as an example.

For model tests, you can simply verify that models have the attributes you expect, and write tests for any model methods.

For the routing and view function tests, things get a bit more complicated. You should make sure that requests to all the endpoints supported in the `views` files return valid responses. If certain routes are protected, you should make sure that users who are not authenticated or authorized cannot successfully make those requests. Conversely, if they are authenticated or authorized, they should be able to.

These tests are a bit trickier to write because they require you to make requests in the test, and look through the response in order to verify that the HTML you get back from the server looks correct.

Here are a few different resources for testing your Flask applications.

- [Testing with Flask](https://www.rithmschool.com/courses/flask-fundamentals/testing-with-flask)
- [Sample Tests for Departments in a many-to-many](https://github.com/rithmschool/python_curriculum/blob/master/Unit-02/examples/many_to_many/project/tests/test_departments.py)
- [Testing - Logging In and Out](http://flask.pocoo.org/docs/0.12/testing/#logging-in-and-out)

(If you're still looking for those 🐛🐛, scroll down for soome hints.)

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

&nbsp;

For one bug, the first step in producing it is searching for yourself while you're logged in.

For another bug, what happens when you go to `/users/login` when you're already logged in?
