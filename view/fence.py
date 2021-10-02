from graphics import Rectangle, Point

from models.grid_position import GridPosition
from view.facade import FenceFigure
from view.field import Field
from view.utils import FenceDirection, ColorType


class Fence:
    def __init__(
        self,
        position: GridPosition,
        color: ColorType,
        direction: FenceDirection,
    ):
        self.position = position
        self.direction = direction
        self.color = color
        self._figure = None

    def get_figure(
        self,
        field: Field,
        square_size: int,
        inner_size: int,
    ) -> FenceFigure:
        height = 2 * square_size + inner_size
        if self.direction == FenceDirection.HORIZONTAL:
            self._figure = FenceFigure(
                Point(field.left, field.top - inner_size),
                Point(field.left + height, field.top),
                self.color
            )
        if self.direction == FenceDirection.VERTICAL:
            self._figure = FenceFigure(
                Point(field.left - inner_size, field.top),
                Point(field.left, field.top + height),
                self.color
            )
        return self._figure

    @property
    def current_element(self) -> Rectangle:
        if self._figure is not None:
            return self._figure
