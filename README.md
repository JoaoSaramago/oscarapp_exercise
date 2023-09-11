# OSCAR App Exercise Solution

### Test locally:

1. Run `pip install -r requirements.txt` to install the python requirements for this project.
2. Build the database and apply the migrations using `python manage.py migrate`.
3. Run the server using the command `python manage.py runserver`
4. Go to the documentation on [http://localhost:8000/api/schema/swagger-ui/](http://localhost:8000/api/schema/swagger-ui/). 
Here you can check the available endpoints.
5. Use the signup [endpoint](http://localhost:8000/api/schema/swagger-ui/#/users/users_signup_create) and click on the button "Try it out" to be able to edit the Request body.
6. After successfully creating an account, use the login [endpoint](http://localhost:8000/api/schema/swagger-ui/#/users/users_login_create) and click on the button "Try it out" to be able to edit the Request body. 
After a successful login refresh the web page so that the CSRF header updates and you can test other endpoints.