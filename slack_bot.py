import os
import sys

import slack


def main():
    total = 0
    for line in sys.stdin:
        total += int(line.strip())

    client = slack.WebClient(token=os.environ['SLACK_API_TOKEN'])
    message = f'total balance of transactions from fraudulent users is {total}'
    client.chat_postMessage(channel='#automation', text=message)


if __name__ == '__main__':
    main()
