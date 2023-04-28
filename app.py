from gpt_index import GPTSimpleVectorIndex
import os

os.environ["OPENAI_API_KEY"] = "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"

def answerMe(vectorIndex):
    vIndex = GPTSimpleVectorIndex.load_from_disk(vectorIndex)
    while True:
        prompt = input("Please ask: ")
        response = vIndex.query(prompt,response_mode = 'compact')
        print(f"Response: {response}\n")

answerMe('vectorIndex.json')