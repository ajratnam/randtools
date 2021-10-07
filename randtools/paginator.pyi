from collections import Callable
from typing import Any, Iterable, Optional, Sequence, Tuple, Union

__all__: Tuple[str]


class Paginator:
    _index: int
    objects: Union[Iterable, Sequence]
    on_end_error: bool

    def __init__(self, objects: Iterable, starting_index: int = ..., on_end_error: bool = ...,
                 convert_to_list: bool = ...) -> None: ...

    @property
    def index(self) -> int: ...

    @index.setter
    def index(self, value: int) -> None: ...

    @property
    def value(self): ...

    def next(self, count: int = ...): ...

    def next_until_cond(self, cond: Callable[[Any], bool], stepper: Optional[Callable[[Paginator]]] = ...): ...

    def next_while_cond(self, cond: Callable[[Any], bool], stepper: Optional[Callable[[Paginator]]] = ...): ...

    def prev(self, count: int = ...): ...

    def prev_until_cond(self, cond: Callable[[Any], bool], stepper: Optional[Callable[[Paginator]]] = ...): ...

    def prev_while_cond(self, cond: Callable[[Any], bool], stepper: Optional[Callable[[Paginator]]] = ...): ...

    def step_next(self, count: int = ...): ...

    def step_prev(self, count: int = ...): ...

    def step_next_until_cond(self, cond: Callable[[Any], bool], stepper: Optional[Callable[[Paginator]]] = ...): ...

    def step_next_while_cond(self, cond: Callable[[Any], bool], stepper: Optional[Callable[[Paginator]]] = ...): ...

    def step_prev_until_cond(self, cond: Callable[[Any], bool], stepper: Optional[Callable[[Paginator]]] = ...): ...

    def step_prev_while_cond(self, cond: Callable[[Any], bool], stepper: Optional[Callable[[Paginator]]] = ...): ...

    def goto_next_non_empty(self): ...

    def goto_next_empty(self): ...

    def goto_prev_non_empty(self): ...

    def goto_prev_empty(self): ...

    def step_to_next_non_empty(self): ...

    def step_to_next_empty(self): ...

    def step_to_prev_non_empty(self): ...

    def step_to_prev_empty(self): ...

    def set(self, value: int) -> None: ...

    @property
    def is_at_end(self) -> bool: ...

    @property
    def is_at_start(self) -> bool: ...

    @property
    def is_at_ends(self) -> bool: ...

    @property
    def length(self) -> int: ...

    def __len__(self) -> int: ...
