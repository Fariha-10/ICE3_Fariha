import unittest
from ICE3.src.temperature_sensor import process_temperatures



class TestTemperatureProcessing(unittest.TestCase):

    # Test valid temperature cases
    def test_valid_temperature_single(self):
        self.assertEqual(process_temperatures([20]), "Min: 20.0°C, Max: 20.0°C, Avg: 20.00°C")

    def test_valid_temperature_multiple(self):
        self.assertEqual(process_temperatures([15, 35]), "Min: 15.0°C, Max: 35.0°C, Avg: 25.00°C")
        self.assertEqual(process_temperatures([10, -10, 30]), "Min: -10.0°C, Max: 30.0°C, Avg: 10.00°C")

    def test_valid_temperature_with_edge_values(self):
        self.assertEqual(process_temperatures([-50, 20, 150, 25]), "Min: -50.0°C, Max: 150.0°C, Avg: 36.25°C")

    def test_valid_temperature_with_repeated_values(self):
        self.assertEqual(process_temperatures([10, 10, 10]), "Min: 10.0°C, Max: 10.0°C, Avg: 10.00°C")

    def test_valid_temperature_multiple_list(self):
        self.assertEqual(process_temperatures([55, 65, 85, 100, 102]), "Min: 55.0°C, Max: 102.0°C, Avg: 81.40°C")

    # Test invalid input cases
    def test_invalid_input_string(self):
        with self.assertRaises(ValueError):  # Should raise ValueError
            process_temperatures([10, "abc", 30])

    def test_invalid_input_special_character(self):
        with self.assertRaises(ValueError):  # Should raise ValueError
            process_temperatures([10, "@", -40])

    # Test out-of-bounds temperature values
    def test_out_of_bounds_lower(self):
        with self.assertRaises(ValueError):  # Should raise ValueError
            process_temperatures([-51, 151])

    # Test large integer out-of-bounds values
    def test_large_integer_out_of_bounds(self):
        with self.assertRaises(ValueError):  # Should raise ValueError
            process_temperatures([2 ** 31 - 1, -2 ** 31])

    # Test empty list input
    def test_empty_input(self):
        with self.assertRaises(ValueError):  # Should raise ValueError for empty input
            process_temperatures([])

    # Test for no valid temperatures in the list
    def test_no_valid_temperatures(self):
        with self.assertRaises(ValueError):  # Should raise ValueError for invalid temperatures
            process_temperatures([2 ** 31 - 1, -2 ** 31])

    # Test mixed valid and invalid temperatures
    def test_mixed_valid_invalid(self):
        with self.assertRaises(ValueError):  # Should raise ValueError
            process_temperatures([34, -12, "hh", 121])

    # Test edge case with all valid temperatures
    def test_valid_temperatures(self):
        with self.assertRaises(ValueError):  # Should raise ValueError due to out-of-bounds value
            process_temperatures([75, -87])


if __name__ == "__main__":
    unittest.main() # pragma: no cover
