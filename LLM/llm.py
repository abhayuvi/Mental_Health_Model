from llama_cpp import Llama

# Load model (Update path to your model file)
llm = Llama(model_path="/content/phi-2.Q4_K_M.gguf")

def query_llm(prompt, max_tokens=300):
    """Query the LLM with a structured prompt and force correct responses."""
    output = llm(prompt, max_tokens=max_tokens)
    return output['choices'][0]['text'].strip()


def suggest_coping_mechanisms(predicted_condition):
    """Suggest coping strategies and self-care methods for the condition"""
    prompt = f"""
    A user has been predicted to have **{predicted_condition}**. 

    **Your task:** Provide a **detailed** and **practical** coping guide, including:
    
    **1️⃣ Understanding the Condition:**  
    - How does {predicted_condition} impact mental health?  
    - How does it affect daily life?  

    **2️⃣ Self-Care Strategies:**  
    - Provide **at least 5 practical coping techniques** (e.g., lifestyle changes, meditation, journaling).  
    - Explain **why** each method works.  

    **3️⃣ When to Seek Professional Help:**  
    - When should a person with {predicted_condition} seek professional help?  
    - What kind of therapies or treatments are most effective?  

    **4️⃣ Additional Resources:**  
    - Recommend books, apps, or support groups.  

    **(Write in a **friendly and supportive** tone, avoiding medical jargon. Use full sentences and paragraphs.)**  
    """
    return query_llm(prompt)


def generate_explanation(predicted_condition):
    """Generate a detailed explanation for the given mental health condition"""
    prompt = f"""
    ### 🧠 Explanation of {predicted_condition} ###
    
    **Definition:**  
    Explain in **simple, clear language** what {predicted_condition} is.  
    
    **Causes:**  
    List **scientific and psychological reasons** why someone might develop this condition.  
    
    **Symptoms:**  
    Describe the **common mental, emotional, and physical symptoms** in at least **5 bullet points**.  
    
    **Effects on Daily Life:**  
    Explain how {predicted_condition} can affect work, relationships, and personal well-being.  
    
    **(Write at least 150 words in full paragraphs)**  
    """
    return query_llm(prompt)



predicted_condition = "Generalized Anxiety Disorder"

explanation = generate_explanation(predicted_condition)
coping_mechanisms = suggest_coping_mechanisms(predicted_condition)

print("🧠 Explanation:", explanation)
print("💡 Coping Strategies:", coping_mechanisms)
