import pytest

from dlgo.gotypes import Player, Point

class TestPlayer:
    def test_black_value(self):
        assert 1 == Player.black.value

    def test_white_value(self):
        assert 2 == Player.white.value

    def test_other(self):
        assert Player.white == Player.black.other
        assert Player.black == Player.white.other

class TestPoint:
    def test_origin_neighbor(self):
        pt = Point(0, 0)
        assert [Point(-1, 0),
                Point(1, 0),
                Point(0, -1),
                Point(0, 1),] == pt.neighbors()
