"""secret_santa.py."""
import csv
import sys
import random
from getpass import getpass
from requirements import requirements
from send_email import send_email, format_message


def secret_santa(sender_email, seed):
    """Short summary.

    Parameters
    ----------
    sender_email : type
        Description of parameter `sender_email`.
    seed : type
        Description of parameter `seed`.

    Returns
    -------
    type
        Description of returned object.

    """
    names, emails = guest_list("guest_list.csv")
    givers, giver_emails, receivers = generate_pairs(names, emails, seed)
    password = getpass(prompt="Type your password and press enter: ")
    for i in range(len(givers)):
        print("Sending email to... {}".format(givers[i]))
        send_email(
            sender_email,
            password,
            giver_emails[i],
            format_message(givers[i], giver_emails[i], receivers[i]),
        )


def guest_list(file):
    """Load the guestlist (names, emails) for the event, in the format.

    Parameters
    ----------
    file : str
        path to guest list file

    Returns
    -------
    list[str]
        names from the guestlist file.
    list[str]
        emails for the names found in the guestlist file.

    """
    with open(file) as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        names = []
        emails = []
        for row in reader:
            names.append(row[0])
            emails.append(row[1])
    return names, emails


def generate_pairs(names, emails, seed=123):
    """Generate and validate pairs of gift givers and receivers for
    secret santa.

    Parameters
    ----------
    names : list[str]
        List of participants' names
    emails : list[str]
        List of participants' emails
    seed : int
        random seed to set (optional)

    Returns
    -------
    list[str]
        Participants to give gifts
    list[str]
        Giving participants' emails
    list[str]
        Partipant to receive gifts

    """
    gift_givers = names
    gift_receivers = names
    reqs_met = False
    random.seed(seed)
    count = 0
    while not reqs_met:
        count += 1
        gift_receivers = random.sample(gift_receivers, len(gift_receivers))
        reqs_met = requirements(gift_givers, gift_receivers)
        if count > 100:
            print(
                "*" * 70,
                "\nTried over 100 times... Could not find a suitable match."
                "\nExiting ... Try again with a different seed?",
            )
            sys.exit()
            break
    return gift_givers, emails, gift_receivers


if __name__ == "__main__":
    sender_email = sys.argv[1]
    seed = sys.argv[2]
    secret_santa(sender_email, seed)
