def highest_number_cubed(limit):
    previous_number = 1

    while True:
        current_number = previous_number + 1
        if current_number ** 3 > limit:
            return previous_number

        previous_number = current_number


def test_three():
    assert highest_number_cubed(30) == 3


def test_two():
    assert highest_number_cubed(12) == 2


def test_one():
    assert highest_number_cubed(3) == 1


def test_big():
    assert highest_number_cubed(12000) == 22
