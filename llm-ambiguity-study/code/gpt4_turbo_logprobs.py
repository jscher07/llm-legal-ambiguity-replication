"""
GPT-4 Turbo Log-Probability Analysis for Legal Ambiguity Detection

This script queries GPT-4 Turbo with paraphrased legal interpretation questions
and extracts the model's internal log-probabilities to measure confidence levels.

Author: Jonathan Scher
Associated Paper: "Beyond Words: The Risks of Generative Interpretation in the Courtroom"
Southern California Law Review (forthcoming)

Usage:
    1. Set your OpenAI API key as an environment variable:
       export OPENAI_API_KEY="your-api-key-here"
    2. Run the script:
       python gpt4_turbo_logprobs.py
"""

import os
import openai
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Load API key from environment variable (never hardcode API keys!)
openai.api_key = os.environ.get("OPENAI_API_KEY")

if not openai.api_key:
    raise ValueError("Please set the OPENAI_API_KEY environment variable")

MODEL = "gpt-4-turbo"

collected_data = []
logprob_data = []

# Example prompt - replace with your specific legal interpretation question
PROMPT = '''
[Your legal interpretation question here]
Answer with a number from 0 to 100 representing a confidence level. 
0 being "no" and 100 being "yes." 
Don't let your prior responses influence your future responses. 
Only answer with a number from 0 to 100.
'''

for i in range(100):
    try:
        response = openai.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": PROMPT}],
            max_tokens=10,
            logprobs=True,
            top_logprobs=5,  # Get top 5 most probable tokens
        )
        
        output = response.choices[0].message.content.strip()
        logprobs = response.choices[0].logprobs

        try:
            number = int(output)
            if 0 <= number <= 100:
                collected_data.append(number)
                logprob_data.append(logprobs)
        except ValueError:
            continue
            
    except Exception as e:
        print(f"Error on iteration {i}: {e}")
        continue

if len(collected_data) == 0:
    print("No valid data collected.")
else:
    print(f"Collected Data: {collected_data}")

# Calculate the mean confidence
mean_confidence = np.mean(collected_data)
print(f"Mean Confidence: {mean_confidence}")

# Plot the distribution
sns.kdeplot(collected_data, fill=True, bw_adjust=1, label=f'Mean = {mean_confidence:.2f}')
plt.xlim(0, 100)
plt.xlabel('Confidence Level (0 = NO; 100 = YES) [n=100]')
plt.ylabel('Density')
plt.title('GPT-4 Turbo Confidence Distribution')
plt.legend()
plt.grid(True)
plt.show()

# Print example log-probabilities
print("\nExample Logprobs:")
for i, lp in enumerate(logprob_data[:3]):
    print(f"Response {i+1}:")
    if lp and lp.content:
        for token_info in lp.content[0].top_logprobs:
            print(f"  Token: {token_info.token} | Logprob: {token_info.logprob:.4f}")
