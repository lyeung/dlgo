import pytest
from dlgo.gotypes import Point, Player
from dlgo.goboard_slow import Move, GoString

@pytest.fixture
def the_move():
    return Move(Point(0, 0))

@pytest.fixture
def stone():
    return Point(0, 0)

@pytest.fixture
def liberty():
    return Point(1, 1)

@pytest.fixture
def go_string():
    return GoString(Player.white,
                    set(), set())

class TestMove:
    def assert_move(self, mv):
        assert mv.point == Point(0,0)
        assert mv.is_play is True
        assert mv.is_pass is False
        assert mv.is_resign is False

    def test_one_move(self, the_move):
        self.assert_move(the_move)

    def test_play(self, the_move):
        result = Move.play(the_move)
        self.assert_move(result.point)

    def test_pass_turn(self):
        result = Move.pass_turn()
        assert result.is_pass is True
        assert result.is_play is False
        assert result.is_resign is False

    def test_resign(self):
        result = Move.resign()
        assert result.is_resign is True
        assert result.is_play is False
        assert result.is_pass is False

class TestGoString():
    def test_add_liberty(self, go_string, liberty):
        assert go_string.num_liberties == 0
        go_string.add_liberty(liberty)

        assert go_string.num_liberties == 1

    def test_remove_liberty(self, go_string, liberty):
        go_string.add_liberty(liberty)
        assert go_string.num_liberties == 1

        go_string.remove_liberty(liberty)
        assert go_string.num_liberties == 0

    def test_merge_with_no_common_liberties(self):
        prev_go_string = GoString(Player.white,
                                  [Point(0,0)],
                                  [Point(0,1), Point(1,0)])
        curr_go_string = GoString(Player.white,
                                  [Point(8,0)],
                                  [Point(7,0), Point(8,1)])

        merged = curr_go_string.merged_with(
            prev_go_string)

        assert merged.color == Player.white
        assert set([Point(0,0),Point(8,0)]) == merged.stones
        assert set([Point(0,1), Point(1,0),
                    Point(7,0), Point(8,1)]) == merged.liberties

    def test_merge_with_common_liberties(self):
        prev_go_string = GoString(Player.white,
                                  [Point(0,0)],
                                  [Point(1,0)])
        curr_go_string = GoString(Player.white,
                                  [Point(1,0)],
                                  [Point(0,0)])

        merged = curr_go_string.merged_with(
            prev_go_string)

        assert merged.color == Player.white
        assert set([Point(0,0), Point(1,0)]) == merged.stones
        assert set() == merged.liberties

    def test_eq(self):
        this = GoString(Player.black, [], [])
        that = GoString(Player.black, [], [])
        assert this == that

    def test_eq_with_stones(self):
        this = GoString(Player.black, [Point(0,0), Point(1,0)], [])
        that = GoString(Player.black, [Point(0,0), Point(1,0)], [])
        assert this == that

    def test_eq_with_liberties(self):
        this = GoString(Player.black, [], [Point(0,0), Point(1,0)])
        that = GoString(Player.black, [], [Point(0,0), Point(1,0)])
        assert this == that

    def test_eq_with_liberties(self):
        this = GoString(Player.black, [Point(1,1), Point(2,2)], 
                        [Point(0,0), Point(1,0)])
        that = GoString(Player.black, [Point(1,1), Point(2,2,)], 
                        [Point(0,0), Point(1,0)])
        assert this == that

