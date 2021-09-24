__all__ = 'Paginator',


class Paginator:
    def __init__(self, objects, starting_pos=0, on_end_error=True):
        self.objects = objects
        self.on_end_error = on_end_error
        self._pos = starting_pos

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, value):
        self._pos = value % len(self.objects)

    @property
    def value(self):
        return self.objects[self.pos]

    def next(self, count=1):
        self.pos += count
        return self.value

    def next_until_cond(self, cond, stepper=None):
        if stepper is None:
            stepper = self.__class__.next
        while not cond(self.value):
            stepper(self)
        return self.value

    def next_while_cond(self, cond, stepper=None):
        return self.next_until_cond(lambda value: not cond(value), stepper)

    def prev(self, count=1):
        return self.next(-count)

    def prev_until_cond(self, cond, stepper=None):
        if stepper is None:
            stepper = self.__class__.prev
        return self.next_until_cond(cond, stepper)

    def prev_while_cond(self, cond, stepper=None):
        return self.prev_until_cond(lambda value: not cond(value), stepper)

    def step(self, count=1):
        step = 1 if count > 0 else -1
        for _ in range(abs(count)):
            yield self.next(step)

    def step_next_until_cond(self, cond, stepper=None):
        if stepper is None:
            stepper = self.__class__.next
        while True:
            stepper(self)
            if cond(self.value):
                break
            yield self.value

    def step_next_while_cond(self, cond, stepper=None):
        return self.step_next_until_cond(lambda value: not cond(value), stepper)

    def step_prev_until_cond(self, cond, stepper=None):
        if stepper is None:
            stepper = self.__class__.prev
        return self.step_next_until_cond(cond, stepper)

    def step_prev_while_cond(self, cond, stepper=None):
        return self.step_prev_until_cond(lambda value: not cond(value), stepper)

    def goto_next_non_empty(self):
        return self.next_until_cond(lambda value: value)

    def goto_next_empty(self):
        return self.next_while_cond(lambda value: value)

    def goto_prev_non_empty(self):
        return self.prev_until_cond(lambda value: value)

    def goto_prev_empty(self):
        return self.prev_while_cond(lambda value: value)

    def step_to_next_non_empty(self):
        return self.step_next_until_cond(lambda value: value)

    def step_to_next_empty(self):
        return self.step_next_while_cond(lambda value: value)

    def step_to_prev_non_empty(self):
        return self.step_prev_until_cond(lambda value: value)

    def step_to_prev_empty(self):
        return self.step_prev_while_cond(lambda value: value)

    def set(self, value):
        self.pos = value
        return self.value
