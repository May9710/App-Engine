import pyodbc
from flask import Flask

connection = pyodbc.connect('Driver={FreeTDS};'
                            'Server=mpponeuse2rhqsql.public.a293f7a7d79e.database.windows.net,3342;'
                            'Database=dwh_CO_Cencosud;'
                            'UID=usrOwner_CO_PM;'
                            'PWD=A*jy5~QeZd76gXc9')
cursor = connection.cursor()

app = Flask(__name__)
@app.route('/')
def index():
    cursor.execute("SELECT DISTINCT CampaignID FROM dwh_CO_Cencosud.dbo.GG_Ads")
    for row in cursor.fetchall():
        print(row.Name)
    
    connection.close()

if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
    
    
