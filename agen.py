from generators import beep, silence
from itertools import chain


class AudioGenerator:
    def __init__(self, generator=None):
        self._generator = generator

    def __iter__(self):
        return self._generator

    def __add__(self, other: "AudioGenerator"):
        if not isinstance(other, AudioGenerator):
            return NotImplemented
        if self._generator is None:
            return other
        return AudioGenerator(chain(self._generator, other._generator))

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        return self + other

    @classmethod
    def beep(cls, frequency=440, seconds=0.25):
        return cls(beep(frequency, seconds))

    @classmethod
    def silence(cls, seconds):
        return cls(silence(seconds))

    def __repr__(self) -> str:
        return f"AudioGenerator({self._generator!r})"
