from app.schemas.strategy import TireCompound


FASTF1_TO_COMPOUND = {
    "SOFT": TireCompound.SOFT,
    "MEDIUM": TireCompound.MEDIUM,
    "HARD": TireCompound.HARD,
    "INTERMEDIATE": TireCompound.INTERMEDIATE,
    "WET": TireCompound.WET,
}


def normalize_compound(raw_value: str) -> TireCompound:
    """
    Maps FastF1 compound strings to the canonical TireCompound enum.

    Missing or unexpected values can be handled here.
    """
    upper = (raw_value or "").upper()
    if upper not in FASTF1_TO_COMPOUND:
        # Default behavior: treat unknown as HARD to avoid crashes (NFR 6.2).
        return TireCompound.HARD
    return FASTF1_TO_COMPOUND[upper]

