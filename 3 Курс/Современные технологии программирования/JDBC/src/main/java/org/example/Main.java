package org.example;

public class Main {
    static final String DATABASE_URL = "jdbc:mysql://localhost:3306/mydb";
    static final String USERNAME = "root";
    static final String PASSWORD = "root";

    public static void main(String[] args) {
        if (LoadDrivers.load()) {
            System.out.println("Загрузили драйвер");
        } else {
            System.out.println("Не загрузили");
        }
    }
    static class LoadDrivers {
        static boolean load() {
            try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            return true;
        } catch (ClassNotFoundException exception) {
                return false;
            }
            }
        }
}