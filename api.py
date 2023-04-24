from flask import Flask, jsonify, request
from gpt_index import GPTSimpleVectorIndex
import os

os.environ["OPENAI_API_KEY"] = "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"

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/response',methods=['POST'])

def answerMe():

    vIndex = GPTSimpleVectorIndex.load_from_disk('vectorIndex.json')
    prompt = request.form.get('prompt')
    response = vIndex.query(prompt,response_mode = 'compact')

    return jsonify(response)
    


if __name__ == "__main__":
    app.run(debug=True)