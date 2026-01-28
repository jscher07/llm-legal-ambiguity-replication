# LLM Ambiguity Detection Study: Replication Materials

This repository contains replication code and data for the empirical study in:

**"Beyond Words: The Risks of Generative Interpretation in the Courtroom"**  
Jonathan Scher  
*Southern California Law Review* (forthcoming)

## Overview

This study evaluates GPT-4 Turbo's ability to detect textual ambiguity across eight Ninth Circuit cases. Unlike prior studies that rely on repeated prompts and "temperature" variance, this study extracts the model's internal log-probabilities, providing a more accurate measure of its confidence.

### Key Findings
- GPT-4 Turbo's ambiguity assessments diverged from judicial determinations in 37.5% of cases
- Even when the model aligned with the court on ambiguity classification, its interpretation of the text sometimes differed
- The distribution of LLM responses does not reflect real-world survey responses from humans

## Repository Structure

```
├── README.md
├── code/
│   └── gpt4_turbo_logprobs.py    # Main analysis script
├── data/
│   └── gpt4_logprobs_100prompts.xlsx    # Raw output data (8 cases × 100 prompts)
└── prompts/
    └── prompt_generation.md      # Methodology for generating paraphrased prompts
```

## Methodology

### Cases Analyzed
1. **Buero v. Amazon.com Servs., Inc.** - "time of authorized attendance"
2. **Gonzales & Gonzales Bonds & Ins. Agency, Inc. v. Dep't of Homeland Security** - "function or duty"
3. **Leuthauser v. United States** - "investigative or law enforcement officers"
4. **M&T Farms v. Fed. Crop Ins. Corp.** - "farming activity"
5. **Manrique v. Kolc** - "charged with"
6. **United States v. Paulson** - "on the date of the decedent's death"
7. **United States v. Scheu** - "abduct"
8. **United States v. Trumbull** - "semiautomatic weapon" / "large capacity magazine"

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
