from Database import Client
from dotenv import load_dotenv
load_dotenv()

# Machine Learning
db = Client('ml')
db.query("SELECT * FROM user_station_interactions")
db.close()