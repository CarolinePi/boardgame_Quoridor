from typing import Union, List

from models.fence_step import FenceStep
from models.pawn_step import PawnStep
from controllers.utils import PlayerActionKey

from models.player import Player

from view.board import Board
from view.utils import ColorEnum, ColorType


class Person(Player):
    def __init__(self, name: str = 'Player', color: ColorType = ColorEnum.RED):
        super().__init__(name, color)

    def play(
        self,
        board: Board,
        valid_pawn_steps: List[PawnStep],
        valid_fence_steps: List[FenceStep],
    ) -> Union[PawnStep, FenceStep]:
        while True:
            key = board.get_keyboard()
            if key == PlayerActionKey.PAWN_STEP.value:
                with board.draw_valid_pawn_step(self.color, self.name, valid_pawn_steps):
                    click = board.get_mouse()
                    pawn_step = board.get_pawn_step_from_mouse_position(
                        self.pawn, click.x, click.y, valid_pawn_steps
                    )
                if pawn_step is not None:
                    return pawn_step
            if key == PlayerActionKey.FENCE_STEP.value and self.can_fences_step:
                click = board.get_mouse()
                fence_step = board.get_fence_step_from_mouse_position(
                    click.x, click.y
                )
                if fence_step is not None:
                    return fence_step

    def __str__(self) -> str:
        return f'{self.__class__.__name__} {self.name} ({self.color})'

