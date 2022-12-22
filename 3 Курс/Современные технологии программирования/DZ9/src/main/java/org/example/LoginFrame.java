package org.example;

import javax.swing.*;
import javax.tools.Tool;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowEvent;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class LoginFrame extends JFrame implements ActionListener {

    static final String DATABASE_URL = "jdbc:mysql://localhost:3306/javadz8";
    static final String USERNAME = "root";
    static final String PASSWORD = "OGwinIT98743*";

    Container container = getContentPane();
    JLabel userLabel = new JLabel("USERNAME");
    JLabel passwordLabel = new JLabel("PASSWORD");
    JTextField userTextField = new JTextField();
    JPasswordField passwordField = new JPasswordField();
    JButton loginButton = new JButton("LOGIN");
    JButton resetButton = new JButton("RESET");
    JCheckBox showPassword = new JCheckBox("Show Password");


    LoginFrame() {
        setLayoutManager();
        setLocationAndSize();
        addComponentsToContainer();
        addActionEvent();

    }
    public static void main(String[] args) {
        LoginFrame frame = new LoginFrame();
        frame.setTitle("Login Form");
        frame.setVisible(true);
        frame.setBounds(10, 10, 370, 600);
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        frame.setResizable(false);
    }

    public void setLayoutManager() {
        container.setLayout(null);
    }

    public void setLocationAndSize() {
        userLabel.setBounds(50, 150, 100, 30);
        passwordLabel.setBounds(50, 220, 100, 30);
        userTextField.setBounds(150, 150, 150, 30);
        passwordField.setBounds(150, 220, 150, 30);
        showPassword.setBounds(150, 250, 150, 30);
        loginButton.setBounds(50, 300, 100, 30);
        resetButton.setBounds(200, 300, 100, 30);


    }

    public void addComponentsToContainer() {
        container.add(userLabel);
        container.add(passwordLabel);
        container.add(userTextField);
        container.add(passwordField);
        container.add(showPassword);
        container.add(loginButton);
        container.add(resetButton);
    }

    public void addActionEvent() {
        loginButton.addActionListener(this);
        resetButton.addActionListener(this);
        showPassword.addActionListener(this);
    }

    public void close() {
        WindowEvent closeWindow = new WindowEvent(this, WindowEvent.WINDOW_CLOSING);
        Toolkit.getDefaultToolkit().getSystemEventQueue().postEvent(closeWindow);
    }


    @Override
    public void actionPerformed(ActionEvent e) {
        try (Connection conn = DriverManager.getConnection(DATABASE_URL, USERNAME, PASSWORD)) {
            try (Statement stmt = conn.createStatement()) {
                if (e.getSource() == loginButton) {
                    String userText;
                    String pwdText;
                    userText = userTextField.getText();
                    pwdText = passwordField.getText();
                    String QUERY = "SELECT * FROM users WHERE login = '"+userText+"';";
                    stmt.executeQuery(QUERY);
                    stmt.getResultSet().next();
                    if (stmt.getResultSet().getString("password").equals(pwdText)) {
                        JOptionPane.showMessageDialog(this, "Login Successful");
                        JFrame AdminFrame = new JFrame();
                        new AdminFrame();
                        close();
                    } else {
                        JOptionPane.showMessageDialog(this, "Invalid Username or Password");
                    }

                }
                if (e.getSource() == resetButton) {
                    userTextField.setText("");
                    passwordField.setText("");
                }
                if (e.getSource() == showPassword) {
                    if (showPassword.isSelected()) {
                        passwordField.setEchoChar((char) 0);
                    } else {
                        passwordField.setEchoChar('*');
                    }


                }
            }

        } catch (SQLException ex) {
            throw new RuntimeException(ex);
        }
    }
}

