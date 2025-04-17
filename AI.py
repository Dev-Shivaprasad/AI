from gpt4all import GPT4All

MODEL_PATH = r"M:\0~CODEBASE\All_AI_Models\phi-2-orange.Q8_0.gguf"

try:
    model = GPT4All(model_name=MODEL_PATH, device="cuda", allow_download=False, verbose=True)
    print("✅ Model loaded successfully!")
except Exception as e:
    print(f"❌ Failed to load model: {e}")
    model = None

def AnalyzeFinancialData(Finance_Data):

    if model is None:
        return {"message": "❌ Model not loaded. Please check server logs."}

    prompt = f"""You are a smart and helpful financial advisor.
Analyze the user's financial data below and suggest improvements to help them make better economic decisions, Start the output by saying Based on the provided financial data, here are some suggestions to help you make better economic decisions and manage your finances more effectively:


Financial Data:
{Finance_Data}

Tips:"""
    try:
        with model.chat_session():
            response =model.generate(
                prompt=prompt,
                temp=0.4,
                top_k=50,
                top_p=0.95,
                repeat_penalty=1.1,
                n_predict=512
            )

        clean_response = response.strip().replace("\\n", "\n")
        return {"message": clean_response}

    except Exception as e:
        print(f"❌ Error during generation: {e}")
        return {"message": f"❌ Error: {e}"}
if __name__ == "__main__":
    financial_data = "Amount 100000.00 Indian Rupees Owed To SBI at interest rate of 9.3 percent(%) before 86 days Amount 1200.00 Indian Rupees Owed To Kishor at interest rate of 1 percent(%) before 100 days  Spent 8000.00 Indian Rupees on ration and it is a fixed expense, Spent 12000.00 Indian Rupees on Service and it is not a fixed expense, Income of 20000.00 Indian Rupees from job and it is not a fixed income, Invested 500.00 Indian Rupees into stocks, Started saving for Car which costs 10000000.00 Indian Rupees. Till now I have saved 50000.00 Indian Rupees"
    analysis_result = AnalyzeFinancialData(financial_data)
    print(analysis_result["message"])