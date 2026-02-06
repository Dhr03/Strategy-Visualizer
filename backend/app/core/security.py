from enum import Enum


class StrategyRole(str, Enum):
    """
    Placeholder for authorization roles.

    V1 of this project has no auth, but we keep this
    module to centralize any future security concerns.
    """

    ADMIN = "admin"
    READONLY = "readonly"


def is_authorized(_: StrategyRole = StrategyRole.READONLY) -> bool:
    """
    Stub for future authorization checks.

    Currently always returns True.
    """

    return True

