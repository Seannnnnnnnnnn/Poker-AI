"""Represents Actions that a player can take"""
from enum import Enum
from typing import Optional
from dataclasses import dataclass


class ActionType(Enum):
    Fold  = "fold"
    Check = "check"
    Call  = "call"
    Raise = "raise"
    AllIn = "all in"


@dataclass
class Action:
    action_type: ActionType
    amount : Optional[int] = None  # valid only for AllIn Raise and Call actions
