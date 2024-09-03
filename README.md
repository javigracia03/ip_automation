
# IP Change Notifier

This is a Python script that monitors your public IP address and sends an email notification when the IP address changes. The script is designed to run on a schedule (e.g., using a cron job) and automatically alert you when your IP changes, which can be useful for remote access setups or servers with dynamic IP addresses.

## Features

- **IP Monitoring**: Fetches the current public IP address from an external service.
- **Email Notification**: Sends an email alert when the public IP address changes.
- **Persistent IP Tracking**: Stores the last known IP address in a text file.

## Requirements

- Python 3.x
- Internet connection
- Gmail account for sending emails

## Setup

### 1. Clone the Repository

Clone the repository to your local machine:

\`\`\`bash
git clone https://github.com/your-username/ip-change-notifier.git
cd ip-change-notifier
\`\`\`

### 2. Install Required Libraries

The script uses Python's built-in libraries, so no additional installations are required.

### 3. Configure Email Credentials

#### Option 1: Using Environment Variables

Set your email credentials as environment variables. This method keeps your credentials secure and avoids hardcoding sensitive information:

\`\`\`bash
export EMAIL_USERNAME='your_email@gmail.com'
export EMAIL_PASSWORD='your_password'
\`\`\`

On Windows, you can set these in the Command Prompt:

\`\`\`cmd
set EMAIL_USERNAME=your_email@gmail.com
set EMAIL_PASSWORD=your_password
\`\`\`

#### Option 2: Using a Configuration File

Alternatively, store your email credentials in a \`config.ini\` file:

1. Create a file named \`config.ini\` in the project directory.
2. Add the following content to \`config.ini\`:

    \`\`\`ini
    [EMAIL]
    USERNAME = your_email@gmail.com
    PASSWORD = your_password
    \`\`\`

3. Add \`config.ini\` to your \`.gitignore\` file to prevent it from being tracked by Git.

### 4. Run the Script

You can run the script manually:

\`\`\`bash
python3 ip_notifier.py
\`\`\`

### 5. Set Up as a Cron Job (Optional)

To automatically check your IP address at regular intervals, you can set up a cron job. For example, to check every hour:

1. Open your crontab file:

    \`\`\`bash
    crontab -e
    \`\`\`

2. Add the following line:

    \`\`\`bash
    0 * * * * /usr/bin/python3 /path/to/your/script/ip_notifier.py
    \`\`\`

This schedules the script to run every hour.

## License

This project is licensed under the MIT License. See the \`LICENSE\` file for more details.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to improve the project.

## Contact

For any inquiries or suggestions, please contact [your_email@gmail.com](mailto:your_email@gmail.com).
