import os
import sys
import unittest

# Add the src directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.abspath(os.path.join(current_dir, "../"))
sys.path.append(src_dir)

from actions import Action, ActionType


class ActionTests(unittest.TestCase):

    def test_fold_action(self):

        action = Action(ActionType.Fold)
        self.assertEqual(action.action_type, ActionType.Fold)
        self.assertIsNone(action.amount)

    def test_check_action(self):
        # Test creation of a Check action
        action = Action(ActionType.Check)
        self.assertEqual(action.action_type, ActionType.Check)
        self.assertIsNone(action.amount, "Check action should not have an amount.")

    def test_call_action(self):
        # Test creation of a Call action
        action = Action(ActionType.Call)
        self.assertEqual(action.action_type, ActionType.Call)
        self.assertIsNone(action.amount, "Call action should not have an amount.")

    def test_raise_action(self):
        # Test creation of a Raise action with a valid amount
        action = Action(ActionType.Raise, amount=50)
        self.assertEqual(action.action_type, ActionType.Raise)
        self.assertEqual(action.amount, 50, "Raise action should have the correct amount.")
        
    def test_all_in_action(self):
        # Test creation of an AllIn action with a valid amount
        action = Action(ActionType.AllIn, amount=500)
        self.assertEqual(action.action_type, ActionType.AllIn)
        self.assertEqual(action.amount, 500, "AllIn action should have the correct amount.")



if __name__ == "__main__":
    unittest.main()