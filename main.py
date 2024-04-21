'''
    File: main.py
    Description: This comprehensive program allows for management of print jobs at a 3D printer.
    Starting off with a user-defined budget, this software enables the user to input what
    print jobs they would like (from the specific quality (High, Standard, Fast) to the
    specific filament (PLA, ABS, Nylon)) as long as it fits within the remaining budget.
    Here, data structures such as queues and hash tables are implemented to keep track
    of the print jobs appropriately as well as access IDs quickly when needed to remove
    or search things up. Additionally, users can review all jobs processed in addition
    to optimizing the maximum number of the best quality print jobs they can get utilizing
    the knapsack algorithm in combination with a simulation of potential jobs to be added to
    see how much more their remaining budget can afford.

    Student Name: Douglas Pham
    Student UT EID: ddp2328
    Partner Name: Zachary Sepulveda
    Partner UT EID: zrs386
    Course Name: CS 313E
    Unique Number: 50775
    Date Created: 4/20/24
    Date Last Modified: 4/20/24
    Course Name: CS 313E
'''
from queue import Queue

class PrintJob:
    """
    Defines the base class for print jobs (whether it be high (slow), standard, or fast).
    This is the foundation all print jobs will build off of.
    """
    id_counter = 0 # Use this to keep track of last ID

    def __init__(self, job_name, base_time, cost):
        """
        Initializes PrintJob class with the type of job and base processing time
        """
        self.job_name = job_name
        self.base_time = base_time
        self.cost = cost
        self.job_id = PrintJob.id_counter  # Assign an ID to the job
        PrintJob.id_counter += 1  # Increment the ID counter to ensure uniqueness

    def get_time(self, settings):
        """
        Calculates the total time to complete the job based on the settings.
        """
        return self.base_time + settings.get_time()

    def __str__(self):
        """
        Returns a string including the job and its base time.
        """
        return f"{self.job_name}: Time = {self.base_time} mins, Cost = ${self.cost}"

class HighDetail(PrintJob):
    """
    Represents a high-detail print job.
    """
    def __init__(self):
        super().__init__("High Detail", 120, 45)  # Assume 120 minutes as the base time

class StandardDetail(PrintJob):
    """
    Represents a standard detail print job.
    """
    def __init__(self):
        super().__init__("Standard Detail", 60, 30)  # Assume 60 minutes as the base time

class FastPrint(PrintJob):
    """
    Represents a fast print job.
    """
    def __init__(self):
        super().__init__("Fast Print", 30, 15)  # Assume 30 minutes as the base time

class Material:
    """
    Base class for materials used in print jobs.
    """
    def __init__(self, material_type, time_modifier, cost):
        self.material_type = material_type
        self.time_modifier = time_modifier
        self.additional_cost = cost

    def get_time(self):
        """
        Returns the time modifier for the material.
        """
        return self.time_modifier

    def __str__(self):
        """
        Returns a string representation of the material.
        """
        return f"{self.material_type} (+{self.time_modifier} mins, +${self.additional_cost})"

class PLA(Material):
    """
    Represents a PLA material.
    """
    def __init__(self):
        super().__init__("PLA", 5, 10)

class ABS(Material):
    """
    Represents an ABS material.
    """
    def __init__(self):
        super().__init__("ABS", 10, 20)

class Nylon(Material):
    """
    Represents an ABS material.
    """
    def __init__(self):
        super().__init__("Nylon", 15, 30)

class Settings:
    """
    Combines different materials into a single setting for a print job.
    """
    def __init__(self, materials=[]):
        self.materials = materials

    def get_time(self):
        """
        Calculates the total time modifier from all materials.
        """
        return sum(material.get_time() for material in self.materials)
    
    def total_cost(self):
        return sum(m.additional_cost for m in self.materials)

    def __str__(self):
        """
        Returns a string representation of all materials used in the settings.
        """
        return ", ".join(str(material) for material in self.materials)

