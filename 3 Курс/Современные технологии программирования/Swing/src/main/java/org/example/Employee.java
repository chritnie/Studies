package org.example;

public class Employee {
    int ID;
    String Name;
    String Surname;
    String dateOfBirth;
    String placeOfBirth;
    int Salary;
    String maritalStatus;

    int getID() {
        return this.ID;
    }

    void setID(int ID){
        this.ID = ID;
    }

    String getName() {
        return this.Name;
    }

    void setName(String Name){
        this.Name = Name;
    }

    String getSurname() {
        return this.Surname;
    }

    void setSurname(String Surname) {
        this.Surname = Surname;
    }

    String getDateOfBirth() {
        return this.dateOfBirth;
    }

    void setDateOfBirth(String dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
    }

    String getPlaceOfBirth() {
        return this.placeOfBirth;
    }

    void setPlaceOfBirth(String placeOfBirth) {
        this.placeOfBirth = placeOfBirth;
    }

    int getSalary() {
        return this.Salary;
    }

    void setSalary(int Salary) {
        this.Salary = Salary;
    }

    String getMaritalStatus() {
        return this.maritalStatus;
    }

    void setMaritalStatus(String maritalStatus) {
        this.maritalStatus = maritalStatus;
    }

    public Employee(int ID, String Name, String Surname, String dateOfBirth, String placeOfBirth, int Salary, String maritalStatus) {
        this.ID = ID;
        this.Name = Name;
        this.Surname = Surname;
        this.dateOfBirth = dateOfBirth;
        this.placeOfBirth = placeOfBirth;
        this.Salary = Salary;
        this.maritalStatus = maritalStatus;
    }
    public static String searchID(int ID) {
        return "SELECT * FROM people WHERE ID = "+ID+";";
    }
    public static String addEmployee(int ID, String Name, String Surname, String dateOfBirth, String placeOfBirth, int Salary, String maritalStatus) {
        return "INSERT people(ID, Name, Surname, Birthday, PlaceOfBirth, Salary, MaritalStatus)" +
                "VALUES ('" + ID + "','" + Name + "','" + Surname + "','" + dateOfBirth + "','" + placeOfBirth + "','" + Salary + "','" + maritalStatus + "');";
    }
    public static String searchName(String Name) {
        return "SELECT * FROM people WHERE Name = '"+Name+"';";
    }
    public static String searchDate(String dateOfBirth) {
        return "SELECT * FROM people WHERE Birthday = '"+dateOfBirth+"';";
    }
    public static String changeEmployee(String changeQuery, String changeUpdate, int ID) {
        return "UPDATE people SET "+changeQuery+" = '"+changeUpdate+"' WHERE ID = "+ID+";";
    }
    public static String deleteEmployee(int ID) {
        return "DELETE FROM people WHERE ID = "+ID+";";
    }
    public static String sumSalary() {
        return "SELECT SUM(Salary) FROM people;";
    }
}
