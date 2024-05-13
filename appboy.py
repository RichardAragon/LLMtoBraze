import openai
import requests
import json

# Set up OpenAI API credentials
openai.api_key = "your_openai_api_key"

# Set up Braze API credentials
braze_api_key = "your_braze_api_key"
braze_api_url = "https://rest.iad-01.braze.com"

# Email template
email_template = """
Subject: Personalized Email for {{first_name}}

Dear {{first_name}},

<LLM Editable>
We hope this email finds you well. We wanted to reach out and offer a personalized message just for you.
</LLM Editable>

Thank you for being a valued customer.

Best regards,
The Team
"""

# Function to retrieve user data from Braze
def get_user_data(user_id):
    endpoint = f"{braze_api_url}/users/export/ids"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {braze_api_key}"
    }
    data = {
        "user_ids": [user_id],
        "fields_to_export": [
            "external_id",
            "first_name",
            "last_name",
            "email",
            "country",
            "language",
            "gender",
            "total_revenue",
            "last_purchase_date",
            "last_used_app",
            "last_used_platform",
            "custom_attributes"
        ]
    }
    response = requests.post(endpoint, headers=headers, data=json.dumps(data))
    user_data = response.json()["users"][0]
    return user_data

# Function to generate personalized email content using OpenAI
def generate_email_content(user_data, email_template):
    prompt = f"Given the following user data: {user_data}\n\nAnd the email template:\n{email_template}\n\nPlease fill in the content within the <LLM Editable> tag to create a personalized email body for the user."
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.7,
    )
    email_body = response.choices[0].text.strip()
    return email_body

# Function to send personalized email using Braze API
def send_email(user_id, email_content):
    endpoint = f"{braze_api_url}/messages/send"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {braze_api_key}"
    }
    data = {
        "messages": [{
            "to_user_id": user_id,
            "email": {
                "app_id": "your_app_id",
                "subject": email_content.split("\n")[0].replace("Subject: ", ""),
                "body": email_content.split("\n", 1)[1].strip()
            }
        }]
    }
    response = requests.post(endpoint, headers=headers, data=json.dumps(data))
    return response.status_code

# Main function to orchestrate the process
def main():
    # List of user IDs to generate personalized emails for
    user_ids = ["user_id_1", "user_id_2", "user_id_3"]

    for user_id in user_ids:
        # Retrieve user data from Braze
        user_data = get_user_data(user_id)

        # Generate personalized email content using OpenAI
        email_content = generate_email_content(user_data, email_template)

        # Replace template variables with user data
        email_content = email_content.replace("{{first_name}}", user_data["first_name"])

        # Send personalized email using Braze API
        status_code = send_email(user_id, email_content)
        print(f"Email sent to user {user_id} with status code {status_code}")

if __name__ == "__main__":
    main()
