import network as n
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

G = n.load_graph()

@app.route("/connection/<root>/<target>")
def connection(root, target):
    return n.get_connection(G, root, target)

if __name__ == "__main__":
    app.run(threaded=True, port=5000)