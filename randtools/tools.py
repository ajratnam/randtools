__all__ = 'Paginator',


class Paginator:
    """
    Class which is used for pagination of objects.

    Attributes
    ----------
    index : int
        The current index of the Paginator.
    objects : TODO
        The objects on which the Paginator is iterating.
    """
    def __init__(self, objects, starting_index=0, on_end_error=True, convert_to_list=False):
        """
        Creates a new Paginator object with the given parameters.

        Parameters
        ----------
        objects : TODO
            The objects on which the Paginator should iterate.
        starting_index : int
            The index where the pagination should start.
        on_end_error : bool
            Whether it should raise error, if the index exceeded the limits.
        convert_to_list: bool
            Whether objects should be converted to a list (needed for generators).
        """
        if convert_to_list:
            objects = list(objects)
        self.objects = objects
        self.on_end_error = on_end_error
        self._index = 0

        self.index = starting_index

    @property
    def index(self):
        """
        Returns the current index of the Paginator.

        When setting the value of the index,
        it raises IndexError if on_end_error is True and the index goes out of bounds,
        otherwise it wraps the index around the bounds.
        """
        return self._index

    @index.setter
    def index(self, value):
        length = len(self.objects)
        if self.on_end_error and 0 < value < length:
            raise IndexError(f"There are only {length} objects, but tried to set index as {value}")
        self._index = value % length

    @property
    def value(self):
        """
        Returns the object at the current index of the Paginator.
        """
        return self.objects[self.index]

    def next(self, count=1):
        """
        Increments the index by the given amount.

        Parameters
        ----------
        count : int
            How much should the index be incremented by?

        Returns
        -------
        value : TODO
            The object at this new index.
        """
        self.index += count
        return self.value

    def next_until_cond(self, cond, stepper=None):
        """
        Increments the index until the specified condition is met.

        Parameters
        ----------
        cond : TODO
            The condition at which it will stop incrementing.
        stepper : TODO
            The function which is used to increment the index.

        Returns
        -------
        value : TODO
            The object at this new index.
        """
        if stepper is None:
            stepper = self.__class__.next
        while not cond(self.value):
            stepper(self)
        return self.value

    def next_while_cond(self, cond, stepper=None):
        """
        Increments the index while the specified condition is met.

        Parameters
        ----------
        cond : TODO
            The condition that is checked to continue incrementing.
        stepper : TODO
            The function which is used to increment the index.

        Returns
        -------
        value : TODO
            The object at this new index.
        """
        return self.next_until_cond(lambda value: not cond(value), stepper)

    def prev(self, count=1):
        """
        Decrements the index by the given amount.

        Parameters
        ----------
        count : int
            How much should the index be decremented by?

        Returns
        -------
        value : TODO
            The object at this new index.
        """
        return self.next(-count)

    def prev_until_cond(self, cond, stepper=None):
        """
        Decrements the index until the specified condition is met.

        Parameters
        ----------
        cond : TODO
            The condition at which it will stop decrementing.
        stepper : TODO
            The function which is used to decrement the index.

        Returns
        -------
        value : TODO
            The object at this new index.
        """
        if stepper is None:
            stepper = self.__class__.prev
        return self.next_until_cond(cond, stepper)

    def prev_while_cond(self, cond, stepper=None):
        """
        Decrements the index while the specified condition is met.

        Parameters
        ----------
        cond : TODO
            The condition that is checked to continue decrementing.
        stepper : TODO
            The function which is used to decrement the index.

        Returns
        -------
        value : TODO
            The object at this new index.
        """
        return self.prev_until_cond(lambda value: not cond(value), stepper)

    def step_next(self, count=1):
        """
        Increments the index by the 1 and yields the object
        at the current index of the paginator,
        until the index increments the specified count times.

        Parameters
        ----------
        count : TODO
            The number of times to increment the index.

        Yields
        -------
        value : TODO
            The object at the each new index.
        """
        step = 1 if count > 0 else -1
        for _ in range(abs(count)):
            yield self.next(step)

    def step_prev(self, count=1):
        """
        Decrements the index by the 1 and yields the object
        at the current index of the paginator,
        until the index decrements the specified count times.

        Parameters
        ----------
        count : TODO
            The number of times to decrement the index.

        Yields
        -------
        value : TODO
            The object at the each new index.
        """
        return self.step_next(-count)

    def step_next_until_cond(self, cond, stepper=None):
        """
        Increments the index by the 1 and yields the object
        at the current index of the paginator,
        until the given condition is met.

        Parameters
        ----------
        cond : TODO
            The condition at which it will stop incrementing.
        stepper : TODO
            The function which is used to increment the index.

        Yields
        -------
        value : TODO
            The object at the each new index.
        """
        if stepper is None:
            stepper = self.__class__.next
        while True:
            stepper(self)
            if cond(self.value):
                break
            yield self.value

    def step_next_while_cond(self, cond, stepper=None):
        """
        Increments the index by the 1 and yields the object
        at the current index of the paginator,
        while the given condition is met.

        Parameters
        ----------
        cond : TODO
            The condition that is checked to continue incrementing.
        stepper : TODO
            The function which is used to increment the index.

        Yields
        -------
        value : TODO
            The object at the each new index.
        """
        return self.step_next_until_cond(lambda value: not cond(value), stepper)

    def step_prev_until_cond(self, cond, stepper=None):
        """
        Decrements the index by the 1 and yields the object
        at the current index of the paginator,
        until the given condition is met.

        Parameters
        ----------
        cond : TODO
            The condition at which it will stop decrementing.
        stepper : TODO
            The function which is used to decrement the index.

        Yields
        -------
        value : TODO
            The object at the each new index.
        """
        if stepper is None:
            stepper = self.__class__.prev
        return self.step_next_until_cond(cond, stepper)

    def step_prev_while_cond(self, cond, stepper=None):
        """
        Decrements the index by the 1 and yields the object
        at the current index of the paginator,
        while the given condition is met.

        Parameters
        ----------
        cond : TODO
            The condition that is checked to continue decrementing.
        stepper : TODO
            The function which is used to decrement the index.

        Yields
        -------
        value : TODO
            The object at the each new index.
        """
        return self.step_prev_until_cond(lambda value: not cond(value), stepper)

    def goto_next_non_empty(self):
        """
        Increments the index until the object at the
        current index of the Paginator, is a truthful value.

        Returns
        -------
        value : TODO
            The object at this new index.
        """
        return self.next_until_cond(lambda value: value)

    def goto_next_empty(self):
        """
        Increments the index until the object at the
        current index of the Paginator, is a falsy value.

        Returns
        -------
        value : TODO
            The object at this new index.
        """
        return self.next_while_cond(lambda value: value)

    def goto_prev_non_empty(self):
        """
        Decrements the index until the object at the
        current index of the Paginator, is a truthful value.

        Returns
        -------
        value : TODO
            The object at this new index.
        """
        return self.prev_until_cond(lambda value: value)

    def goto_prev_empty(self):
        """
        Decrements the index until the object at the
        current index of the Paginator, is a falsy value.

        Returns
        -------
        value : TODO
            The object at this new index.
        """
        return self.prev_while_cond(lambda value: value)

    def step_to_next_non_empty(self):
        """
        Increments the index by the 1 and yields the object
        at the current index of the paginator,
        until the object at the current index
        of the Paginator, is a truthful value.

        Yields
        -------
        value : TODO
            The object at the each new index.
        """
        return self.step_next_until_cond(lambda value: value)

    def step_to_next_empty(self):
        """
        Increments the index by the 1 and yields the object
        at the current index of the paginator,
        until the object at the current index
        of the Paginator, is a falsy value.

        Yields
        -------
        value : TODO
            The object at the each new index.
        """
        return self.step_next_while_cond(lambda value: value)

    def step_to_prev_non_empty(self):
        """
        Decrements the index by the 1 and yields the object
        at the current index of the paginator,
        until the object at the current index
        of the Paginator, is a truthful value.

        Yields
        -------
        value : TODO
            The object at the each new index.
        """
        return self.step_prev_until_cond(lambda value: value)

    def step_to_prev_empty(self):
        """
        Decrements the index by the 1 and yields the object
        at the current index of the paginator,
        until the object at the current index
        of the Paginator, is a falsy value.

        Yields
        -------
        value : TODO
            The object at the each new index.
        """
        return self.step_prev_while_cond(lambda value: value)

    def set(self, value):
        """
        Sets the index of the Paginator, to the given value.

        Parameters
        ----------
        value : int
            The number, that is to be set as the new index of
            the Paginator.

        Returns
        -------
        value : TODO
            The object at this new index.

        Raises
        ------
        IndexError
            If on_end_error is set to True and the new index is
            out of bounds of the number of objects.
        """
        self.index = value
        return self.value
