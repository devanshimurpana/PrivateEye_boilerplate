# Some set up for the application 

from flask import Flask
from flaskext.mysql import MySQL

# create a MySQL object that we will use in other parts of the API
db = MySQL()

def create_app():
    app = Flask(__name__)
    
    # secret key that will be used for securely signing the session 
    # cookie and can be used for any other security related needs by 
    # extensions or your application
    app.config['SECRET_KEY'] = 'someCrazyS3cR3T!Key.!'

    # these are for the DB object to be able to connect to MySQL. 
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = open('/secrets/db_password.txt').readline()
    app.config['MYSQL_DATABASE_HOST'] = 'db'
    app.config['MYSQL_DATABASE_PORT'] = 3306
    app.config['MYSQL_DATABASE_DB'] = 'PrivateEyeDB'  

    # Initialize the database object with the settings above. 
    db.init_app(app)
    
    # Add a default route
    @app.route("/")
    def welcome():
        return "<h1>Welcome to the 3200 boilerplate app</h1>"

    # Import the various routes
    from src.views import views
    from src.technician.technician import technicians
    from src.private_company.private_company import private_companies
    from src.pe_firm.pe_firm import pe_firms
    # Register the routes that we just imported so they can be properly handled
    app.register_blueprint(views,       url_prefix='/v')
    app.register_blueprint(technicians, url_prefix='/t')
    app.register_blueprint(private_companies, url_prefix='/pc')
    app.register_blueprint(pe_firms, url_prefix='/pe')

    return app