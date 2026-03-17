import pytest

from src.car import Car, NotEnoughFuelError, OverfillError

REFUEL_AMOUNT = 20
DRIVE_DISTANCE = 20
OVERFILL_AMOUNT = 80

class TestCase:
    def setup_method(self):
        self.car = Car(model="BMW X5", fuel_capacity=80)

    def test_drive(self):
        self.car.refuel_car(REFUEL_AMOUNT)
        self.car.drive(DRIVE_DISTANCE)
        assert self.car.get_current_fuel_level() < REFUEL_AMOUNT

    def test_drive_without_fuel(self):
        with pytest.raises(NotEnoughFuelError):
            self.car.drive(DRIVE_DISTANCE)

    def test_refuel(self):
        self.car.refuel_car(REFUEL_AMOUNT)
        assert self.car.get_current_fuel_level() == REFUEL_AMOUNT

        with pytest.raises(OverfillError):
            self.car.refuel_car(OVERFILL_AMOUNT)
