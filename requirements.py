"""requirements.py."""
import csv


def requirements(giver_list, receiver_list):
    """Check requirements for secret santa givers and receivers.

    Check the following:
        - Couples cannot give to each other
        - No one can give to themselves
        - No two people have each other (short circuit)

    Parameters
    ----------
    giver_list : list[str]
        Ordered list of giver's names.
    receiver_list : list[str]
        Ordered list of receiver's names (matches with giver_list).

    Returns
    -------
    bool
        False if requirements requirements not met
        True otherwise

    """
    reqs_met = True
    if short_circuit(giver_list, receiver_list):
        reqs_met = False
    else:
        for i in range(len(giver_list)):
            giver = giver_list[i]
            receiver = receiver_list[i]
            if same_person(giver, receiver):
                reqs_met = False
            if is_couple(giver, receiver):
                reqs_met = False
    return reqs_met

# Requirements


def same_person(person_1, person_2):
    """Check if the giving participant is the same as the receiver.

    Parameters
    ----------
    person_1 : str
    person_2 : str

    Returns
    -------
    bool
        Equality of person_1 and person_2

    """
    if person_1 == person_2:
        return True
    else:
        return False


def short_circuit(giver_list, receiver_list):
    """Determine if there is a 'short circuit'.

    i.e. checks if two people are to exchange gifts with eachother.

    Parameters
    ----------
    giver_list : list[str]
        Ordered list of giver's names.
    receiver_list : list[str]
        Ordered list of receiver's names (matches with giver_list).

    Returns
    -------
    bool
        True if giver/receiver pair exists as receiver/giver pair
        False otherwise

    """
    # sorts tuples in alphabetical order
    giver_receiver_pairs = [
        sorted(pair) for pair in zip(giver_list, receiver_list)
    ]
    short_circuit = False
    while len(giver_receiver_pairs) != 0:
        pair = giver_receiver_pairs.pop()
        # checks if pair still exists in remaining pairs
        if pair in giver_receiver_pairs:
            short_circuit = True
    return short_circuit


def is_couple(person_1, person_2):
    """Check if the persons are romantic partners against a "couples.csv" list.

    Parameters
    ----------
    person_1 : str
        First person to check if part of a pairing
    person_2 : str
        Second person to check if part of a pairing

    Returns
    -------
    bool
        truth value of the persons being partners

    """
    try:  # if couples csv doesnt exist, just doesn't consider
        with open("couples.csv") as f:
            reader = csv.reader(f)
            couples = []
            for row in reader:
                couples.append(row)
    except FileNotFoundError:
        return False
    is_couple = False
    for couple in couples:
        if person_1 in couple and person_2 in couple:
            is_couple = True
    return is_couple
