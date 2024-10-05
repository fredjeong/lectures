from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import sentencepiece

# Load the model and tokeniser

#model_name = "facebook/blenderbot-400M-distill"

# Define the chat function

def chat_with_bot(model_name):
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    while True:
        # Get user input
        input_text = input("You: ")

        # Exit conditions
        if input_text.lower() in ["quit", "exit", "bye"]:
            print("Chatbot: Goodbye!")
            break

        # Tokenise input and generate response
        inputs = tokenizer.encode(input_text, return_tensors="pt")
        outputs = model.generate(inputs, max_new_tokens=150)
        response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

        # Display bot's response
        print("Chatbot:", response)


# Start chatting
if __name__=="__main__":
    chat_with_bot("google/flan-t5-base")