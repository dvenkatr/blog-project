### Blog with the following functionality

**Without login**
- View the published blog posts
- Add a commment to a blog post

**Login required**
- Add a new post and save it as a draft
- Publish a draft
- Edit or delete a post
- Approve or remove a commment

Registration has been implemented through superusers / admin only

### Libraries / dependencies
- Python v3.9
- Django v3.1.6
- WSIWG editor yabwe
- Bootstrap v4.0
- Google fonts Libre Baskerville and Dosis
- Home page by domaso
- See requirements.txt for other dependencies in my virtual environment (some of these are dev only dependencies, and need to be cleaned up)

### Run
- Clone the project
- python manage.py runserver and visit http://127.0.0.1:8000
- python manage.py createsuperuser to create an admin login for http://127.0.0.1:8000/admin (where you can add other users)
