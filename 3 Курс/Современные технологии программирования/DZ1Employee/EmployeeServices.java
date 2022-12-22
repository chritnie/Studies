package Java.lab2;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class EmployeeServices {
    private static Set<Employee> employeeList = new HashSet<>();

    public static void setEmployee(Employee employee){
        if (employeeList.size() < 100) employeeList.add(employee);
        else System.out.println("невозможно добавить больше 100 сотрудников");
    }

    public static Set<Employee> getEmployeeList() {
        return employeeList;
    }

    public static Employee getEmployeeById(int id) {
        // Правильный код
        // return employeeList.stream().filter(e -> e.getId() == id).findFirst().orElse(null);

        // Код по проще
        for (Employee employee : employeeList){
            if (employee.getId() == id) return employee;
        }
        return null;
    }

    public static void getEmployeeByIdAndPrint(int id) {
        System.out.println(getEmployeeById(id));
    }

    public static int getEmployeeCosts() {
        // Правильный код
        // return employeeList.stream().reduce(0, (s, e) -> s + e.getSalary(), Integer::sum);

        // Код по проще
        int s = 0;
        for (Employee employee : employeeList){
            s += employee.getSalary();
        }
        return s;
    }

    public static List<Employee> getEmployeeByDate(String date) {
        List<Employee> l = new ArrayList<>();
        for (Employee employee : employeeList) {
            if (employee.getDateOfBirth().equals(date)) l.add(employee);
        }
        return l;
    }

    public static List<Employee> getEmployeeByName(String name) {
        List<Employee> l = new ArrayList<>();
        for (Employee employee : employeeList) {
            if (employee.getName().equals(name)) l.add(employee);
        }
        return l;
    }
}
