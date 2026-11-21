import unittest

from operations.memory import Memory


class TestMemory(unittest.TestCase):
    def setUp(self):
        self.memory = Memory()

    def test_initial_value(self):
        self.assertEqual(self.memory.mr(), 0.0)

    def test_m_plus_sets(self):
        self.memory.m_plus(5)
        self.assertEqual(self.memory.mr(), 5.0)

    def test_m_plus_accumulates(self):
        self.memory.m_plus(5)
        self.memory.m_plus(3)
        self.assertEqual(self.memory.mr(), 8.0)

    def test_m_minus(self):
        self.memory.m_plus(10)
        self.memory.m_minus(3)
        self.assertEqual(self.memory.mr(), 7.0)

    def test_m_minus_to_negative(self):
        self.memory.m_minus(5)
        self.assertEqual(self.memory.mr(), -5.0)

    def test_mc_clears(self):
        self.memory.m_plus(5)
        self.memory.mc()
        self.assertEqual(self.memory.mr(), 0.0)

    def test_mc_returns_zero(self):
        self.memory.m_plus(5)
        self.assertEqual(self.memory.mc(), 0.0)


if __name__ == "__main__":
    unittest.main()
