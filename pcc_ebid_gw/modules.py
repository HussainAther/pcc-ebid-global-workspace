from __future__ import annotations

from dataclasses import dataclass
import random


@dataclass
class CandidateSignal:
    module_name: str
    value: int
    confidence: float


class SpecialistModule:
    def __init__(
        self,
        name: str,
        *,
        seed: int,
        reliability: float = 0.8,
        noise: float = 0.1,
    ) -> None:
        self.name = name
        self.rng = random.Random(seed)
        self.reliability = reliability
        self.noise = noise

    def propose(self, true_value: int) -> CandidateSignal:
        correct = self.rng.random() < self.reliability

        if correct:
            value = true_value
        else:
            value = 1 - true_value

        confidence = self.reliability

        confidence += self.rng.uniform(
            -self.noise,
            self.noise,
        )

        confidence = max(
            0.0,
            min(1.0, confidence),
        )

        return CandidateSignal(
            module_name=self.name,
            value=value,
            confidence=confidence,
        )
