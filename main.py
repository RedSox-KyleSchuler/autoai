import os
from helper import read_file, write_file
from openai_helper import ask

# Get the current directory and list all the files
cwd = os.getcwd()
files = os.listdir(cwd)

# Check if there is a file called "goal.md"
if "goals.md" in files:
    # Read the contents of the "goal.md" file
    goal = read_file("goals.md")
    print("Goal:", goal)

    # Ask OpenAI for the next steps based on the current goal
    next_steps = ask(goal)

    # Print the suggested next steps and ask for confirmation
    print("Next steps:", next_steps)
    confirm = input("Do you want to proceed with these steps? (y/n) ")

    if confirm.lower() == "y":
        # Create a new file for the next steps
        new_file = "next_steps.md"
        write_file(new_file, next_steps)

        # Update the "goal.md" file with the completed steps and new goal
        completed_steps = f"- {goal}\n"
        new_goal = f"- {next_steps}"
        write_file("goals.md", completed_steps + new_goal)

        # Update the "release_notes.md" file with the changes
        release_notes = f"Added {new_file} with next steps:\n{next_steps}"
        write_file("release_notes.md", release_notes)
else:
    # Create a new "goal.md" file
    new_goal = "Learn Python"
    write_file("goals.md", f"- {new_goal}")

    # Update the "release_notes.md" file with the changes
    release_notes = f"Created new file: goals.md with goal: {new_goal}"
    write_file("release_notes.md", release_notes)
