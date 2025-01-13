import argparse

from dotenv import load_dotenv

import airevise


def get_args():
    parser = argparse.ArgumentParser(
        description="Quickly revise your emails and Slack messages with ChatGPT."
    )

    parser.add_argument(
        "message",
        help="The original message text.",
    )

    msg_type = parser.add_mutually_exclusive_group()
    msg_type.add_argument(
        "-s", "--slack", action="store_true", help="This is a Slack message."
    )
    msg_type.add_argument(
        "-e", "--email", action="store_true", help="This is an email."
    )

    return parser.parse_args()


args = get_args()
load_dotenv()

client = airevise.RevisionClient()
original_text = str(args.message)

if args.slack:
    msg_type = airevise.MessageType.SLACK
else:
    msg_type = airevise.MessageType.EMAIL

revised_text = client.get_revision(original_text, msg_type)

print(revised_text)
