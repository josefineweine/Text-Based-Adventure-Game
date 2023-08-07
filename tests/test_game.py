import unittest
from game import scenario_1, scenario_2, scenario_3, game_over, game_win

class TestGame(unittest.TestCase):

    def test_scenario_1(self):
        with unittest.mock.patch('builtins.input', return_value='left'):
            self.assertEqual(scenario_1(), scenario_2())

        with unittest.mock.patch('builtins.input', return_value='right'):
            self.assertEqual(scenario_1(), game_over())

    def test_scenario_2(self):
        with unittest.mock.patch('builtins.input', return_value='open'):
            self.assertEqual(scenario_2(), game_win())

        with unittest.mock.patch('builtins.input', return_value='leave'):
            self.assertEqual(scenario_2(), scenario_3())

    def test_scenario_3(self):
        with unittest.mock.patch('builtins.input', return_value='swim'):
            self.assertEqual(scenario_3(), game_over())

        with unittest.mock.patch('builtins.input', return_value='bridge'):
            self.assertEqual(scenario_3(), game_win())

    def test_game_over(self):
        self.assertEqual(game_over(), None)

    def test_game_win(self):
        self.assertEqual(game_win(), None)

if __name__ == '__main__':
    unittest.main()
