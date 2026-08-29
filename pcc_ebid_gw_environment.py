from __future__ import annotations

import random


class BinaryTaskEnvironment:
    """
    Minimal binary task.

    Each trial has a hidden correct answer:
        0 or 1
    """

    def __init__(
        self,
        *,
        seed: int = 1,
    ) -> None:
        self.rng = random.Random(seed)

    def sample_target(self) -> int:
        return self.rng.choice([0, 1])

    @staticmethod
    def reward(
        action: int,
        target: int,
    ) -> float:
        return 1.0 if action == target else 0.0
