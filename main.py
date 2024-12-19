from dotenv import load_dotenv


load_dotenv()
from api.index import app

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)