class WaveHeight:
    def __init__(self, wave_deep, wave_period):
        self.g = 9.81
        self.wave_deep = wave_deep
        self.wave_speed = self.g * self.wave_deep**(1/2)
        self.wave_length = self.wave_speed * wave_period

    def wave_height_from_wind_speed(self, wind_speed, wave_period):
        significant_wave_height = 0.283 * (wind_speed ** 2) * wave_period
        return significant_wave_height
