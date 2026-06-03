import os


EMAIL_FOLDER = "data/emails"


def load_emails():

    emails = []

    for file in os.listdir(
        EMAIL_FOLDER
    ):

        path = os.path.join(
            EMAIL_FOLDER,
            file
        )

        with open(
            path,
            encoding="utf-8"
        ) as f:

            emails.append(
                f.read()
            )

    return emails


if __name__ == "__main__":

    emails = load_emails()

    print(
        f"Loaded {len(emails)} emails"
    )