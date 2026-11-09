import unittest

from object_detection.detector import calculate_fps, is_quit_key


class TestFPSCalculation(unittest.TestCase):
    def test_calculates_fps(self):
        fps, elapsed = calculate_fps(10.0, 11.0)
        self.assertEqual(elapsed, 1.0)
        self.assertEqual(fps, 1.0)

    def test_smooths_fps(self):
        fps, _ = calculate_fps(10.0, 10.5, previous_fps=10.0)
        self.assertAlmostEqual(fps, 8.4)

    def test_non_positive_elapsed_keeps_previous_fps(self):
        fps, elapsed = calculate_fps(10.0, 10.0, previous_fps=24.0)
        self.assertEqual(elapsed, 0.0)
        self.assertEqual(fps, 24.0)


class TestQuitKey(unittest.TestCase):
    def test_q_quits(self):
        self.assertTrue(is_quit_key(ord("q")))

    def test_uppercase_q_quits(self):
        self.assertTrue(is_quit_key(ord("Q")))

    def test_escape_quits(self):
        self.assertTrue(is_quit_key(27))

    def test_other_key_does_not_quit(self):
        self.assertFalse(is_quit_key(ord("a")))


if __name__ == "__main__":
    unittest.main(verbosity=2)
