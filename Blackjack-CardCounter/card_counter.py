"""Hi-Lo card counting utilities."""

from typing import Iterable


class CardCounter:
    """Implement the Hi-Lo card counting strategy."""

    HI_LO_VALUES = {
        "2": 1,
        "3": 1,
        "4": 1,
        "5": 1,
        "6": 1,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": -1,
        "J": -1,
        "Q": -1,
        "K": -1,
        "A": -1,
    }

    def __init__(self) -> None:
        self.running_count = 0

    def _card_value(self, card: str) -> int:
        """Return the Hi-Lo value for a given card name."""
        rank = str(card).split("_")[0]
        return self.HI_LO_VALUES.get(rank, 0)

    def update_running_count(self, cards: Iterable[str] | str) -> int:
        """Update running count given detected cards.

        Args:
            cards: A single card name or iterable of card names.

        Returns:
            The updated running count.
        """
        if isinstance(cards, str):
            cards = [cards]
        for card in cards:
            self.running_count += self._card_value(card)
        return self.running_count

    def get_true_count(self, decks_remaining: float) -> float:
        """Calculate the true count based on remaining decks."""
        if decks_remaining <= 0:
            return 0.0
        return self.running_count / float(decks_remaining)

