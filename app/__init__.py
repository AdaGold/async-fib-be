from flask import Flask
from flask_cors import CORS

def fib(n):
    if n <= 1:
        return n

    return fib(n-1) + fib(n-2)

def create_app():
    app = Flask(__name__)

    @app.get("/fib/<n>")
    def get_fib(n):
        n = int(n)
        return dict(result=fib(n))

    CORS(app)

    return app