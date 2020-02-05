from flask import Flask

app = Flask(__name__)
db_uri = 'mysql+pymysql://root:nippy@localhost/feedreader'
app.config['SQLALCHEMY_DATABASE_URL'] db_uri

