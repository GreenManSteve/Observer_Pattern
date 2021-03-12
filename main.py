from abs_subject import AbsSubject
from abs_observer import AbsObserver
from met_office import MetOffice
from observers.southern_rail import SouthernRail

with MetOffice() as met:
    with SouthernRail(met):
        met.set_weather("raining")