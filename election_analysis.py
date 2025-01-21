import csv
import os

def analyze_election_results(file_path):
    try:
        # Initialize variables
        total_votes = 0
        candidates = {}
        winner = None

        # Read the election results file
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            
            # Process each vote
            for row in reader:
                total_votes += 1
                candidate = row['Candidate']  # Assuming the column name is 'Candidate'

                # Count votes for each candidate
                if candidate in candidates:
                    candidates[candidate] += 1
                else:
                    candidates[candidate] = 1

        # Display results
        print("\nElection Results")
        print("-" * 30)
        print(f"Total Votes: {total_votes}")
        print("-" * 30)

        # Calculate vote percentages and determine the winner
        max_votes = 0
        for candidate, votes in candidates.items():
            percentage = (votes / total_votes) * 100
            print(f"{candidate}: {percentage:.2f}% ({votes} votes)")

            if votes > max_votes:
                max_votes = votes
                winner = candidate

        print("-" * 30)
        print(f"Winner: {winner}")
        print("-" * 30)

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except KeyError:
        print("Error: Make sure the file contains a 'Candidate' column.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function to execute the script
if __name__ == "__main__":
    # Path to the election results CSV file
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "data", "election_data.csv")

    analyze_election_results(file_path)
