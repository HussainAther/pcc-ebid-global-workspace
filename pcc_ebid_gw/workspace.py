from __future__ import annotations

from dataclasses import dataclass

from .modules import CandidateSignal


@dataclass
class WorkspaceResult:
    ignited: bool
    winner: CandidateSignal | None
    broadcast_value: int | None


class GlobalWorkspace:
    def __init__(
        self,
        *,
        ignition_threshold: float = 0.65,
        broadcast_enabled: bool = True,
    ) -> None:
        self.ignition_threshold = ignition_threshold
        self.broadcast_enabled = broadcast_enabled

    def compete(
        self,
        signals: list[CandidateSignal],
    ) -> WorkspaceResult:
        if not signals:
            return WorkspaceResult(
                ignited=False,
                winner=None,
                broadcast_value=None,
            )

        winner = max(
            signals,
            key=lambda signal: signal.confidence,
        )

        ignited = (
            winner.confidence
            >= self.ignition_threshold
        )

        if not ignited:
            return WorkspaceResult(
                ignited=False,
                winner=winner,
                broadcast_value=None,
            )

        broadcast_value = (
            winner.value
            if self.broadcast_enabled
            else None
        )

        return WorkspaceResult(
            ignited=True,
            winner=winner,
            broadcast_value=broadcast_value,
        )
