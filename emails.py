import re

# emails.txt file read karna
with open("emails.txt", "r") as file:
    content = file.read()

# Email addresses find karna
emails = re.findall(
    r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    content
)

# Emails ko new file mein save karna
with open("extracted_emails.txt", "w") as file:
    for email in emails:
        file.write(email + "\n")

print("Emails extracted successfully!")