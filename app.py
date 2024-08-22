import logging
from flask import Flask, render_template, request, jsonify
from gradio_client import Client

app = Flask(__name__)

# Initialize Gradio Client
gradio_client = Client("YashMhaskar/chatbottest")

# Configure logging
#logging.basicConfig(level=logging.DEBUG)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form.get("user_input")
        if not user_input:
            return jsonify({"response": "No input provided."})

        try:
            # Make a request to Gradio API
            result = gradio_client.predict(user_input=user_input, api_name="/predict")
            return jsonify({"response": result})
        except Exception as e:
            app.logger.error(f"Error occurred: {e}")
            return jsonify({"response": "An error occurred, please try again."})

    return render_template("index.html")

if __name__ == "__main__":
    # Run Flask app
    app.run(debug=True, host='0.0.0.0', port=8000)  # Use appropriate port
