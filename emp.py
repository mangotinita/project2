class Employee:
    def __init__(self, name, emp_number):
        self._name = name
        self._emp_number = emp_number

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_emp_number(self):
        return self._emp_number

    def set_emp_number(self, emp_number):
        self._emp_number = emp_number

class ProductionWorker(Employee):
        def __init__(self, name, emp_number, shift_number, hourly_pay_rate):
            super().__init__(name, emp_number)
            self.shift_number = shift_number
            self.hourly_pay_rate = hourly_pay_rate

        def get_hourly_pay_rate(self):
            return self.hourly_pay_rate

        def get_shift_number(self):
            return self.shift_number

        def set_hourly_pay_rate(self, hourly_pay_rate):
            self.hourly_pay_rate = hourly_pay_rate




