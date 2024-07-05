
""" this module does this blabla """

from fastapi import FastAPI
from .frontend import init

app = FastAPI()


@app.get('/')
def read_root():
    return {'Hello': 'World'}


init(app)

if __name__ == '__main__':
    print('Please start the app with the "uvicorn" command as shown in the start.sh script')