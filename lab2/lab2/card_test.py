import unittest
from cards import check_straight, check_3ofa_kind, check_royal_flush, play_cards

class TestPokerFunctions(unittest.TestCase):

    def test_check_straight(self):
        # Test cases for straight
        self.assertEqual(check_straight('S5', 'S6', 'S7'), 7)
        self.assertEqual(check_straight('S6', 'S5', 'S7'), 7)
        self.assertEqual(check_straight('S10', 'SJ', 'SQ'), 12)

        # Test cases for non-straight
        self.assertEqual(check_straight('S3', 'SQ', 'SK'), 0)

    def test_check_3ofa_kind(self):
        # Test cases for three-of-a-kind
        self.assertEqual(check_3ofa_kind('S9', 'S9', 'S9'), 9)

        # Test cases for non-three-of-a-kind
        self.assertEqual(check_3ofa_kind('S2', 'S4', 'S2'), 0)
        self.assertEqual(check_3ofa_kind('S3', 'S3', 'S4'), 0)

    def test_check_royal_flush(self):
        # Test cases for royal flush
        self.assertEqual(check_royal_flush('SA', 'SK', 'SQ'), 14)
        self.assertEqual(check_royal_flush('SJ', 'SQ', 'SK'), 0)  # Not a royal flush
        self.assertEqual(check_royal_flush('S10', 'SJ', 'SQ'), 0)  # Not a royal flush

    def test_play_cards(self):
        # Test cases for who wins
        self.assertEqual(play_cards('S5', 'S6', 'S7', 'S8', 'S9', 'S10'), 1)  # Right wins
        self.assertEqual(play_cards('S10', 'SJ', 'SQ', 'S8', 'S9', 'S10'), -1)  # Left wins
        self.assertEqual(play_cards('S2', 'S3', 'S4', 'S2', 'S3', 'S4'), 0)  # Draw

    if __name__ == '__main__':
        unittest.main()