class PrinterController:
    """
    Controller class that manages the printer queue and processes commands.
    """
    def __init__(self,budget):
        """
        Initializes the PrinterController with a list of available print jobs.
        """
        self.job_classes = [HighDetail, StandardDetail, FastPrint]
        self.material_classes = [PLA, ABS, Nylon]
        # Create a dictionary to store jobs with respective IDs as keys
        self.job_dict = {}
        self.budget = budget
        self.job_queue = Queue() # Create job queue

    def select_job(self):
        """
        Allows the user to choose a print job from available options.
        """
        print("\nAvailable print job options:")
        for count, job_class in enumerate(self.job_classes, start = 1):
            # Display example instances of each job class
            print(f"{count}. {job_class().__str__()}")

        job_choice = 0
        while job_choice < 1 or job_choice > len(self.job_classes):
            job_choice = int(input("Please enter the number of your job choice: "))
            if job_choice < 1 or job_choice > len(self.job_classes):
                print("Invalid choice. Please enter the number 1, 2, or 3.")

        # Create a new instance of the selected job class
        selected_job = self.job_classes[job_choice - 1]()
        self.add_job_to_dict(selected_job)
            
        return selected_job

    def add_job_to_dict(self, job):
        """
        Adds a new job to the job dictionary.
        This ensures each job added is unique and has a unique ID.
        """
        self.job_dict[job.job_id] = job
        self.job_queue.enqueue(job.job_id)  # Add job ID to the queue
        print(f"\nAdded Job ID {job.job_id} to the system.")

    def get_job_by_id(self, job_id):
        """
        Retrieves a job from the job dictionary by its ID.
        """
        job = self.job_dict.get(job_id, None)
        if job is not None:
            return job
        else:
            print("Job ID not found!")
            return None
        
    def customize_job(self, job):
        """
        Allows the user to customize their selected job with different materials.
        """
        materials = []
        valid_choices = {1: PLA, 2: ABS, 3: Nylon}  # Maps valid choices to material classes
        
        print("\nAvailable materials:")
        for count, material_class in enumerate(self.material_classes, start = 1):
            # Display example instances of each material class
            print(f"{count}. {material_class().__str__()}")

        while True:
            choice_input = input("Enter the numbers of the materials you want to use separated by commas (e.g., 1,2): ")
            choices = list(map(int, choice_input.split(',')))  # Convert input to list of integers

            if all(choice in valid_choices for choice in choices):  # Use list comprehension to check if all entries are valid
                break
            else:
                print(f"Invalid choice. Please enter between 1-3 seperated by commas.")

        for choice in choices:
            if choice == 1:
                materials.append(PLA())
            elif choice == 2:
                materials.append(ABS())
            elif choice == 3:
                materials.append(Nylon())

        return Settings(materials)

    def process_job(self, job, settings):
        """
        Processes the selected job and prints the estimated completion time.
        """
        total_cost = job.cost + settings.total_cost()
        if self.budget >= total_cost:
            self.budget -= total_cost
            print(f"Processed {job} with settings {settings}. Total cost: ${total_cost}. Remaining budget: ${self.budget}")
            self.job_queue.dequeue()  # Remove job from queue after processing
        else:
            print("Not enough budget to process this job.")
            print(f"Job ID {job.job_id} was out of the budget, so it was removed.")
            self.job_dict.pop(job.job_id)
            self.job_queue.dequeue()  # Remove job from queue after rejecting/not processing
    
    def review_jobs(self):
        """
        Allows the user to review all jobs in the system by listing their IDs and details.
        """
        total_cost = sum(job.cost for job in self.job_dict.values())
        total_time = sum(job.base_time for job in self.job_dict.values())

        if not self.job_dict:
            print("No jobs currently in system.")
        else:
            print()
            for job_id, job in self.job_dict.items():
                print(f"Job ID {job_id}: {job}")
            print("----------------------------")
            print(f"Total cost: ${total_cost}")
            print(f"Total print time: {total_time} minutes")

    def simulate_job_addition(self, remaining_budget):
        """Simulate the addition of new jobs based on the remaining budget and calculate potential quantity of best prints."""
        potential_jobs = []
        for job_class in self.job_classes:
            while True:
                job = job_class()
                total_job_cost = job.cost + 10  # Add filament cost as well
                if total_job_cost <= remaining_budget:  # Check if another job can be afforded
                    potential_jobs.append(job)
                    remaining_budget -= job.cost  # Deduct the cost of the job from the remaining budget
                else:
                    break
        return potential_jobs

    def optimize_num_jobs(self):
        current_jobs = list(self.job_dict.values())
        remaining_budget = self.budget - sum(job.cost for job in current_jobs)
        potential_jobs = self.simulate_job_addition(remaining_budget)

        # Setting up weights and values for knapsack problem
        costs = [(job.cost + 10) for job in potential_jobs]  # Weights in knapsack (add 10 for cheapest filament cost)
        values = [1 for _ in potential_jobs]  # Max out number of high quality prints

        # Maximum number of jobs and which jobs to include
        max_value, chosen_jobs_indices = self.knapsack(remaining_budget, costs, values, len(costs))

        print(f"Max quantity of best prints (with cheapest filament ($10) achievable within budget: {max_value}")

        for index in chosen_jobs_indices:
            print(f"Included Job: {potential_jobs[index].job_name}, Total Cost: ${potential_jobs[index].cost + 10}, Value: {values[index]}")

    def knapsack(self, W, wt, val, n):
        K = [[0 for x in range(W + 1)] for _ in range(n + 1)]
        for i in range(1, n+1):
            for w in range(1, W+1):
                if wt[i-1] <= w:
                    K[i][w] = max(K[i-1][w], val[i-1] + K[i-1][w-wt[i-1]])
                else:
                    K[i][w] = K[i-1][w]

        # Finding out which items to include in the optimal set
        result = K[n][W]
        w = W
        items_selected = []
        for i in range(n, 0, -1):
            if result == K[i-1][w]:
                continue
            else:
                items_selected.append(i-1)
                result -= val[i-1]
                w -= wt[i-1]

        return K[n][W], items_selected

    def start(self):
        """
        Starts the main loop of the printer control program.
        """
        while True:
            print("\nWelcome to Texas InventionWork's Craftbot 3D printer queue management system!\n")
            print("1. Start a new print job")
            print("2. Review all jobs") # Show total cost and dollars in budget left
            print("3. Maximize Quantity") # Maximize the number of prints based on the total dollars left
            print("4. Exit")
            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                selected_job = self.select_job()
                settings = self.customize_job(selected_job)
                self.process_job(selected_job, settings)
            elif choice == '2':
                self.review_jobs()
            elif choice == '3':
                self.optimize_num_jobs()
            elif choice == '4':
                print("Thank you for using the printer. Goodbye!")
                break
            else:
                print("\nInvalid choice. Please enter 1, 2, or 3.")    

def main():
    """
    This will run the main function with the controller/UI
    allowing the user to input what they need for their work order.
    """
    initial_budget = int(input("Enter your starting budget ($): "))
    controller = PrinterController(initial_budget)
    controller.start()

if __name__ == "__main__":
    main()
