from agen import AudioGenerator
from morse import encode


class MorseGenerator:
    def __init__(
        self,
        frequency: float = 880,
        unit: float = 0.1,
        dot_units: float = 1,
        dash_units: float = 3,
        signals_silence_units: float = 1,
        letters_silence_units: float = 3,
        words_silence_units: float = 7,
    ):
        self.frequency = frequency
        self.unit = unit
        self.dot_duration = dot_units * unit
        self.dash_duration = dash_units * unit
        self.signals_silence_duration = signals_silence_units * unit
        self.letters_silence_duration = letters_silence_units * unit
        self.words_silence_duration = words_silence_units * unit

    def dot(self):
        return AudioGenerator.beep(self.frequency, self.dot_duration)

    def dash(self):
        return AudioGenerator.beep(self.frequency, self.dash_duration)

    def signals_silence(self):
        return AudioGenerator.silence(self.signals_silence_duration)

    def letters_silence(self):
        return AudioGenerator.silence(self.letters_silence_duration)

    def words_silence(self):
        return AudioGenerator.silence(self.words_silence_duration)

    def generate_signal(self, signal, dot_sign=".", dash_sign="-"):
        if not signal:
            return self.signals_silence()
        if signal in dot_sign:
            return self.dot()
        elif signal in dash_sign:
            return self.dash()
        else:
            raise ValueError(f"Unknown signal '{signal}'")

    def generate_letter_signals(self, letter_signals, dot_sign=".", dash_sign="-"):
        first_signal, *rest_signals = letter_signals
        result = self.generate_signal(
            first_signal, dot_sign=dot_sign, dash_sign=dash_sign
        )
        for signal in rest_signals:
            result += self.signals_silence() + self.generate_signal(
                signal, dot_sign=dot_sign, dash_sign=dash_sign
            )
        return result

    def generate_word_signals(
        self, word_signals, dot_sign=".", dash_sign="-", letters_delimiter: str = " "
    ):
        letters = [
            letter.strip()
            for letter in word_signals.split(letters_delimiter)
            if letter.strip()
        ]
        first_letter, *rest_letters = letters
        result = self.generate_letter_signals(
            first_letter, dot_sign=dot_sign, dash_sign=dash_sign
        )
        for letter in rest_letters:
            result += self.letters_silence() + self.generate_letter_signals(
                letter, dot_sign=dot_sign, dash_sign=dash_sign
            )
        return result

    def generate_signals(
        self,
        signals: str,
        dot_sign: str = ".",
        dash_sign: str = "-",
        letters_delimiter: str = " ",
        words_delimiter: str = "/",
    ):
        words = [
            word.strip() for word in signals.split(words_delimiter) if word.strip()
        ]  # TODO: generator?
        first_word, *rest_words = words
        result = self.generate_word_signals(
            first_word,
            dot_sign=dot_sign,
            dash_sign=dash_sign,
            letters_delimiter=letters_delimiter,
        )
        for word in rest_words:
            result += self.words_silence() + self.generate_word_signals(word)
        return result

    def generate_text(self, text: str, dot_sign: str = ".", dash_sign: str = "-"):
        return self.generate_signals(
            encode(text), dot_sign=dot_sign, dash_sign=dash_sign
        )

    def __repr__(self) -> str:
        return f"MorseGenerator({self.frequency!r}, {self.unit!r})"
