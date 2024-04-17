class PrintJob:
    """
    Defines the base class for print jobs (whether it be high (slow), standard, or fast).
    This is the foundation all print jobs will build off of.
    """
    id_counter = 0 # Use this to keep track of last ID

    def __init__(self, job_name, base_time):
        """
        Initializes PrintJob class with the type of job and base processing time
        """
        self.job_name = job_name
        self.base_time = base_time
        self.job_id = PrintJob.id_counter  # Assign an ID to the job
        PrintJob.id_counter += 1  # Increment the ID counter to ensure uniqueness

    def get_time(self, settings):
        """
        Calculates the total time to complete the job based on the settings.
        """
        return self.base_time + settings.get_time()

    def __str__(self):
        """
        Returns a string representation of the job and its base time.
        """
        return f"{self.job_name}: {self.base_time} minutes"

class HighDetail(PrintJob):
    """
    Represents a high-detail print job.
    """
    def __init__(self):
        super().__init__("High Detail", 120)  # Assume 120 minutes as the base time

class StandardDetail(PrintJob):
    """
    Represents a standard detail print job.
    """
    def __init__(self):
        super().__init__("Standard Detail", 60)  # Assume 60 minutes as the base time

class FastPrint(PrintJob):
    """
    Represents a fast print job.
    """
    def __init__(self):
        super().__init__("Fast Print", 30)  # Assume 30 minutes as the base time

class Material:
    """
    Base class for materials used in print jobs.
    """
    def __init__(self, material_type, time_modifier):
        self.material_type = material_type
        self.time_modifier = time_modifier

    def get_time(self):
        """
        Returns the time modifier for the material.
        """
        return self.time_modifier

    def __str__(self):
        """
        Returns a string representation of the material.
        """
        return f"{self.material_type} (+{self.time_modifier} mins)"

class PLA(Material):
    """
    Represents a PLA material.
    """
    def __init__(self):
        super().__init__("PLA", 5)

class ABS(Material):
    """
    Represents an ABS material.
    """
    def __init__(self):
        super().__init__("ABS", 10)

class Nylon(Material):
    """
    Represents an ABS material.
    """
    def __init__(self):
        super().__init__("Nylon", 15)

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

    def __str__(self):
        """
        Returns a string representation of all materials used in the settings.
        """
        return ", ".join(str(material) for material in self.materials)

class PrinterController:
    """
    Controller class that manages the printer queue and processes commands.
    """
    def __init__(self):
        """
        Initializes the PrinterController with a list of available print jobs.
        """
        self.jobs = [HighDetail(), StandardDetail(), FastPrint()]
        # Create a dictionary to store jobs with respective IDs as keys
        self.job_dict = {}  

    def select_job(self):
        """
        Allows the user to choose a print job from available options.
        """
        print("Available print job options:")
        for count, job in enumerate(self.jobs, start = 1):
            print(f"{count}. {job}")

        job_choice = 0
        while job_choice < 1 or job_choice > len(self.jobs):
            job_choice = int(input("Please enter the number of your job choice: "))
        
        selected_job = self.jobs[job_choice - 1]
        self.add_job_to_dict(selected_job)  # Add job to the dictionary for tracking
        
        return selected_job
    
    def add_job_to_dict(self, job):
        """
        Adds a new job to the job dictionary.
        """
        self.job_dict[job.job_id] = job

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
        total_time = job.get_time(settings)
        print(f"Your print job {job} with settings {settings} will take approximately {total_time} minutes.")
    
    def review_jobs(self):
        """
        Allows the user to review all jobs in the system by listing their IDs and details.
        """
        if not self.job_dict:
            print("No jobs currently in system.")
        else:
            for job_id, job in self.job_dict.items():
                print(f"Job ID {job_id}: {job}")

    def start(self):
        """
        Starts the main loop of the printer control program.
        """
        while True:
            print("\nWelcome to Texas InventionWork's Craftbot 3D printer queue management system!\n")
            print("1. Start a new print job")
            print("2. Review all jobs")
            print("3. Exit")
            choice = input("Enter your choice (1-3): ")

            if choice == '1':
                selected_job = self.select_job()
                settings = self.customize_job(selected_job)
                self.process_job(selected_job, settings)
            elif choice == '2':
                self.review_jobs()
            elif choice == '3':
                print("Thank you for using the printer. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
    
    

def main():
    """
    This will run the main function with the controller/UI
    allowing the user to input what they need for their work order.
    """
    controller = PrinterController()
    controller.start()

if __name__ == "__main__":
    main()
