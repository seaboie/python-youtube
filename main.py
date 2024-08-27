import ollama
import time
import os
import json
import numpy as np
from numpy.linalg import norm

def parse_file(filename):
    with open(filename, encoding="utf-8-sig") as f:
        paragraphs = []
        buffer = []
        # Read
        for line in f.readlines():
            line = line.strip()
            if line:
                buffer.append(line)
            elif len(buffer):
                paragraphs.append((" ").join(buffer))
                buffer = []
        if len(buffer):
            paragraphs.append((" ").join(buffer))
            
        return paragraphs


def save_embeddings(filename, embeddings):
    # create directory if it does not exist
    if not os.path.exists("embeddings"):
        os.makedirs("embeddings")

    # dump embeddings to json
    with open(f"embeddings/{filename.rsplit('.', 1)[0]}.json", "w") as f:
              json.dump(embeddings, f)

def load_embeddings(filename):
    #  check if not found file
    if not os.path.exists(f"embeddings/{filename.rsplit('.', 1)[0]}.json"):
        return False
    
    # loading from json
    with open(f"embeddings/{filename.rsplit('.', 1)[0]}.json", "r") as f:
        return json.load(f)
    
def get_embeddings(filename, modename, chunks):
    # check if embeddings are already saved
    if (embeddings := load_embeddings(filename)) is not False:
        return embeddings
    
    embeddings = [
        ollama.embeddings(model=modename, prompt=chunk)["embedding"] for chunk in chunks
    ]

    # save embeddings
    save_embeddings(filename, embeddings)

    return embeddings

# find cosine similarity of every chunk to a given embedding
def find_most_similar(needle, haystack):
    needle_norm = norm(needle)
    similarity_scores = [
        np.dot(needle, item) / (needle_norm * norm(item)) for item in haystack
    ]
    return sorted(zip(similarity_scores, range(len(haystack))), reverse=True)

def main():
    SYSTEM_PROMPT = """You are a helpful reading assistant who answers questions 
        based on snippets of text provided in context. Answer only using the context provided, 
        being as concise as possible. If you're unsure, just say that ผมไม่ทราบเลย ครับ.
        Context:
    """
    filename = 'peter-pan.txt'
    paragraphs = parse_file(filename)
    # start = time.perf_counter()
    embeddings = get_embeddings(filename, "mistral-nemo", paragraphs[:120])

    
    prompt = input("What do you want to know? ===> ")
    prompt_embedding = ollama.embeddings(model="mistral-nemo", prompt=prompt)["embedding"]

    # 
    most_similar_chunks = find_most_similar(prompt_embedding, embeddings)[:5]

    # 
    response = ollama.chat(
        model="mistral-nemo",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT + "\n".join(paragraphs[item[1]] for item in most_similar_chunks),
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    
    print("\n\n")
    print(response["message"]["content"])
    # print(len(embeddings))
    # print(time.perf_counter() - start)
    

if __name__ == "__main__":
    main()