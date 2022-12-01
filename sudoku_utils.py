import csv
import thread_manager_utils as tmu

# File Importer
class FileImporter:
    """Importer class that parses the input file"""
    file_path = ""

    def __init__(self):
        self.file_path = input("\tInput file path: ")

    def __parse_input_file__(self):
        with open(self.file_path, 'r') as read_obj:
            csv_reader = csv.reader(read_obj)
            csv_list = list(csv_reader)

        # Return list
        return csv_list

    def load_solution_file(self):
        return self.__parse_input_file__()


# Solution Checker
class SolutionChecker:
    # Variables
    soduku_solution = []
    thread_list = []

    def __init__(self):
        """Initialize the SolutionChecker object, prompt for file"""
        # Load the solution file and store as a list
        file_importer = FileImporter()
        self.soduku_solution = file_importer.load_solution_file()

    def create_threads(self):
        """Create all threads to be used"""
        thread_id = 0

        # Create column threads
        for i in range(0, 9):
            self.thread_list.append(tmu.column_thread(thread_id, thread_id, i, self.soduku_solution))
            thread_id += 1

        # Create row threads
        for i in range(0, 9):
            self.thread_list.append(tmu.row_thread(i, i, i, self.soduku_solution))
            thread_id += 1

        # Create subgrid threads
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                self.thread_list.append(tmu.subgrid_thread(i, i, i, j, self.soduku_solution))
            thread_id += 1

    def start_threads(self):
        """Start all of the threads in the thread list"""
        for thread in self.thread_list:
            thread.start()

    def verify(self):
        """Verify the solution of the soduku puzzle via each threa's truth value"""
        truth_vals = []

        for t in self.thread_list:
            truth_vals.append(t.is_valid)

        if False in truth_vals:
            print("\n\tSolution Valid: FALSE")
        else:
            print("\n\tSolution Valid: TRUE")