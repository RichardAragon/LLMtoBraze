# LLM to Braze

LLM to Braze is a Python application that integrates OpenAI's Large Language Model (LLM) with the Braze customer engagement platform to generate personalized email content for individual users based on their Braze profile data.

## Features

- Retrieves user data from Braze using the Braze User Export API
- Utilizes OpenAI's LLM to generate personalized email content based on user data
- Sends personalized emails to users using the Braze Messaging API
- Supports the use of email templates with editable sections for personalized content

## Requirements

- Python 3.x
- OpenAI API credentials
- Braze API credentials

## Installation

1. Clone the repository:
git clone https://github.com/your-username/llm-to-braze.git
Copy code
2. Install the required dependencies:
pip install -r requirements.txt
Copy code
3. Set up your API credentials:
- Replace `"your_openai_api_key"` with your actual OpenAI API key in the code.
- Replace `"your_braze_api_key"` with your actual Braze API key in the code.
- Replace `"your_app_id"` with your actual Braze app ID in the code.

## Usage

1. Prepare your email template:
- Define your email template in the `email_template` variable in the code.
- Use the `<LLM Editable>` tag to indicate the portion of the email that should be personalized by the LLM.

2. Specify the user IDs:
- Update the `user_ids` list in the `main` function with the desired user IDs for which you want to generate personalized emails.
