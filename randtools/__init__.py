from .tools import *

__version__ = "1.0.0"
__all__ = tools.__all__,


def __getattr__(name):
    try:
        return getattr(tools, name)
    except AttributeError:
        raise ImportError(f'Cannot find the object/function called {name} in randtools!!\n'
                          f'Are you sure you are on the latest version and you are '
                          f'trying to import the correct object/function?') from None
