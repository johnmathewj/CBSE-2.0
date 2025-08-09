import re
from flask import Flask, request, jsonify
from flask_cors import CORS
from google import genai

client = genai.Client(api_key="AIzaSyBc70X28NtqrbzEpkz6uKcbLfXgDZ1Sixs")


def generate_explanation(name, class_, topic, board):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Explain the topic {topic} of class {class_} to a student named {name} as per syllabus of {board} elaborately. When giving your prompt whereever there is a new line insert a <br> there and if there is a case where you are teaching html then if there is any html related content write it like this &lt;tagname&gt; Don't mention about this in your prompt.",
    )
    raw_text = response.text
    return raw_text


app = Flask(__name__)
CORS(app)


@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    name = data.get("name")
    topic = data.get("topic")
    board = data.get("board")
    class_ = data.get("class")

    explanation = generate_explanation(name, class_, topic, board)
    return jsonify({"txt": explanation})


if __name__ == "__main__":
    app.run(debug=True)

