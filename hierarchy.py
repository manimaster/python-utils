class Employee:
    def __init__(self, emp_id, manager=None):
        self.emp_id = emp_id
        self.manager = manager

class EmployeeHierarchy:
    def __init__(self):
        self.employees = {}

    def add_employee(self, emp_id, manager_id):
        # Check if employee already exists
        if emp_id in self.employees:
            raise ValueError(f"Employee with ID {emp_id} already exists.")

        # Check if manager exists if provided
        if manager_id and manager_id not in self.employees:
            raise ValueError(f"Manager with ID {manager_id} doesn't exist.")

        manager = self.employees.get(manager_id)
        self.employees[emp_id] = Employee(emp_id, manager)

    def remove_employee(self, emp_id):
        if emp_id not in self.employees:
            raise ValueError(f"Employee with ID {emp_id} doesn't exist.")

        manager = self.employees[emp_id].manager

        # Reassign direct reportees to the manager of the departing employee
        for emp in self.employees.values():
            if emp.manager and emp.manager.emp_id == emp_id:
                emp.manager = manager

        del self.employees[emp_id]

    def common_manager(self, emp_id1, emp_id2):
        if emp_id1 not in self.employees or emp_id2 not in self.employees:
            raise ValueError("One or both employees don't exist.")

        ancestors1 = set()
        emp1 = self.employees[emp_id1]
        while emp1.manager:
            ancestors1.add(emp1.manager.emp_id)
            emp1 = emp1.manager

        emp2 = self.employees[emp_id2]
        while emp2.manager:
            if emp2.manager.emp_id in ancestors1:
                return emp2.manager.emp_id
            emp2 = emp2.manager

        return None

# Sample usage:
hierarchy = EmployeeHierarchy()

hierarchy.add_employee(1, None)  # CEO
hierarchy.add_employee(2, 1)     # Reports to CEO
hierarchy.add_employee(3, 1)     # Reports to CEO
hierarchy.add_employee(4, 2)     # Reports to employee 2
hierarchy.add_employee(5, 2)     # Reports to employee 2

print(hierarchy.common_manager(4, 5))  # Should print 2

hierarchy.remove_employee(2)  # All reportees of 2 should now report to 1
print(hierarchy.common_manager(4, 5))  # Should print 1
