# Prompt Generation Methodology

## Overview

For each of the eight cases, 100 paraphrased versions of the core legal interpretation question were generated using Claude (Anthropic). This approach tests the model's prompt sensitivity—whether small changes in wording lead to different confidence assessments.

## Meta-Prompt Structure

The following meta-prompt was used to generate paraphrased versions:

```
Generate 100 paraphrased versions of the following legal interpretation question. 
Each paraphrase should:
1. Preserve the core legal question being asked
2. Include the relevant statutory/contractual text
3. Vary the wording, sentence structure, and framing
4. End with instructions to respond with a number from 0-100

Original question: [CASE-SPECIFIC QUESTION]

Each paraphrase should end with:
"Answer with a number from 0 to 100 representing a confidence level. 
0 being 'no' and 100 being 'yes.' 
Don't let your prior responses influence your future responses. 
Only answer with a number from 0 to 100."
```

## Case-Specific Base Questions

### Buero v. Amazon.com Servs., Inc.
> Is time spent in security screening lines considered part of "time of authorized attendance" at work?

### Gonzales & Gonzales Bonds & Ins. Agency, Inc. v. Dep't of Homeland Security
> Does "function or duty" in the Federal Vacancies Reform Act apply only to duties expressly made nondelegable by statute?

### Leuthauser v. United States
> Are Transportation Security Officers (TSOs) "investigative or law enforcement officers" under the FTCA, defined as "any officer of the United States who is empowered by law to execute searches, seize evidence, or make arrests for violations of Federal law"?

### M&T Farms v. Fed. Crop Ins. Corp.
> Does a storefront partnership's marketing and selling of its partners' farm commodities constitute "farming activity" under a federal crop insurance policy?

### Manrique v. Kolc
> Does the term "charged with" in an extradition treaty include non-formal charges?

### United States v. Paulson
> Under 26 U.S.C. § 6324(a)(2), does the phrase "on the date of the decedent's death" apply to both "receives" and "has"?

### United States v. Scheu
> A defendant dragged an individual 35 to 40 feet into a cornfield before sexually assaulting her. Based on the plain meaning of the word "abduct," did the defendant abduct her?

### United States v. Trumbull
> The defendant was arrested while in possession of a Glock 17 loaded with 17 rounds. Is this a semiautomatic weapon that is capable of accepting a large capacity magazine?

## Prompt Variations

The paraphrased prompts varied along several dimensions:
- **Framing**: Direct questions vs. hypothetical scenarios
- **Voice**: Active vs. passive construction
- **Specificity**: Including more or less statutory context
- **Question type**: Yes/no framing vs. interpretive framing

## Example Paraphrases (Buero case)

1. "Is time spent in security screening lines considered part of 'time of authorized attendance' at work?"
2. "When employees wait in security screening lines, should this count as 'time of authorized attendance'?"
3. "On a scale of 0-100, does 'time of authorized attendance' include security screening wait times?"
4. "Should 'time of authorized attendance' be read to include time employees spend in a mandatory security screening?"
5. "Under a strict reading, does 'time of authorized attendance' cover time spent in a security line before work?"

(See data files for complete prompt lists)
