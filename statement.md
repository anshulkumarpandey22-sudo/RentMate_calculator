# Project Statement

## Problem Statement
Living with roommates is great, but figuring out how to split the monthly bills usually isn't. When the first of the month rolls around, someone always has to sit down, add up the rent, track down the utility bills, and do the math to figure out exactly what everyone owes. It often leads to manual calculation errors or awkward conversations about who owes what. This project aims to eliminate that friction by providing a fast, reliable, and straightforward tool to calculate exact individual contributions for shared housing expenses, replacing napkin-math with a simple script.

## Scope of the Project
The Easy Rent Calculator is a focused, command-line Python application designed to calculate equal financial splits for shared living expenses. It handles dynamic string inputs to capture any number of roommate names, processes floating-point financial data (rent and utilities), and computes the exact per-person financial obligation. The current scope focuses entirely on equal distribution and does not currently process weighted payments (such as paying more for the master bedroom) or track historical payment statuses. 

## Target Users
*   **College Students:** Students living off-campus in shared housing who need a quick, transparent way to split monthly dues without arguing over the math.
*   **Young Professionals:** Flatmates looking for a no-fuss, automated way to combine rent and utility totals.
*   **Leaseholders:** The specific roommate responsible for collecting everyone's money and paying the landlord, who needs a clear, objective calculation to share in the group chat.

## High-Level Features 
*   **Dynamic Roommate Entry:** The system accepts a comma-separated list of names, automatically cleaning up extra spaces and filtering out empty entries so the roommate count is always accurate.
*   **Comprehensive Expense Aggregation:** It prompts for both base rent and total utilities independently, merging them into a single total household expense.
*   **Automated Split Calculation:** The tool does the heavy lifting by dividing the combined expenses evenly by the exact number of valid roommates detected.
*   **Input Validation & Error Prevention:** If a user accidentally submits a blank line without entering names, the system safely catches it and stops the calculation, preventing technical crashes (like division-by-zero errors).
*   **Clean Financial Formatting:** All monetary outputs are specifically formatted to exactly two decimal places, ensuring the final numbers represent real-world currency constraints.