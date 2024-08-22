from flask import Flask, render_template, request, jsonify
from gradio_client import Client

app = Flask(__name__)

# Initialize Gradio Client
gradio_client = Client("YashMhaskar/chatbottest")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form.get("user_input")
        # Adjust method call based on the actual API of gradio_client
        # If `predict` takes inputs as positional arguments, you may need to adjust like this:
        try:
            result = gradio_client.predict(user_input)
            return jsonify({"response": result})
        except Exception as e:
            return jsonify({"error": str(e)})
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
