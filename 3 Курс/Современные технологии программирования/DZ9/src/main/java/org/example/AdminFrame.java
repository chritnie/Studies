package org.example;

import java.awt.*;
import javax.swing.*;
import javax.swing.border.EmptyBorder;


public class AdminFrame extends JFrame{

    static final String DATABASE_URL = "jdbc:mysql://localhost:3306/javadz8";
    static final String USERNAME = "root";
    static final String PASSWORD = "OGwinIT98743*";
    private JButton addUser = new JButton("Добавить пользователя");

    private JButton removeUser = new JButton("Удалить пользователя");

    private JButton addEmployee = new JButton("Добавить сотрудника");

    private JButton searchID = new JButton("Искать сотрудника по ID");

    private JButton searchName = new JButton("Искать сотрудника по имени");

    private JButton searchDate = new JButton("Искать сотрудника по дате рождения");

    private JButton changeInfo = new JButton("Изменить информацию о сотруднике");

    private JButton sumSalary = new JButton("Сумма зарплат");
    private static JFrame frame=new JFrame("Администратор");

    JTextField userAddTextField = new JTextField();



    AdminFrame(){
        panels();
        setLayoutManager();
    }

    public void setLayoutManager() {
        frame.setLayout(null);
    }

    public void setLocationAndSize() {

    }
    private void panels(){
        JPanel panel = new JPanel(new GridLayout(1,1));
        panel.setBorder(new EmptyBorder(5, 5, 5, 5));
        JPanel rightPanel = new JPanel(new GridLayout(15,0,10,10));
        rightPanel.setBorder(new EmptyBorder(15, 5, 5, 10));
        frame.add(panel);
        frame.getContentPane().add(rightPanel,BorderLayout.EAST);
        rightPanel.add(addUser);
        rightPanel.add(removeUser);
        rightPanel.add(addEmployee);
        rightPanel.add(searchID);
        rightPanel.add(searchName);
        rightPanel.add(searchDate);
        rightPanel.add(changeInfo);
        rightPanel.add(sumSalary);
        panel.add(userAddTextField);
        userAddTextField.setBounds(150, 150, 150, 30);
        panel.revalidate();


        frame.setBounds(10, 10, 1500, 1500);
        frame.setVisible(true);
        frame.setLocationRelativeTo(null);

    }
}