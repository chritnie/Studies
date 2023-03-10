package org.example;

import java.io.*;
import java.util.ArrayList;

public class Main{
    public static void main(String[] args) throws IOException {
        String textFile = "";
        String str;
        int lowerCase = 0;
        int words = 0;
        int upperCase = 0;
        int sumLetters = 0;
        int whiteSpace = 0;
        int integerNumbers = 0;

        try (BufferedReader ab = new BufferedReader(new FileReader("D:/Studies/СТП/HomeWork2/src/main/java/input.txt"))) {
            while ((str = ab.readLine()) != null) {
                textFile += str;
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

        char[] c = textFile.toCharArray();

        System.out.println("Исходный текст: " + textFile);
        var sumWords = String.valueOf(textFile.split(" ").length);
        System.out.println("Сумма слов в тексте: " + sumWords);


        for (int count = 0; count < c.length; count++) {
            if (Character.isLowerCase(c[count])) lowerCase++;
        }
        System.out.println("Маленьких букв: " + lowerCase);
        for (int count = 0; count < c.length; count++) {
            if (Character.isUpperCase(c[count])) upperCase++;
        }
        System.out.println("Заглавных букв: " + upperCase);
        sumLetters = upperCase + lowerCase;
        System.out.println("Сумма маленьких и заглавных букв: " + sumLetters);

        for (int count = 0; count < c.length; count++) {
            if (Character.isWhitespace(c[count])) whiteSpace++;
        }
        System.out.println("Количество пробелов: " + whiteSpace);

        for (int count = 0; count < c.length; count++) {
            if (Character.isDigit(c[count])) integerNumbers++;
        }
        System.out.println("Количество целых чисел: " + integerNumbers);
        System.out.println("Количество знаков препинания: " + (textFile.length() - removePunctuations(textFile).length()));
        System.out.println("Текст без знаков препинания: " + String.valueOf(removePunctuations(textFile)));


        FileWriter save = new FileWriter("Results.txt");
        save.write("Всего слов в тексте: " + words + '\n'
                        + "Маленьких букв: " + lowerCase + '\n'
                        + "Заглавных букв: " + upperCase + '\n'
                        + "Сумма маленьких и заглавных букв: " + sumLetters + '\n'
                        + "Количество пробелов: " + whiteSpace + '\n'
                        + "Количество целых чисел: " + integerNumbers + '\n'
                        + "Количество знаков препинания: " + (textFile.length() - removePunctuations(textFile).length()) + '\n'
                        + "Текст без знаков препинания: " + String.valueOf(removePunctuations(textFile)) + '\n'
                        + "Количество чисел с плавающей точкой: " + CountFloat(textFile).toArray().length + " " + String.valueOf(CountFloat(textFile))
                );
        save.close();
        System.out.println("Количество чисел с плавающей точкой: " + CountFloat(textFile).toArray().length + " " + String.valueOf(CountFloat(textFile)));
        System.out.println("Сохранено");
    }

    public static String removePunctuations(String source) {
        return source.replaceAll("\\p{Punct}", "");

    }
    public static ArrayList<Float> CountFloat (String S){
        String [] arr = S.split(" ");
        ArrayList<Float> floats = new ArrayList<Float>();
        for (String s : arr) {
            if (s.contains(".")) {
                try {
                    float b = Float.parseFloat(String.valueOf(Float.parseFloat(s) * 100)) / 100;
                    floats.add(b);
                } catch (NumberFormatException e) {
                }
            }
        }
        return floats;
    }

    }