from intersections import Intersections


def test_init():
    intersections = Intersections(5, 5, 100, 100)
    assert intersections.SPACING == 50
    assert intersections.ROW_NUM == 5
    assert intersections.COL_NUM == 5
    assert intersections.X == 100
    assert intersections.Y == 100
    assert len(intersections.grid) == 5
    assert len(intersections.grid[0]) == 5
    assert intersections.count == 25
    assert len(intersections.occupied) == 5
    assert len(intersections.occupied[0]) == 5
    assert len(intersections.stone_colors) == 5
    assert len(intersections.stone_colors[0]) == 5
    for row in intersections.occupied:
        assert all(val is False for val in row)
    for row in intersections.stone_colors:
        assert all(val == 0 for val in row)


def test_mark_occupied():
    intersections = Intersections(3, 3, 0, 0)
    intersection = intersections.grid[1][1]
    # Test marking an intersection as occupied by black stone
    intersections.mark_occupied(intersection, 'black')
    assert intersections.occupied[1][1] is True
    assert intersections.stone_colors[1][1] == 1

    # Test marking an intersection as occupied by white stone
    intersections.mark_occupied(intersection, 'white')
    assert intersections.occupied[1][1] is True
    assert intersections.stone_colors[1][1] == 2


def test_is_occupied():
    intersections = Intersections(2, 2, 0, 0)
    intersection = intersections.grid[0][1]

    # Test if an intersection is initially not occupied
    assert intersections.is_occupied(intersection) is False

    # Mark an intersection as occupied
    intersections.mark_occupied(intersection, 'black')
    assert intersections.is_occupied(intersection) is True


def test_is_full():
    intersections = Intersections(2, 2, 0, 0)
    assert intersections.is_full() is False

    # Mark all intersections as occupied
    for row in intersections.grid:
        for intersection in row:
            intersections.mark_occupied(intersection, 'black')

    assert intersections.is_full() is True


def test_mark_occupied():
    # Initialize Intersections object
    intersections = Intersections(3, 3, 0, 0)
    intersection = intersections.grid[1][1]

    # Test marking an intersection as occupied by black stone
    intersections.mark_occupied(intersection, 'black')
    assert intersections.occupied[1][1] is True
    assert intersections.stone_colors[1][1] == 1

    # Test marking an intersection as occupied by white stone
    intersections.mark_occupied(intersection, 'white')
    assert intersections.occupied[1][1] is True
    assert intersections.stone_colors[1][1] == 2

    # Test marking an intersection as unoccupied
    intersections.mark_occupied(intersection, 'none', occupied=False)
    assert intersections.occupied[1][1] is False
    assert intersections.stone_colors[1][1] == 0
