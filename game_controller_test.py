from game_controller import GameController


class MockIntersections:
    def __init__(self, stone_colors):
        self.stone_colors = stone_colors


def test_check_win():
    # Test win for black stones
    intersections = MockIntersections([
        ['black', 'white', 'black', 'black', 'black'],
        ['black', 'black', 'black', 'black', 'black'],
        ['black', 'black', 'black', 'black', 'black'],
        ['black', 'black', 'black', 'black', 'black'],
        ['black', 'black', 'black', 'black', 'black']
    ])
    game_controller = GameController(5, 5, intersections)
    assert game_controller.check_win('black') is True

    # Test win for white stones
    intersections.stone_colors = [
        ['white', 'white', 'white', 'white', 'black'],
        ['white', 'white', 'white', 'black', 'black'],
        ['white', 'white', 'black', 'black', 'black'],
        ['white', 'black', 'black', 'black', 'black'],
        ['black', 'black', 'black', 'black', 'black']
    ]
    assert game_controller.check_win('white') is True

    # Test no win
    intersections.stone_colors = [
        ['black', 'white', 'black', 'black', 'black'],
        ['black', 'white', 'white', 'black', 'black'],
        ['black', 'black', 'black', 'black', 'black'],
        ['black', 'black', 'black', 'black', 'black'],
        ['black', 'black', 'black', 'black', 'black']
    ]
    assert game_controller.check_win('white') is False


def test_update():
    # Test update for black winning
    game_controller = GameController(5, 5, MockIntersections([]))
    game_controller.update('black')
    assert game_controller.black_wins is True
    assert game_controller.white_wins is False

    # Test update for white winning
    game_controller.update('white')
    assert game_controller.black_wins is False
    assert game_controller.white_wins is True

    # Test no update
    game_controller.update('none')
    assert game_controller.black_wins is False
    assert game_controller.white_wins is False
