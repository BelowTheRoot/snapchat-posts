from app import *

db.create_all()
# db.drop_all()
db.session.commit()
