# Self-Regenerating Program

This repository contains code for a self-regenerating program that uses OpenAI's GPT-3 API to generate new code and integrate it into the existing codebase.
As openai chat api is capable of generating code, my idea is to start with some basic code that can take a simple idea, and ask openAI to generate some code for that idea.
after that, the base code would take the code that openAI wrote, convert it into actual code, integrate it into the base code, and then rerun itself.
The code should all be writted in python


## Files

- main.py: This is the main file that runs the program.
- openai.py: This file contains the code to interact with the OpenAI GPT-3 API.
- helper.py: This file contains some helper functions.
- utils.py: This file contains some utility functions.
- goals.md: This file contains the project goals and steps to achieve them.
- readme.md: This file provides an overview of the repository and its contents.

## Usage

To use this program, run the main.py file. The program will automatically gather all files in the repository, check for a goals.md and readme.md file, and create blank versions of those files if they don't exist. The program will then submit the data to the OpenAI API, interpret the response, and suggest changes to existing Python files or the creation of new Python files as needed. The program will update the readme.md and goals.md files to reflect the changes, and then rerun itself to repeat the process.

## Contributing

If you'd like to contribute to this program, please submit a pull request.

## Dependencies

This program requires the following dependencies:

- OpenAI
- Requests
- python-dotenv

## License

This program is licensed under the MIT License.
