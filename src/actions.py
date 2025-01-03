"""Represents Actions that a player can take"""
from enum import Enum, auto


class PostFlopActions(Enum):
    Fold = auto()
    Call = auto()
    Raise = auto()


class PreFlopActions(Enum):
    raise NotImplementedError
