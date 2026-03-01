from logpainter import colors


def test_red_wraps_text_with_ansi_codes():
    assert colors.red("hi") == f"{colors.RED}hi{colors.RESET}"


def test_blue_wraps_text_with_ansi_codes():
    assert colors.blue("x") == f"{colors.BLUE}x{colors.RESET}"


def test_color_map_points_to_functions():
    assert colors.color_map["red"] is colors.red
    assert colors.color_map["yellow"] is colors.yellow
    assert colors.color_map["green"] is colors.green
    assert colors.color_map["blue"] is colors.blue
    assert colors.color_map["cyan"] is colors.cyan
