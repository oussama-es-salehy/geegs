import json
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from helper import get_candidate
from tools import tools
from prompt import system_prompt  # your system prompt string

# -----------------------------
# Load a small HF model
# -----------------------------
MODEL_NAME = "TheBloke/vicuna-7B-1.1-HF"  # or smaller if PC is weak
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, device_map="auto", torch_dtype=torch.float16)

def generate_response(prompt, max_length=200):
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(**inputs, max_new_tokens=max_length)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# -----------------------------
# Agent
# -----------------------------
def hr_ai_agent():
    print("🤖 HR AI Agent: Ask me anything about candidates or jobs! (type 'exit' to quit)")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        # Compose prompt for LLM
        prompt = f"""
{system_prompt}

User question: "{user_input}"

Available ML models:
1. Job Fit Prediction -> Inputs: candidate_skills, required_skills, degree, years_experience
2. Salary Prediction -> Inputs: years_experience, role, degree, company_size, location, level
3. Resume Screening -> Inputs: resume_text, job_description_text
4. Candidate Priority -> Inputs: experience_band, skills_coverage, referral_flag, english_level, location_match

Always respond with a JSON object with keys:
- model: chosen model name
- params: dictionary of input parameters for the model
- note: optional explanation
"""

        llm_output = generate_response(prompt)
        
        try:
            llm_data = json.loads(llm_output)
            model_name = llm_data.get("model")
            params = llm_data.get("params", {})
        except json.JSONDecodeError:
            print("HR AI Agent: Could not parse model from LLM, showing raw response:")
            print(llm_output)
            continue

        # Fetch candidate info if candidate_id provided
        candidate_id = params.get("candidate_id")
        if candidate_id:
            candidate_info = get_candidate(candidate_id)
            if candidate_info:
                params.update(candidate_info)

        # Map model_name to your actual API functions
        api_map = {
            "Job Fit Prediction": "check_job_fit",
            "Salary Prediction": "predict_salary",
            "Resume Screening": "screen_resume",
            "Candidate Priority": "get_priority"
        }

        func_name = api_map.get(model_name)
        if func_name and func_name in tools:
            try:
                result = tools[func_name](**params)
            except Exception as e:
                result = {"error": str(e)}
        else:
            result = {"error": "Unknown model or missing tool"}

        print("HR AI Agent Output:")
        print(json.dumps(result, indent=2))


# -----------------------------
# Run the agent
# -----------------------------
if __name__ == "__main__":
    hr_ai_agent()
