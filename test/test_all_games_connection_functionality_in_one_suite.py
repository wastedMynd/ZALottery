import unittest
from test_common_games_info_connection import TestCommonGames as test_info_connection
from test_common_games_draw_connection import TestCommonGames as test_draw_connection
from test_common_games_history_connection import TestCommonGames as test_history_connection
from test_common_games_draw_update_connection import TestCommonGames as test_draw_update_connection
from test_common_games_quick_pick_connection import TestCommonGames as test_quick_pick_connection
from test_common_games_all_draw_update_connection import TestCommonGames as test_all_draw_update_connection

info_suite = unittest.TestLoader().loadTestsFromTestCase(test_info_connection)
draw_suite = unittest.TestLoader().loadTestsFromTestCase(test_draw_connection)
history_suite = unittest.TestLoader().loadTestsFromTestCase(test_history_connection)
draw_update_suite = unittest.TestLoader().loadTestsFromTestCase(test_draw_update_connection)
quick_pick_suite = unittest.TestLoader().loadTestsFromTestCase(test_quick_pick_connection)
all_draw_update_suite = unittest.TestLoader().loadTestsFromTestCase(test_all_draw_update_connection)

tests = [
    quick_pick_suite,
    info_suite,
    draw_suite,
    history_suite,
    draw_update_suite,
    all_draw_update_suite,
]

suite = unittest.TestSuite(tests)


if __name__ == '__main__':
    unittest\
        .TextTestRunner(verbosity=2)\
        .run(suite)
