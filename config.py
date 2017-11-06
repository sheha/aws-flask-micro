# Here we set up the DB,polling, and a little bit of security for Flask
# Add your own or use mine, which will keep you in  the Free Tier
# ( which is even more than we need for this microservice ).
# format: (user):(password)@(db_identifier).amazonaws.com:3306/(db_name)


SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://roman:letters123@romanletters.cyfipmeu2bho.eu-central-1.rds.amazonaws.com:3306/romandb'

# Uncomment the line below if you want to work with a local DB
# SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

SQLALCHEMY_POOL_RECYCLE = 3600

WTF_CSRF_ENABLED = True
SECRET_KEY = 'dsaf0897sfdg45sfdgfdsaqzdf98sdf0a'
