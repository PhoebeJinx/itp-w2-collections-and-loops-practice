def create_box(height, width, character):
    if not height:
        return "Enter height value >= 1"
    if not width:
        return "Enter width value >= 1"
    
    box_list = []
    for h in range(height):
        for w in range(width):
            box_list.append(character)
        box_list.append('\n')
    output = "".join(box_list)
    return output    


# Tests:

first_box_expected = """
****
****
****
""".lstrip()

second_box_expected = """
@
""".lstrip()

third_box_expected = """
xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxx
""".lstrip()


def test_first_box():
    assert create_box(3, 4, '*') == first_box_expected


def test_second_box():
    assert create_box(1, 1, '@') == second_box_expected

# Write your own test using the `third_box_expected` box
def test_third_box():
    assert create_box(3, 24, 'x') == third_box_expected