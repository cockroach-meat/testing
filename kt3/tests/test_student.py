"""Ваши проверки. Сначала рассчитайте ожидания по требованиям, затем пишите код."""

import unittest

from mediapolka import issue, new_state, return_loan


class StudentTests(unittest.TestCase):
    # Методы проверок должны называться test_...
    # Начинайте независимый тест с state = new_state().
    # Пример синтаксиса смотрите в test_start.py и в памятке.
    def test_issue_zero_microphones(self):
        state = new_state()
        result = issue(state, "mic", "0")

        self.assertFalse(result["ok"])

    def test_issue_one_microphone(self):
        state = new_state()
        result = issue(state, "mic", "1")

        self.assertTrue(result["ok"])

    def test_issue_three_microphones(self):
        state = new_state()
        result = issue(state, "mic", "3")

        self.assertTrue(result["ok"])

    def test_issue_four_microphones(self):
        state = new_state()
        result = issue(state, "mic", "4")

        self.assertFalse(result["ok"])

    def test_issue_foo_microphones(self):
        state = new_state()
        result = issue(state, "mic", "foo")

        self.assertFalse(result["ok"])

    def test_issue_minus_two_microphones(self):
        state = new_state()
        result = issue(state, "mic", "-2")

        self.assertFalse(result["ok"])

    def test_issue_half_microphones(self):
        state = new_state()
        result = issue(state, "mic", "0.5")

        self.assertFalse(result["ok"])

    def test_issue_two_tripods(self):
        state = new_state()
        result = issue(state, "tripod", "2")

        self.assertFalse(result["ok"])

    def test_issue_tripod_two_times(self):
        state = new_state()
        issue(state, "tripod", "1")
        result = issue(state, "tripod", "1")

        self.assertFalse(result["ok"])

    def test_issue_light(self):
        state = new_state()
        result = issue(state, "light", "1")

        self.assertFalse(result["ok"])

    def test_return_invalid_loan(self):
        state = new_state()
        result = return_loan(state, -1)

        self.assertFalse(result["ok"])

    def test_issue_and_return_microphone(self):
        state = new_state()
        loan = issue(state, "mic", "1")
        result = return_loan(state, loan["loan_id"])

        self.assertTrue(result["ok"])

    def test_issue_and_return_microphone_two_times(self):
        state = new_state()
        loan = issue(state, "mic", "1")
        return_loan(state, loan["loan_id"])
        result = return_loan(state, loan["loan_id"])

        self.assertFalse(result["ok"])

    def test_issue_and_return_tripod_then_issue_again(self):
        state = new_state()
        loan = issue(state, "tripod", "1")
        return_loan(state, loan["loan_id"])
        result = issue(state, "tripod", "1")

        self.assertTrue(result["ok"])
