# Sentiment Analyser

A simple command-line tool that analyzes the sentiment of any text you type in. It uses an LLM through [OpenRouter](https://openrouter.ai/) and [LangChain](https://www.langchain.com/) to classify input as **Positive**, **Negative**, or **Neutral**.

## Features

- Interactive CLI loop for analyzing multiple inputs in one session
- Strict single-word output (Positive / Negative / Neutral)
- Uses a free model on OpenRouter (`stepfun/step-3.5-flash:free`), easily swappable
- Minimal setup and easy to extend

## How It Works

The script sends your text to the LLM along with a system prompt that instructs it to act as a sentiment analysis expert and reply with only one word. The response is then printed to the console.
