## Corndel - Level 6 Applied AI Engineering
# 📝 Lessons-Learnt Log: QuickLoan Workshop

**Name:** `___________________________`
**Date:** `____/____/______`
**Workshop:** `WS1 – Ethics-First Design in Action`

---

## 1. Technical Pipeline Summary

* **Data Source:**
    > _Describe the `cs-training.csv` file. What does it contain? Where was it sourced from?_

* **Preprocessing Step(s):**
    > _What happened in the `process.py` script? Think about data cleaning, feature engineering, and splitting the data._

* **Model Training:**
    > _What algorithm was used (XGBoost)? What was its objective? Note the instance type used._

* **Model Registration & Deployment:**
    > _How was the model evaluated (AUC threshold)? What does `PendingManualApproval` mean for a real-world deployment process?_

---

## 2. Observations During the Build

* **Assumptions I Made:**
    > _e.g., "I assumed the data was clean," and/or "I assumed the default hyperparameters were good enough."_

* **Unexpected Issues:**
    > _e.g., "The pipeline took longer than expected," or "I had a permissions error with my S3 bucket."_

* **Decisions Taken Without Full Evidence:**
    > _e.g., "I chose an AUC threshold of 0.75 without knowing the business impact of false positives vs. false negatives."_

---

## 3. Ethical & Governance Reflections

* **Who might be negatively affected by this pipeline?** 👥
    > _Think beyond the end-user. Consider loan applicants who are unfairly rejected, or even loan officers whose jobs might change._

* **What biases or blind spots might exist in this model?**
    > _Consider historical bias in the data (e.g., were certain demographics historically denied loans?) and how the model might perpetuate it._

* **How did I consider fairness, privacy, and security?** 🔐
    > _Did you think about who has access to the data? How are you ensuring the model doesn't discriminate against protected groups?_

* **What evidence would a regulator or stakeholder need to see to trust this model?**
    > _Think about model cards, fairness reports, explainability reports and logs of who accessed the model._

---

## 4. Risks Identified

* **Most Fragile Part of My Pipeline:**
    > _e.g., "The data processing step, because a change in an input column name would break everything."_

* **Risks with High Likelihood:**
    > _e.g., "Model performance will degrade over time (concept drift) as economic conditions change."_

* **Risks with High Impact:**
    > _e.g., "A biased model is deployed, leading to discriminatory lending, reputational damage, and regulatory fines."_

* **Mitigation Ideas:**
    > _For the risks above, what's one action you could take? e.g., "Implement automated monitoring for data drift and fairness metrics."_

---

## 5. What Worked vs. What Didn’t

* **✅ Worked Well:**
    > _e.g., "The SageMaker Pipeline abstracted away a lot of the complexity of connecting steps."_

* **❌ Didn’t Work Well:**
    > _e.g., "It was hard to debug the processing script once it was running inside the pipeline."_

* **💡 Something I’d Change Next Time:**
    > _e.g., "I would add more logging to my scripts to make debugging easier."_

---

## 6. Lessons for My Professional Practice

* **How will I document my work better in the future?**
    > _e.g., "I will create a model card for every model I build, even experimental ones."_

* **How can I explain this build to a non-technical stakeholder (like a product manager)?**
    > _Practice a simple, one-paragraph explanation focusing on the business value and the safeguards put in place._

* **What concrete step will I take to improve responsible engineering in my work?**
    > _e.g., "I will add a fairness check as a standard step in my project template," or "I will schedule a pre-mortem to identify risks before starting my next project."_

---

## 7. Personal Reflection (Private)

* **What blind spots did I notice in my own thinking?**
    > _Did I focus too much on the tech and not enough on the people it affects? Did I make assumptions without realizing it?_

* **Which ethical value or principle do I need to consciously bring into my engineering practice?**
    > _e.g., Fairness, transparency, accountability, security, privacy._
