# python
# A Flask application that allows login and registration. 
# One of the major components to every website is login and registration.
Registration: The user inputs their information and the informations gets verified as correct or incorrect. user 
information gets inserted into the database and returned back with a success message. If the information is not 
valid, user gets redirected to the registration page.

Validations: First Name - letters only, at least 2 characters and that it was submitted
Last Name - letters only, at least 2 characters and that it was submitted
Email - valid Email format, does not already exist in the database, and that it was submitted
Password - at least 8 characters, and that it was submitted
Password Confirmation - matches password

When the user initially registers we would log them in automatically.

For logging in, we need to validate in a different way:
Check whether the email provided is associated with a user in the database,
if it is, check whether the password matches what's saved in the database.

Logout: A logout button or link. When a user logs out, their session should be cleared. If the user attempts to 
access a page (i.e. making a GET request by typing in the url), they are redirected back to the login and 
registration page.
