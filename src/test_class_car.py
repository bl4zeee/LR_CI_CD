import unittest
from .car import Car

class TestCase(unittest.TestCase):
    def setUp(self):
        self.car = Car(model="BMW X5", fuel_capacity=800)

    def tearDown(self):
        pass

    def test_drive(self):
        self.car.drive(20)
        self.assertRaises(Exception, lambda: self.car.drive(80000))

    def test_refuel(self):
    # Сначала сольем немного топлива (проедем 100 км)
        self.car.drive(100)  # сжигаем 8 литров
    # Теперь можно заправить 20 литров
        self.car.add_fuel(20)
    # Было 80, сожгли 8 = 72, залили 20 = 92, но бак 80 → должно быть 80
        self.assertEqual(self.car.get_current_fuel_level(), 80)
