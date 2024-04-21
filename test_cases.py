"""
Test Case 1: Print Job Initialization and Properties
Test Case 2: Material Time and Cost Modifier Application
"""
# HighDetail
100 # Budget
1 # Choose to make a job
1 # Type of Print
3 # Nylon
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
3 # Type of Print
1 # PLA
4 # End

"""
Test Case 3: Job and Material Integration
"""
100 # Budget
1 # Choose to make a job
1 # Type of Print
1, 2 # Filament
2 # Review Job
4 # End

"""
Test Case 4: Budget Management in Job Processing
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
Test Case 5: Maximum Quantity Test
"""
95 # Budget
3 # Choose to see the maximum quantity
4 # End

"""
Test Case 6: System Interaction and Error Handling
"""
100 # Budget
asdf1234 # Invalid input
2 # Review Job
1 # Choose to make a job
8 # Invalid input
1 # Type of Print
7 # Invalid input
1 # Filament
10 # Invalid input
4 # End