# ChatLan Contributing Guidelines
Thank you for your interest in contributing to ChatLan! We welcome contributions from the community to help improve our project. Please read the following guidelines to ensure a smooth contribution process.


## requirements
- Basic knowledge of Git and GitHub.
- Familiarity with the Python programming language.
- Understanding of Python packaging and distribution.
- Familiarity with Poetry for dependency management.
- Familirity with Terminals and Command Lines.
if you're looking for the Code of Conduct, please refer to [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## How to Contribute
0. talk to us on Discord or GitHub Discussions before making any changes (people don't like it when you don't talk to us first especially **Mobsy** the creator of ChatLan).
1. **Fork the Repository**: Start by forking the ChatLan repository to your GitHub account.

2. **Clone the Forked Repository and install the local dependencies**: Clone your forked repository to your local machine using:
   ```
   git clone the/url/of/your/forked/repo.git
   ```
   - 2.1 Navigate to the project directory:
   ```bash
   cd repo-name
   ```
   - 2.2 Install Poetry if you haven't already. 
   Follow the instructions at [Poetry's official website](https://python-poetry.org/docs/#installation) to install Poetry.
   - 2.3 Install the project dependencies using Poetry:
   ```bash
   poetry install
   ```

> [!TIP]
> To run the unit tests, you must install the optional test dependencies group by running:
> ```bash
> poetry install --with test
> ```

> [!NOTE]
> Although ChatLan is compatible with Windows, we highly recommend using a Unix-based system (Linux or macOS) for development to avoid potential compatibility issues since our major tests are runned there.


3. **Create a New Branch**: Create a new branch for your feature or bug fix:
   ```
   git checkout -b your-feature-branch
   ```
4. **Make Your Changes**: Implement your feature or fix the bug. Ensure your code follows the project's coding standards, if the changes alter the user experience, write a separate NEW_FEATURE.md file for the developers.

5. **Commit Your Changes**: Commit your changes with a descriptive message:
   ```
   git commit -m "Description of your changes"
   ```  
6. **Push to Your Fork**: Push your changes to your forked repository:
   ```
   git push origin your-feature-branch
   ```
7. **Create a Pull Request**: Go to the original ChatLan repository and create a pull request from your forked repository's branch to the main branch of ChatLan. Provide a clear description of your changes and why they are needed.

## Conventions
- Follow the existing coding style and conventions used in the project.
### rules
   - as you see because this is an open source project, we have to follow certain rules.
   - be respectful to others.
   - do not spam issues or pull requests.
   - make sure your code is well-documented.
   - test your changes thoroughly before submitting a pull request.
   - always talk to us on Discord or GitHub Discussions before making any changes.
   - thank you for contributing to ChatLan!

## Code of Conduct
By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md). Please be respectful and considerate to all members of the community.   

-- Mobsy and the ChatLan Team --