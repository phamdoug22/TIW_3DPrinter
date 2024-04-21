"""
Test Case 1: Print Job Initialization and Properties
Objective: To verify that the print job classes correctly initialize and store properties.
Test Steps:
Create an instance of each job class (HighDetail, StandardDetail, FastPrint).
Check the initialization of properties like job_name, base_time, cost, and revenue.
Expected Results:
Each instance should have its respective properties set according to its class definition.
For example, HighDetail should have a base_time of 120 minutes, a cost of $45, and a revenue of $115.

Test Case 2: Material Time and Cost Modifier Application
Objective: To ensure that material subclasses correctly modify time and cost.
Test Steps:
Create an instance of each material class (PLA, ABS, Nylon).
Check the time_modifier and additional_cost for each material.
Expected Results:
PLA should add 5 minutes and $10 to the cost.
ABS should add 10 minutes and $20 to the cost.
Nylon should add 15 minutes and $30 to the cost.
"""
# HighDetail
100 # Budget
1 # Choose to make a job
3 # Type of Print
1 # Nylon
4 # End

# Standard Detail
100 # Budget
1 # Choose to make a job
2 # Type of Print
2 # ABS
4 # End

# FastPrint
100 # Budget
1 # Choose to make a job
1 # Type of Print
3 # PLA
4 # End

"""
Test Case 3: Job and Material Integration
Objective: To test if the Settings class correctly aggregates multiple materials' time and cost impacts on print jobs.
Test Steps:
Create instances of HighDetail and multiple materials.
Apply these materials to the job using the Settings class.
Calculate the total time and cost.
Expected Results:
The total time and cost should correctly reflect the sum of the base job time and cost plus all modifications from the materials.
"""
100 # Budget
1 # Choose to make a job
1 # Type of Print
1, 2 # Filament
2 # Review Job
4 # End

"""
Test Case 4: Budget Management in Job Processing
Objective: To confirm that the system correctly updates and respects the budget during job processing.
Test Steps:
Initialize the PrinterController with a set budget.
Process a job with settings that should exceed the available budget.
Attempt to process another job within the budget.
Expected Results:
The job exceeding the budget should not be processed, and an appropriate message should be displayed.
The job within the budget should be processed successfully, and the budget should be updated accordingly.
"""
40 # Budget
1 # Choose to make a job
1 # Type of Print
3 # Filament
# Exceeds Budget
2 # Review Job
1 # Choose to make a job
3 # Type of Print
1 # Filament
2 # Review Job
4 # End

"""
Test Case 5: Optimization Algorithm Accuracy
Objective: To assess the accuracy of the knapsack algorithm implementation in maximizing potential revenue.
Test Steps:
Populate the system with multiple jobs with known costs and revenues.
Run the optimize_jobs method to select the combination of jobs that maximizes revenue without exceeding the budget.
Expected Results:
The algorithm should select the combination of jobs that yields the highest possible revenue within the given budget constraints.
"""
######################## Need to add

"""
Test Case 6: System Interaction and Error Handling
Objective: To evaluate the systems response to user inputs and its ability to handle errors gracefully.
Test Steps:
Simulate user inputs with both valid and invalid data (such as non-numeric input where numbers are expected).
Check the systems response and error messages.
Expected Results:
The system should accept valid inputs without issue and perform the expected functions.
For invalid inputs, the system should display an error message and prompt the user to try again without crashing.
"""
100 # Budget
afnwue9 # Invalid input
2 # Review Job
1 # Choose to make a job
ed32 # Invalid input
1 # Type of Print
asdf123 # Invalid input
1 # Filament
ljka34 # Invalid input
4 # End
