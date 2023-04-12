import os
from dotenv import load_dotenv
from openai_helper import ask
from helper import read_file, write_file

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_changes(prompt):
    response = ask(prompt)
    return response.strip()

def update_files():
    files = [f.lower() for f in os.listdir()]

    if "goal.md" in files:
        goal = read_file("goal.md").strip()
    else:
        goal = "Create a new project"
        write_file("goal.md", goal)

    if "readme.md" in files:
        readme = read_file("readme.md").strip()
    else:
        readme = ""
        write_file("readme.md", "")

    if "repo.md" in files:
        repo = read_file("repo.md").strip()
    else:
        repo = ""

    prompt = f"""
    Access the GitHub repository from {repo}.
    Look at the readme.md file for assistance in interpreting the relationship of the files.
    Check the goal.md file to determine the next steps.
    Recommend specific file-level changes to one of the files, or to create a new file for the repository.
    Also, specify changes to be made to the goal.md and readme.md files to reflect the changes.

    Please be specific with your changes and provide context in the release_notes.md file.
    If a new Python file should be created, or an existing Python file edited, please specify the filename and what the file should be comprised of.

    Update the release_notes.md file with the changes made.

    """
    changes = get_changes(prompt)

    # Implement the logic for updating files, goal.md, readme.md, and release_notes.md
    change_lines = changes.split("\n")
    release_notes = ""

    for line in change_lines:
        if line.startswith("# Update goal.md"):
            goal = line.split(":")[-1].strip()
            write_file("goal.md", goal)
        elif line.startswith("# Update readme.md"):
            readme = line.split(":")[-1].strip()
            write_file("readme.md", readme)
        elif line.startswith("# Add to release_notes.md"):
            release_notes += line.split(":")[-1].strip() + "\n"

    if release_notes:
        if "release_notes.md" in files:
            with open("release_notes.md", "a") as notes_file:
                notes_file.write("\n\n")
                notes_file.write(release_notes)
        else:
            with open("release_notes.md", "w") as notes_file:
                notes_file.write("# Release Notes\n\n")
                notes_file.write(release_notes)

    print("All changes made successfully!")

if __name__ == "__main__":
    update_files()