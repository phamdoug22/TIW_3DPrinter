1. What is your project idea about?
Texas InventionWorks is debuting software that was created with Sepulveda-Pham Software Company to manage an entire 3D printing service, from many types of print jobs to various materials, under a set budget while ensuring the most high-quality outputs. Their jobs and materials are varied, from which to choose. For a variety of choices that are possible, each has their own cost, revenue, and time. Once the software identifies all possible choices a user needs to make, it provides the least-cost combination, which will optimize profit within these sets of constraints. This tool would ultimately make use of two particular fields: Mechanical Engineering, with the use of the Texas Inventionworks facility and 3D printers present in it, and Finance, in terms of the optimization and maximization of potential revenue the 3D printer is able to bring in.

2. If you use any datasets, describe the dataset and provide how one can access and download it.
The entire program is built entirely on predefined classes and methods within the program itself, which can ultimately handle the creation and management of print jobs, materials, and budget considerations.

3. Describe your design for main packages, classes, methods, functions, and iterations between them.
PrintJob (Base Class)
The PrintJob class acts as a template or base class for different kinds of print jobs. All common attributes, like job name, base time, cost, revenue, profit, and job ID, are enclosed within the class. The class that includes methods to initialize a new print job, calculate the total time it would take for completion, including modifications for materials and time, and provide a string representation for the print job.

HighDetail, StandardDetail, FastPrint (Subclasses of PrintJob)
There are three subclasses of the PrintJob class: HighDetail, StandardDetail, and FastPrint. They each take care of the different levels of print detail and speed. These subclasses are further instantiated with specified attributes, related to the processing time, cost, and expected revenue set, using the constructor of the base class, so as to assure consistency in handling such job-related data.

Material (Base Class)
The Material class is a base class for all the material that is present in print jobs. It will manage all the attributes of the given material: type of material, time modifier, and additional cost. This class provides a method that returns the time change for a material and a string description that shows the impact that a material has on the time of processing jobs and its costing.

PLA, ABS, Nylon (Subclasses of Material)
PLA, ABS, and Nylon are all inheriting subclasses of the Material class. They represent printing materials of the type. Every class has its unique modifiers and costs related to time, which are all defined upon initialization.These materials affect the overall time and cost of print jobs when selected and used in printing settings.

Settings
The Settings class represents the combination of the materials selected for printing. It has the attribute to hold a list of selected materials and methods that allow computing time and costs based on materials used.

PrinterController
The most central point is PrinterController, which manages the queue of print, commands to be executed, and more. It has a collection of print job types, a defined collection of print jobs, and an attribute for budget. This includes the selection for print jobs and customization, process, and review jobs, simulation in the review of job selection so that there occurs addition of new jobs based on budget constraints, and selection of jobs for maximum revenue with an approach-based knapsack algorithm. This class is also responsible for handling the user's interaction with the system through the command-line interface by giving him hints on the functionalities offered by the system. The design has a modular architecture, hence ensures the scalability and easy upgradability to include new types of jobs or new material options without great changes in the core architecture. Every class is designed for a certain part of the printing process, starting with creating a job and choosing materials up to managing finances and user interactions, in order to provide a finished solution for 3D printing service.




4. Describe any libraries that you use.
We did not use any additional third-party libraries to run the functionalities outlined above. 

5. Design some Test cases that can test the correctness of your software.
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

Test Case 3: Job and Material Integration
Objective: To test if the Settings class correctly aggregates multiple materials' time and cost impacts on print jobs.
Test Steps:
Create instances of HighDetail and multiple materials.
Apply these materials to the job using the Settings class.
Calculate the total time and cost.
Expected Results:
The total time and cost should correctly reflect the sum of the base job time and cost plus all modifications from the materials.

Test Case 4: Budget Management in Job Processing
Objective: To confirm that the system correctly updates and respects the budget during job processing.
Test Steps:
Initialize the PrinterController with a set budget.
Process a job with settings that should exceed the available budget.
Attempt to process another job within the budget.
Expected Results:
The job exceeding the budget should not be processed, and an appropriate message should be displayed.
The job within the budget should be processed successfully, and the budget should be updated accordingly.

Test Case 5: Optimization Algorithm Accuracy
Objective: To assess the accuracy of the knapsack algorithm implementation in maximizing potential revenue.
Test Steps:
Populate the system with multiple jobs with known costs and revenues.
Run the optimize_jobs method to select the combination of jobs that maximizes revenue without exceeding the budget.
Expected Results:
The algorithm should select the combination of jobs that yields the highest possible revenue within the given budget constraints.

Test Case 6: System Interaction and Error Handling
Objective: To evaluate the system’s response to user inputs and its ability to handle errors gracefully.
Test Steps:
Simulate user inputs with both valid and invalid data (such as non-numeric input where numbers are expected).
Check the system’s response and error messages.
Expected Results:
The system should accept valid inputs without issue and perform the expected functions.
For invalid inputs, the system should display an error message and prompt the user to try again without crashing.

6. What is your current expectations of your software? For example, do you expect that it works well?
Currently, we expect the software will work well. We expect it to perform efficiently in managing print jobs and materials while optimizing financial outcomes using a knapsack algorithm for revenue maximization. The system's design facilitates seamless integration of user choices into time and cost calculations, ensuring users can make informed decisions based on their budget constraints.

A key functionality includes the ability to analyze various combinations of print jobs and materials to determine the optimal mix that maximizes revenue without exceeding the budget. This revenue optimization feature, powered by the knapsack algorithm, is critical for achieving the highest profitability possible under given financial conditions.

The software also features an intuitive user interface that simplifies the process of job selection, customization, and management, making it accessible even to users with no prior technical knowledge. This interface supports easy navigation and interaction with the system’s functions, enhancing user experience and efficiency.

Overall, the expectation is that the software will not only streamline the logistical aspects of 3D printing but also provide strategic insights to improve profitability, thereby serving as a valuable tool for users in diverse educational and commercial environments.

7. What are the expected weaknesses?
The 3D printer queue management system, designed to optimize print job scheduling and material use, exhibits potential weaknesses that could affect its utility and user experience. One significant concern is the complexity of the knapsack algorithm used for revenue optimization. While powerful, this algorithm requires careful tuning and can be computationally intensive, potentially leading to slower response times during high-demand scenarios or when handling a large number of job entries.

Another possible weakness is the system's reliance on user input for operations, which could lead to errors if the input is incorrect or not in the expected format. This dependency increases the risk of operational disruptions and could complicate usage for those unfamiliar with such systems.


Example Catalog for Tools
https://inventionworks.engr.utexas.edu/facilities/equipment

