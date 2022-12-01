import sudoku_utils as sdu

# Create a solution checker object
checker = sdu.SolutionChecker()

# Create the threads
checker.create_threads()

# Start the threads
checker.start_threads()

# Verify the solution
checker.verify()

print("\n\t(Made by Simon Aytes, CMP426, Fall 2022)")