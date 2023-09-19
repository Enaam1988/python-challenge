import csv
import os

# Files to load and output (Remember to change these)
load_file = os.path.join("PyPoll","Resources", "election_data.csv")
output_file= os.path.join("PyPoll","analysis", "election_analysis.txt")

# Total Vote Counter
total_votes = 0

# Candidate list and Vote Counters
candidate_list = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0

# Read the csv and convert it into a list of dictionaries
with open(load_file) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row...
    for row in reader:

    
        # Add to the total vote count
        total_votes = total_votes + 1

        # Extract the candidate name from each row
        candidate_name = row[2]

        if candidate_name not in candidate_list:

            # Add it to the list of candidates in the running
            candidate_list.append(candidate_name)

            # candidate's voter count
            candidate_votes[candidate_name] = 0

        # Then add a vote to that candidate's count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

# Print the results and export the data to our text file
with open(output_file, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file
    txt_file.write(election_results)

    # Determine the winner by looping through the counts
    for candidate in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100
        #winning vote count and candidate
        if(votes > winning_count):
         winning_count = votes
         winning_candidate = candidate

        # Print each candidate's voter count and percentage (to terminal)
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

        # Save each candidate's voter count and percentage to text file
        txt_file.write(voter_output)
# Print the winning candidate (to terminal) 
    winner_candidate = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winner_candidate)

    # Save the winning candidate's name to the text file

    txt_file.write(winner_candidate) 

   
