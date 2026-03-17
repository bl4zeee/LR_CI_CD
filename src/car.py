121212
class NotEnoughFuelError(Exception):
    pass

class OverfillError(Exception):
    pass

NOT_ENOUGH_FUEL_MSG = "Не доедем жеж..."
OVERFILL_MSG = "Вы пытаетесь залить слишком много бензина!"

class Car:
    def __init__(self, model: str, fuel_capacity: float) -> None:
        self._model = model
        self._max_fuel_capacity: float = fuel_capacity
        self._fuel_in_tank: float = 0

    def get_current_fuel_level(self) -> float:
        return self._fuel_in_tank

    def refuel_car(self, fuel_quantity: float):
        if self._max_fuel_capacity - self._fuel_in_tank < fuel_quantity:
            raise OverfillError(OVERFILL_MSG)
        self._fuel_in_tank += fuel_quantity

    def drive(self, distance_km: float):
        fuel_burned = 8 * (distance_km / 100)
        if self._fuel_in_tank < fuel_burned:
            raise NotEnoughFuelError(NOT_ENOUGH_FUEL_MSG)
        self._fuel_in_tank -= fuel_burned
        return self.get_current_fuel_level()
