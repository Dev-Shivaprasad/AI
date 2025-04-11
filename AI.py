from gpt4all import GPT4All

ModelPath = r"M:\0~CODEBASE\PYTHON\AI(API)\Models\FinGPT-MT-Llama-3-8B-LoRA-Q4_K_M.gguf"

available_gpus = GPT4All.list_gpus()
print(f"Available GPUs: {available_gpus}")

# Try loading the model
try:
    model = GPT4All(model_name=ModelPath, device="cuda", allow_download=False, verbose=True)
    print("✅ Model loaded successfully!")
except Exception as e:
    print(f"❌ Failed to load model: {e}")
    model = None

def Generate(Prompt: str):
    if model is None:
        return {"message": "Model not loaded. Please check server logs."}

    try:
        with model.chat_session() as chat:
            response = chat.generate(
                prompt=Prompt,
                max_tokens=600,
                temp=0.3,
                repeat_penalty=1.1,
            )
        
        if not response or response.strip() == "":
            return {"message": "❌ Model generated an empty response. Please try again."}

        # Clean response
        clean_response = response.replace('\\n', '\n').replace('\\"', '"').strip()
           
        # Remove unnecessary prefixes if exist
        for unwanted in ["Assistant:", "User:"]:
            if unwanted in clean_response:
                clean_response = clean_response.split(unwanted)[-1].strip()

        return {"message": clean_response}
    except Exception as e:
        print(f"❌ Exception during generation: {e}")
        return {"message": f"❌ Error: {e}"}
