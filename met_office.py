from abs_subject import AbsSubject


class MetOffice(AbsSubject):
    _london_weather = ""

    @property
    def london_weather(self):
        return self._london_weather

    def set_weather(self, london_weather):
        self._london_weather = london_weather
        self.notify()