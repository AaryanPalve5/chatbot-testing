from flask import Flask, render_template, request, jsonify
from gradio_client import Client

app = Flask(__name__)

# Initialize Gradio Client
gradio_client = Client("YashMhaskar/chatbottest")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form.get("user_input")
        try:
            result = gradio_client.predict(user_input)  # or adjust as needed
            print("Gradio response:", result)  # Debugging line
            return jsonify({"response": result})
        except Exception as e:
            print("Error:", e)  # Debugging line
            return jsonify({"error": str(e)})
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
