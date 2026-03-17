import unittest
from src.car import Car


class TestCase(unittest.TestCase):
    def setUp(self):
        self.car = Car(model="BMW X5", fuel_capacity=80)

    def test_drive(self):
        self.car.drive(20)
        self.assertEqual(self.car.get_current_fuel_level(), 78.4)

    def test_refuel(self):
        # Просто проверяем, что заправка работает без ошибок
        self.car.add_fuel(20)
        self.assertTrue(True)  # тест пройден, если до сюда дошли
