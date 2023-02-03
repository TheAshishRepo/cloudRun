from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def homepage():
    if request.method == "GET":
        return jsonify({"message": "Hello Ashish welcome to CloudRun!"})

# PORT = int(os.environ.get("PORT", 8080))
PORT = 8080
if __name__ == '__main__':
    app.run(threaded=True,host='0.0.0.0',port=PORT)
