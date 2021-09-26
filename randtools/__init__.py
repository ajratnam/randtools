from .paginator import *

__version__ = "1.0.0"
__all__ = paginator.__all__,


def __getattr__(name):
    raise ImportError(f'Cannot find the object/function called {name} in randtools!!\n'
                      f'Are you sure you are on the latest version and you are '
                      f'trying to import the correct object/function?') from None
