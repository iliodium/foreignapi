import enum


class StatusEnum(str, enum.Enum):
    good = "good"
    error = "error"


class DishEnum(str, enum.Enum):
    added = "The dish is added"
    already_exists = "The dish is already on the menu"
