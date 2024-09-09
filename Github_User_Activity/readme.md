# GitHub User Activity CLI

The GitHub User Activity CLI is a simple command-line interface application that fetches and displays the recent activity of a GitHub user.

## Features

- Accepts a GitHub username as a command-line argument
- Fetches the user's recent activity using the GitHub API
- Displays the activity in a user-friendly format
- Handles errors gracefully, such as invalid usernames or API failures

## Usage

To use the GitHub User Activity CLI, follow these steps:

1. Ensure you have Python 3 installed on your system.
2. Save the `github_activity.py` file to your desired directory.
3. Open a terminal or command prompt and navigate to the directory containing the `github_activity.py` file.
4. Run the script with the GitHub username as an argument:

   ```
   python github_activity.py <username>
   ```

   Replace `<username>` with the GitHub username you want to fetch the activity for.

Example output:

```
- Pushed 3 commits to kamranahmedse/developer-roadmap
- Opened a new issue in kamranahmedse/developer-roadmap
- Starred kamranahmedse/developer-roadmap
- Created a new repository: kamranahmedse/gitflow-cheat-sheet
```

## Implementation Details

The GitHub User Activity CLI is implemented using Python 3. It fetches the user's recent activity using the GitHub API and displays the activity in a user-friendly format.

The main functions are:

- `get_user_activity(username)`: Fetches the user's recent activity from the GitHub API.
- `display_activity(events)`: Displays the fetched activity in the terminal.

The script uses the `requests` library to make the API requests and handles any errors that may occur during the requests.

## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request on the [GitHub repository](https://github.com/your-username/github-activity-cli).

## License

This project is licensed under the [MIT License](LICENSE).
