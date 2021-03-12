from abs_observer import AbsObserver


class SouthernRail(AbsObserver):
    london_weather = ""

    def __init__(self, met_office):
        self._met_office = met_office
        met_office.attach(self)

    def update(self):
        self.london_weather = self._met_office.london_weather
        self.display()

    def display(self):
        print("weather in London is {}".format(self.london_weather))

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._met_office.detach(self)