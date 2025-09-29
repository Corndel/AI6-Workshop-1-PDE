## Corndel - Level 6 Applied AI Engineering
# 🛡️ Pipeline Risk Assessment Grid

Use this 2x2 grid to categorise the risks you identified in your **Lessons-Learnt Log**. The goal is to prioritise which risks require the most attention.

A **risk** is any potential event that could cause your pipeline to fail, produce incorrect results, or have a negative real-world consequence.

---

## How to Use

1.  **Identify a Risk:** Think of something that could go wrong with your data, code, model, or infrastructure.
2.  **Assess Impact:** If this risk happens, how bad would the consequences be? (Low Impact vs. High Impact)
3.  **Assess Likelihood:** How likely is it that this risk will actually happen? (Low Likelihood vs. High Likelihood)
4.  **Place it in the Grid:** Write your risk in the corresponding quadrant below.

---

## The Risk Grid

|                  | **Low Likelihood** <br/> _(Rare, Unlikely)_ | **High Likelihood** <br/> _(Frequent, Probable)_ |
| :--------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **High Impact** <br/> _(Major financial, reputational, or ethical damage)_ | ### 🟠 Major Risk: Monitor & Mitigate <br/> _These are serious but unlikely threats. You should have a clear plan to mitigate them if they occur._ <br/><br/> **Example:** _"The S3 bucket containing sensitive training data is accidentally made public."_ <br/><br/> **Your Risks:** <br/> - | ### 🔴 Critical Risk: Address Immediately <br/> _These are your top priorities. They are likely to happen and will cause significant problems._ <br/><br/> **Example:** _"Model performance degrades over time (drift) due to changing economic conditions, causing poor loan decisions."_ <br/><br/> **Your Risks:** <br/> - |
| **Low Impact** <br/> _(Minor inconvenience, easily fixed, low cost)_ | ### 🟢 Low Risk: Monitor Casually <br/> _These are the lowest priority. Acknowledge them but don't spend significant resources on them._ <br/><br/> **Example:** _"A typo in a log message causes minor confusion during debugging."_ <br/><br/> **Your Risks:** <br/> - | ### 🟡 Minor Risk: Accept or Automate <br/> _These are frequent but manageable annoyances. Either accept them or find an efficient/automated way to handle them._ <br/><br/> **Example:** _"A pipeline run fails due to a temporary AWS service outage, requiring a manual re-run."_ <br/><br/> **Your Risks:** <br/> - |

---

## Your Prioritised Risks

After filling out the grid, list the risks you will focus on, starting with the **Critical** ones.

* **Critical Risks to Address:**
    1.  
    2.  

* **Major Risks to Mitigate:**
    1.  
    2.
