from application import db
'''This triggers DB INIT on AWS'''
db.create_all()

print("DB created.")
