# Netflix Writer

[![License: GNU AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)<br>[![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)](https://www.python.org/)
[![Pydantic](https://img.shields.io/badge/Pydantic-2.13-blue?logo=pydantic)](https://docs.pydantic.dev/)
org/)<br>[![hack.d Lawrence McDaniel](https://img.shields.io/badge/Author-Lawrence%20McDaniel-orange.svg)](https://lawrencemcdaniel.com)

This repo contains source code for ...
Netflix AI Greenlight Challenge: Can Data Science Predict the Next Hit Drama?

## Quickstart

## Obtaining a Kaggle API Key

This project downloads data from Kaggle using the official Kaggle API.
Before running the data ingestion scripts, you must create and install a
Kaggle API token.

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

   kaggle datasets list -s netflix

   If your credentials are configured correctly, Kaggle will return a list of matching datasets.

   Troubleshooting

   If you encounter an authentication error such as:

   OSError: Could not find kaggle.json

   verify that:

   - The file exists at ~/.kaggle/kaggle.json
   - The file permissions are set to 600
   - The file contains valid credentials generated from your Kaggle account

**Do not commit kaggle.json to source control. The file contains credentials
associated with your Kaggle account and should be treated like a password.**

## Support

Please report bugs to the [GitHub Issues Page](https://github.com/netflix-writers/netflix/issues)
for this project.
