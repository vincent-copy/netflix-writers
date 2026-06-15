# Kaggle REST API

This project downloads data from Kaggle using the official Kaggle API.
Before running the data ingestion scripts, you must create and install a
Kaggle API token.

## Obtaining a Kaggle API Key

1. Create a Kaggle Account

   If you do not already have an account, create one at:

   [https://www.kaggle.com/](https://www.kaggle.com/)

2. Generate an API Token

   1. Sign in to Kaggle.
   2. Click your profile picture in the upper-right corner.
   3. Select Settings.
   4. Scroll down to the API section.
   5. Click Create New Token.

   Kaggle will download a file named:

   `kaggle.json`

   This file contains your API credentials.

3. Install the API Token

   Create the Kaggle configuration directory:

   ```console
   mkdir -p ~/.kaggle
   ```

   Move the downloaded token into the directory:

   ```console
   mv ~/Downloads/kaggle.json ~/.kaggle/kaggle.json
   ```

   Restrict the file permissions so that only your user account can read it:

   ```console
   chmod 600 ~/.kaggle/kaggle.json
   ```

4. Verify Your Configuration

   Run the following command:

   ```console
   kaggle datasets list -s netflix
   ```

   If your credentials are configured correctly, Kaggle will return a list of
   matching datasets.

## Troubleshooting

If you encounter an authentication error such as:

```console
OSError: Could not find kaggle.json
```

verify that:

- The file exists at ~/.kaggle/kaggle.json
- The file permissions are set to 600
- The file contains valid credentials generated from your Kaggle account

**Do not commit kaggle.json to source control. The file contains credentials
associated with your Kaggle account and should be treated like a password.**
