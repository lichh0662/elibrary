import os
SECRET_KEY = 'cd99f6eb39b78d27742089f72bb2102587c30f7c22c4c97850ded91dda7e58cd'

MYSQL_USER = 'helious12'
MYSQL_PASSWORD = 'Lich1204!'
MYSQL_HOST = 'helious12.mysql.pythonanywhere-services.com'
MYSQL_DATABASE = 'elibrary'




ADMIN_ROLE_ID = 1
MODERATOR_ROLE_ID = 2

UPLOAD_FOLDER = UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'img')