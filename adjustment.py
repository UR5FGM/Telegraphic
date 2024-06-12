class _Adjustment:
    def __init__(self):
        self.level = 10

    def up(self):
        self.level += 1
        if self.level > 20:
            self.level = 20

    def down(self):
        self.level -= 1
        if self.level < 0:
            self.level = 0


class Tone_level(_Adjustment):
    _levels = (
        200,
        270,
        340,
        410,
        480,
        550,
        620,
        690,
        760,
        830,
        900,
        970,
        1040,
        1110,
        1180,
        1250,
        1320,
        1390,
        1460,
        1530,
        1600,
    )

    @property
    def freq(self):
        return Tone_level._levels[self.level]


class Rate_level(_Adjustment):
    _levels = (
        0.21,
        0.2,
        0.19,
        0.18,
        0.17,
        0.16,
        0.15,
        0.14,
        0.13,
        0.12,
        0.11,
        0.1,
        0.09,
        0.08,
        0.07,
        0.06,
        0.05,
        0.04,
        0.03,
        0.02,
        0.01,
    )

    @property
    def speed(self):
        return Rate_level._levels[self.level]
