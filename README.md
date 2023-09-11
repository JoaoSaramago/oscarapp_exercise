# OSCAR App Exercise Solution

### Test locally:

1. Run `pip install -r requirements.txt` to install the python requirements for this project.
2. Build the database and apply the migrations using `python manage.py migrate`.
3. Run the server using the command `python manage.py runserver`
4. Go to the documentation on [http://localhost:8000/api/schema/swagger-ui/](http://localhost:8000/api/schema/swagger-ui/). 
Here you can check the available endpoints.

**[Now you can keep using the documentation page to test the endpoints or use another software of your choice, for example, Postman]**
5. Use the signup [endpoint](http://localhost:8000/api/schema/swagger-ui/#/users/users_signup_create) by clicking on the button "Try it out" to be able to edit the Request body, and then click on "Execute" to make the request.
6. After successfully creating an account, use the login [endpoint](http://localhost:8000/api/schema/swagger-ui/#/users/users_login_create). 
When you get a success message on the login, refresh the web page so that the CSRF header updates and you can test other endpoints.