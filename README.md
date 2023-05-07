ChatGPT wrote this btw.

# pyMessage

Python-based application designed to automatically respond to iMessages using OpenAI's ChatGPT language model. 

## :sparkles: About

pyMessage is an AI-driven project that was originally built to have ChatGPT auto-respond to iMessages but gradually grew to include additional features. pyMessage can automatically reply to incoming iMessages, sync and monitor the iMessage database. It probably won't grow any more from here though.

## :rocket: Features

* Auto-respond to incoming iMessages using OpenAI's ChatGPT
* Sync iMessage database to an external folder
* Monitor the iMessage database for new incoming messages
* Easily configurable settings (ish???)

## :wrench: Configuration
To use this application, you will need to create a `config.ini` file in the root directory of the project with the following format:

```ini
[database]
path = /Users/yourusername/Library/Messages
db_file = /Users/yourusername/Library/Messages/chat.db
write_ahead_file = /Users/yourusername/Library/Messages/chat.db-wal
db_copy_path = /Users/yourusername/Desktop/iMessage

[openai]
api_key = your open api key
prompt = system prompt to influence chat gpt completion.
```
# Config Documentation

This documentation provides instructions on how to use the following configuration file:

## Database

The database section of the configuration file contains the following parameters:

- `path`: The path to the directory containing the iMessage database.
- `db_file`: The path to the iMessage database file.
- `write_ahead_file`: The path to the iMessage write-ahead log file.
- `db_copy_path`: The path to the directory where the iMessage database will be copied.

## OpenAI

The OpenAI section of the configuration file contains the following parameters:

- `api_key`: The API key to use for the OpenAI service.
- `prompt`: The prompt to use for generating responses using the OpenAI service.

To use this configuration file, update the values of the parameters as necessary and use it in your code by loading the configuration file and accessing the parameters.

Replace `yourusername` with your actual username, and `your_api_key` with your OpenAI API key. The `path` variable should point to the directory containing your iMessage database (`chat.db`). The `db_copy_path` variable should point to the directory where you want to copy the database for syncing. The `db_file` variable should be the full path to your iMessage database (`chat.db`).

You can obtain an OpenAI API key by signing up for their [API access](https://beta.openai.com/signup/) and following their instructions.
