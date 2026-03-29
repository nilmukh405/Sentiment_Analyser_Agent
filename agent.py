from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openrouter import ChatOpenRouter

load_dotenv()

# Initialize the LLM (same as your main.py)
llm = ChatOpenRouter(model="stepfun/step-3.5-flash:free")

SYSTEM_PROMPT = """You are a sentiment analysis expert.
Analyze the sentiment of the given text and respond with ONLY one word:
- Positive
- Negative
- Neutral

No explaination needed, just a SINGLE word"""

def analyze_sentiment(text: str) -> str:
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=text)
    ]
    response = llm.invoke(messages)
    return response.content.strip()

def analyze_from_text():
    print("\n----------Text Sentiment Analyser----------")
    print("Type 'quit' to exit\n")
    while True:
        text = input("Enter text: ").strip()
        if text.lower() == "quit":
            break
        if not text:
            print("Please enter some text.")
            continue
        sentiment = analyze_sentiment(text)
        print(f"Sentiment: {sentiment}\n")


def main():
    print("Sentiment Analyser")
    print("------------------")
    analyze_from_text()
   

if __name__ == "__main__":
    main()