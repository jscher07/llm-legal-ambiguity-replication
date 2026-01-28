# Replication Materials

This repository contains code and data for the empirical study in "Beyond Words: The Risks of Generative Interpretation" by Jonathan Scher, forthcoming in the *Southern California Law Review*. 

## About the Study

This Note examines whether GPT-4 Turbo can reliably detect textual ambiguity in real-world legal interpretation. I tested the model on eight Ninth Circuit cases, prompting it 100 times per case with paraphrased versions of each legal question. Rather than looking at the model's text outputs (which can be distorted by temperature settings), I extracted the model's internal log-probabilities to get a clearer pircutre of its actual confidence in a given interpretation.

The short version: GPT-4 Turbo disagreed with the courts on ambiguity 50% of the time.

### What's Here

- code/gpt4_turbo_logprobs.py: The Python script used to query GPT-4 Turbo and extract log-probabilities
- data/gpt4_logprobs_100prompts.xlsx: Raw output data and prompt information for all eight cases (100 prompts each)

### The Cases

1. *Buero v. Amazon.com Servs., Inc.*
2. *Gonzales & Gonzales Bonds & Ins. Agency, Inc. v. Dep't of Homeland Security*
3. *Leuthauser v. United States*
4. *M&T Farms v. Fed. Crop Ins. Corp.*
5. *Manrique v. Kolc*
6. *United States v. Paulson*
7. *United States v. Scheu*
8. *United States v. Trumbull*

### Approach
Following a modified version of Choi's confidence estimation method:

1. For each case, GPT-4 Turbo was prompted **100 times** with paraphrased versions of the legal interpretation question
2. Each prompt asked the model to respond with a number from 0-100 representing confidence
3. The model's **top 5 most probable numeric outputs** were recorded along with their log-probabilities
4. A **weighted average confidence score** was calculated for each prompt

### Prompt Structure
Each prompt followed this general structure:
```
[Legal interpretation question with statutory/contractual text]
Answer with a number from 0 to 100 representing a confidence level. 
0 being "no" and 100 being "yes." 
Don't let your prior responses influence your future responses. 
Only answer with a number from 0 to 100.
```

Paraphrased versions were generated using Claude to test prompt sensitivity.

## Data Dictionary

The Excel file contains 8 sheets (one per case), each with the following columns:

| Column | Description |
|--------|-------------|
| Prompt # | Prompt iteration number (1-100) |
| Prompt Text | The full text of the paraphrased prompt |
| Model Response | GPT-4 Turbo's numeric response |
| Token | The token value from top-5 logprobs |
| Logprob | Log-probability of the token |
| Raw Probability | Exponentiated logprob (actual probability) |
| Rank | Rank among top-5 tokens (Top 1, Top 2, etc.) |
| Weighted Average | Confidence score weighted by probability |
| Normalized Probability (%) | Probability as percentage |

## Requirements

To run the analysis script:
```bash
pip install openai matplotlib numpy seaborn pandas
```

Set your OpenAI API key:
```bash
export OPENAI_API_KEY="your-api-key-here"
```

## Citation

If you use this code or data, please cite:

```
Jonathan Scher, Beyond Words: The Risks of Generative Interpretation in the Courtroom, 
S. CAL. L. REV. (forthcoming 2026).
```

## License

MIT License

## Contact

Jonathan Scher  
University of Southern California Gould School of Law  
jonathan.scher.2026@lawmail.usc.edu
