"""Handles logic for hand-evaluation"""
from typing import List
from phevaluator.evaluator import evaluate_cards


class HandEvaluator:
    
    @staticmethod
    def evaluate_hand(cards: List) -> int:
        return evaluate_cards(*cards)