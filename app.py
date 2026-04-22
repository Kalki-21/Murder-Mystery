from flask import Flask, jsonify, request, send_from_directory
from cases import load_cases
from game_engine import GameEngine

app = Flask(__name__, static_folder="web", static_url_path="")

cases = load_cases()
engine = None
current_case = None


@app.route("/")
def index():
    return send_from_directory("web", "index.html")


@app.route("/get_cases")
def get_cases():
    return jsonify([c.title for c in cases])


@app.route("/select_case", methods=["POST"])
def select_case():
    global current_case, engine

    data = request.get_json()
    index = int(data["index"])

    current_case = cases[index]
    engine = GameEngine(current_case)

    return jsonify({"story": current_case.story})


@app.route("/get_suspects")
def get_suspects():
    if not current_case:
        return jsonify([])

    return jsonify([s.name for s in current_case.suspects])


@app.route("/get_questions", methods=["POST"])
def get_questions():
    if not current_case:
        return jsonify([])

    data = request.get_json()
    name = data["suspect"]

    for s in current_case.suspects:
        if s.name == name:
            return jsonify(list(s.responses.keys()))

    return jsonify([])


@app.route("/ask", methods=["POST"])
def ask():
    if not engine:
        return jsonify({"answer": "Start a case first."})

    data = request.get_json()
    name = data["suspect"]
    question = data["question"]

    for s in current_case.suspects:
        if s.name == name:
            return jsonify({"answer": engine.ask_question(s, question)})

    return jsonify({"answer": "No response."})


@app.route("/get_clue")
def get_clue():
    if not engine:
        return jsonify({"clue": "Start a case first."})

    return jsonify({"clue": engine.get_clue()})


@app.route("/accuse", methods=["POST"])
def accuse():
    if not engine:
        return jsonify({"result": False})

    data = request.get_json()
    name = data["suspect"]

    return jsonify({"result": engine.check_answer(name)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)