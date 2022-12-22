typeof(имя), где имя – имя переменной или константы
is.numeric(имя)
is.integer(имя)
is.double(имя)
is.numeric(имя)
is.logical(имя)
is.character(имя)
is.finite(имя)
is.infinite(имя)
is.na(имя)
is.nan(имя)
as.numeric(имя)
as.integer(имя)
as.double(имя)
as.numeric(имя)
as.logical(имя)
as.character(имя) 
#                         1
a <- as.numeric(77)
b <- as.integer(77)
c <- as.double(77)
d <- as.logical(10)
e <- as.character(100) 
typeof(a)
typeof(b)
typeof(c)
typeof(d)
typeof(e)
typeof(29)
typeof(23i)
typeof(-34L)
typeof(2/3)
typeof(4/2)
typeof(0xA)
typeof(0xbL - 120L)
typeof(0xbL -120)
typeof(0xbL*17)
#по умолчанию численные переменные будут double,
#если указать в конце L то integer
#                         2
{
  x <- readline("enter data: ")
  print(paste("integer и double", as.integer(x)==as.double(x)),  quote = FALSE)
  print(paste("integer и logical", as.integer(x)==as.logical(as.double(x))))
  print(paste("integer и character", as.character(x)==as.character(x)), quote = FALSE)
  print(paste("double и logical", as.double(x)==as.logical(as.double(x))))
  print(paste("double и character", as.double(x)==as.character(x)), quote = FALSE)
}
#приводится к типам по возрастанию значимости
#при сравнении численных к double, если есть строковые
#то к character, учсли есть логические то к
#logical, если одна из NA то результат NA т.к. нет
#операции сравнения для NA
#                         3
{
  x <- readline("enter data: ")
  y <- readline("enter data: ")
  x1 <- as.integer(x); y1 <- as.double(y)
  x2 <- as.integer(x); y2 <- as.logical(as.double(y))
  x3 <- as.logical(as.double(x)); y3 <- as.character(y)
  x4 <- as.double(x); y4 <- as.logical(as.double(y))
  x5 <- as.double(x); y5 <- as.character(y)
  cat("integer и double", typeof(x1+y1),"\n")
  cat("integer и logical", typeof(x2+y2), "\n")
  cat("logical и character", typeof(x3+y3), "\n")
  cat("double и logical", typeof(x4+y4), "\n")
  cat("double и character", typeof(x5+y5), "\n")
}

#cat выполняет меньше преобразований нежели
#print выводит объекты объединяя представления
#(не добавляет кавычки и перевод на новую строку например)
#logical в integer в double, а character ошибка

#                        4
{
  q1 <-2
  q2 <-0
  q3 <- (q1 == 2) & (q2 ==2)
  print(q3)
  q1 <-2
  q2 <-0
  q3 <- (q1 == 2) && (q2 ==2)
  print(q3)
}
#для скалярных значений разницы нет
{
  q1 <-(2:4) # вектор из элементов 2, 3, 4
  q2 <-(2:0) # вектор из элементов 0, 1, 2
  print(q1 == 2)
  print(q2 == 2)
  q3 <- (q1 == 2) & (q2 ==2)
  print(q3)
  print('----------------------')
  q1 <- c(2,3,4)
  q2 <- c(2,3,2)
  print(q1 == 2)
  print(q2 == 2)
  q3 <- (q1 == 2) && (q2 ==2)
  print(q3)
  print('----------------------')
  q1 <- c(2,3,4)
  q2 <- c(7,3,2)
  print(q1 == 2)
  print(q2 == 2)
  q3 <- (q1 == 2) && (q2 ==2)
  print(q3)
}
#при поэлементном сравнение сравнивается первый элемент
#первого вектора с первым элементом второго вектора
#и результатом является вектор значений
#при сокращенном сравнении сравнивается только
#первый элемент одного вектора и первый другого
#                            5
3/7
3/7-0.4285714

#число отображается с округлением и выводится на экран
#уже округленное, но при выполнении более точной
#операции выводится более точное округленное значение

#                             6
sqrt(2)*sqrt(2)
(sqrt(2)*sqrt(2))-2

#вычисляя корень из 2 R представляет его в виде некторого числа
#причем у этого числа есть точность, когда мы перемножаем
#корни в математике мы получим 2, но R перемножает два
#приближенных значения с какойто точностью, а при выводе
#получает 2 с небольшим хвостом, но окргуляет до 2
#то есть на самом деле, изза округления мы получаем
#не чистую 2, а число, приближенное к 2 и при вычитании
#из него 2 как раз видим это приближение (погрешность)