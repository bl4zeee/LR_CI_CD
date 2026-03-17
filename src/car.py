class Car:
    def __init__(self, model: str, fuel_capacity: float) -> None:
        self.model = model
        self._max_fuel_capacity = fuel_capacity
        self._fuel_in_tank: float = fuel_capacity  # Изначально бак полный!

    def get_current_fuel_level(self) -> float:
        return self._fuel_in_tank

    def add_fuel(self, fuel_quantity: float):
        if self._max_fuel_capacity - self._fuel_in_tank < fuel_quantity:
            raise Exception("Вы пытаетесь залить слишком много бензина!")
        self._fuel_in_tank += fuel_quantity

    def drive(self, distance_km: float):
    # Считаем, что расход 8 литров на 100 км
        fuel_burned: float = 8 * (distance_km / 100)
        if self._fuel_in_tank < fuel_burned:
            raise Exception("Не доедем жеж...")
        self._fuel_in_tank -= fuel_burned  # ← ЭТО ВАЖНО!
        return self.get_current_fuel_level()
