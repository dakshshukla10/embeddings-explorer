import gensim.downloader as api

from similarity import cosine_similarity

def compare_words(model,word1,word2):
    if word1 not in model:
        print(f"'{word1}' not found in the model.")
        return

    if word2 not in model:
        print(f"'{word2}' not found in the model.")
        return

    vector1 = model[word1]
    vector2 = model[word2]



    score = cosine_similarity(vector1,vector2)

    print(
        f"{word1:<10} vs {word2:<10}"
        f"-> similartiy: {score:.4f}"
    )

def main():
    print("Loading embeddings...")
    model = api.load("glove-twitter-25")
    print("\nSemantic similarity between words:\n")
    print("Enter number of word pairs to compare:")
    pairs = int(input())
    for _ in range(pairs):
        print("\nEnter first word:")
        word1 = input().strip()
        print("Enter second word:")
        word2 = input().strip()
        compare_words(model,word1,word2)

if __name__ == "__main__":
    main()