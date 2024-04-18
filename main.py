"""
Major Finance + MechE
3D Printer w/ Finance Optimization Integrated

At the beginning, you get $$$$ + Time
From there you can optimize the numbero f high qualtiy print jobs you can do


say you get a budget to spend
"""

class PrintJob:
    """
    Defines the base class for print jobs (whether it be high (slow), standard, or fast).
    This is the foundation all print jobs will build off of.
    """
    id_counter = 0 # Use this to keep track of last ID

    def __init__(self, job_name, base_time, cost, profit):
        """
        Initializes PrintJob class with the type of job and base processing time
        """
        self.job_name = job_name
        self.base_time = base_time
        self.cost = cost
        self.profit = profit
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
        super().__init__("High Detail", 120, 45, 25)  # Assume 120 minutes as the base time

class StandardDetail(PrintJob):
    """
    Represents a standard detail print job.
    """
    def __init__(self):
        super().__init__("Standard Detail", 60, 30, 15)  # Assume 60 minutes as the base time

class FastPrint(PrintJob):
    """
    Represents a fast print job.
    """
    def __init__(self):
        super().__init__("Fast Print", 30, 15, 5)  # Assume 30 minutes as the base time

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
        # Create a dictionary to store jobs with respective IDs as keys
        self.job_dict = {}
        self.budget = budget

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
        print("\nAvailable materials:")
        print("1. PLA")
        print("2. ABS")
        print("3. Nylon")
        choice = input("Enter the numbers of the materials you want to use separated by commas: ")
        choices = map(int, choice.split(','))

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
        else:
            print("Not enough budget to process this job.")
    
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

    def optimize_jobs(self):
        profits = [job.profit for job in self.job_dict.values()] 
        weights = [job.cost for job in self.job_dict.values()]
        num_items = len(profits)
        max_value = PrinterController.knapsack(self.budget, weights, profits, num_items)  # Call as static method
        print(f"Maximum profit for TIW achievable with current budget (${self.budget}): ${max_value}")

    @staticmethod
    def knapsack(W, wt, val, n):
        K = [[0 for x in range(W + 1)] for x in range(n + 1)]
        for i in range(n + 1):
            for w in range(W + 1):
                if i == 0 or w == 0:
                    K[i][w] = 0
                elif wt[i-1] <= w:
                    K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
                else:
                    K[i][w] = K[i-1][w]
        return K[n][W]   
    

    def start(self):
        """
        Starts the main loop of the printer control program.
        """
        while True:
            print("\nWelcome to Texas InventionWork's Craftbot 3D printer queue management system!\n")
            print("1. Start a new print job")
            print("2. Review all jobs") # Show total cost and dollars in budget left
            print("3. Maximize Profit") # Maximize revenue based on the total dollars left
            print("4. Exit")
            choice = input("Enter your choice (1-3): ")

            if choice == '1':
                selected_job = self.select_job()
                settings = self.customize_job(selected_job)
                self.process_job(selected_job, settings)
            elif choice == '2':
                self.review_jobs()
            elif choice == '3':
                self.optimize_jobs()
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
