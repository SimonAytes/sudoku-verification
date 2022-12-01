import threading

class column_thread(threading.Thread):
    # Boolean value for the status of the check
    is_valid = False
    column_to_check = -1
    solution = []

    def __init__(self, thread_name, thread_ID, col_index, solution):
        """Initialize new thread object"""
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.thread_ID = thread_ID

        # Specify the column which will be checked
        self.column_to_check = col_index

        # Load the solution
        self.solution = solution

    def run(self):
        """Check the relevant area of the sudoku solution."""
        #print(f"Column Thread: {self.thread_ID}")
        # Create an empty list for column
        col_vals = []
        truth_vals = []

        # Grab the column that was specified
        for row in self.solution:
            col_vals.append(row[self.column_to_check])

        # Cast all vals to int
        col_vals = [int(x) for x in col_vals]

        # Sort the list in ascending order
        # Determine that each value (1 thru 9) is present
        # If all numbers are present return true, otherwise return false
        self.is_valid = (sorted(col_vals) == list(range(1, 10)))

        #print(f"COLUMN\t\t{self.column_to_check}\t\t{self.is_valid}")
        
class row_thread(threading.Thread):
    # Boolean value for the status of the check
    is_valid = False
    row_to_check = -1
    solution = []

    def __init__(self, thread_name, thread_ID, row_index, solution):
        """Initialize new thread object"""
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.thread_ID = thread_ID

        # Specify the row which will be checked
        self.row_to_check = row_index

        # Load the solution
        self.solution = solution

    def run(self):
        """Check the relevant area of the sudoku solution."""
        #print(f"Row Thread: {self.thread_ID}")
        # Capture the solution row
        row_vals = self.solution[self.row_to_check]

        # Cast all vals to int
        row_vals = [int(x) for x in row_vals]

        # Sort the list in ascending order
        # Determine that each value (1 thru 9) is present
        # If all numbers are present return true, otherwise return false
        self.is_valid = (sorted(row_vals) == list(range(1, 10)))

        #print(f"ROW\t\t{self.row_to_check}\t\t{self.is_valid}")

class subgrid_thread(threading.Thread):
    # Boolean value for the status of the check
    is_valid = False
    subg_row = -1
    subg_col = -1
    solution = []

    def __init__(self, thread_name, thread_ID, row_index, col_index, solution):
        """Initialize new thread object"""
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.thread_ID = thread_ID

        # Specify the row/col which will be checked
        self.subg_row = row_index
        self.subg_col = col_index

        # Load the solution
        self.solution = solution

    def run(self):
        """Check the relevant area of the sudoku solution."""
        #print(f"Row Thread: {self.thread_ID}")
        # Capture the solution subgroup
        subg_vals = []

        for i in range(self.subg_row, self.subg_row + 3):
            row = self.solution[i]
            for j in range(self.subg_col, self.subg_col + 3):
                subg_vals.append(row[j])


        # Cast all vals to int
        subg_vals = [int(x) for x in subg_vals]

        # Sort the list in ascending order
        # Determine that each value (1 thru 9) is present
        # If all numbers are present return true, otherwise return false
        self.is_valid = (sorted(subg_vals) == list(range(1, 10)))

        #print(f"SUBGROUP\t(R:{self.subg_row}, C:{self.subg_col})\t{self.is_valid}")