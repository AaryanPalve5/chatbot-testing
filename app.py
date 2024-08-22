from flask import Flask, render_template, request, jsonify
from gradio_client import Client

app = Flask(__name__)

# Initialize Gradio Client
gradio_client = Client("YashMhaskar/chatbottest")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form.get("user_input")
        result = gradio_client.predict(user_input=user_input, api_name="/predict")
        return jsonify({"response": result})
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
