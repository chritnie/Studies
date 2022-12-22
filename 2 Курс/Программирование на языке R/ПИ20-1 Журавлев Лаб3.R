{
w1 <- c(-12L,4,'Level2',8.2,TRUE)
w2 <- c(0,56/6,FALSE,FALSE,18)
w3 <- c(Inf,NULL,NA,FALSE,18,NaN)
w4 <- c(Inf,NULL,NA,FALSE,18L,NaN)
w5 <- c(Inf,NULL,NA,FALSE,'18L',NaN)
w6 <- c(NULL)

print(w1);print(paste(typeof(w1),mode(w1)))
print(w2);print(paste(typeof(w2),mode(w2)))
print(w3);print(paste(typeof(w3),mode(w3)))
print(w4);print(paste(typeof(w4),mode(w4)))
print(w5);print(paste(typeof(w5),mode(w5)))
print(w6);print(paste(typeof(w6),mode(w6)))
}
#преобразование double > character, причем
#NA,INF, NaN не влияют, NULL исчезает, FALSE TRUE превращается
# в текст или 0 и 1
{
  z <- vector()
  print(paste(typeof(z),length(z)))
}
#Логический тип длиной 0
{
  z2 <- vector(mode='numeric', length=129)
  z3 <- vector(mode='logical', length=22)
  z4 <- vector(mode='integer', length=34)
  z5 <- vector(mode='character', length=0)
  z6 <- vector(mode='double', length=19)
  z7 <-vector(length=19) # тип данных задается по умолчанию
  z8 <- vector(mode='double') # длина вектора задается по умолчанию
  print(paste("typeof(z2)",typeof(z2),"typeof(z7)",typeof(z7),"length(z8)",length(z8)))
}
{
  z2 <- numeric(length=129)
  z3 <- logical(length=22)
  z4 <- integer(length=34)
  z5 <- character(length=0)
}
w <- c(10:3)
w
w <- c(1:20, 3)
w
w <- c(10:5, 5:10, 15:18)
w
w <- -4:10
w
w <- 4.5:15.3
w
# от первого значения с шагом 1
1:10-1
1: (10-1)
#сначала ( ) потом : потом +-
w <- rep(TRUE, 8)
w
w2 <- rep(3:-2, 3)
w2
w <- seq(4, from=12, length.out = 10)
w
w <- seq(from = -11, to = 5, by = 2.5)
w
mas <- c(55, 71, 84, 90, 77, 60, 58, 94, 49, 53, 81)
m100 <- mas >= 100
m90 <- mas >= 90
m100
m90
m90 <- mas[mas>=90]
m90[c(TRUE,FALSE)]
#-------------------------------------------------------
#        № 1
#typeof() более информативна и точнее определяет класс
#mode() более старая и для чисел определяет общий класс numeric
#str() определяет int но все же больше похожа на Mode 
#кроме того str преобразует служебную информацию о векторе в строку

#        № 2
{
  w1 <- c(-12L,4,'Level2',8.2,TRUE)
  w2 <- c(0,56/6,FALSE,FALSE,18)
  w3 <- c(Inf,NULL,NA,FALSE,18,NaN)
  w4 <- c(Inf,NULL,NA,FALSE,18L,NaN)
  w5 <- c(Inf,NULL,NA,FALSE,'18L',NaN)
  w6 <- c(NULL)
  
  print(w1);print(paste(typeof(w1),mode(w1),length(w1)))
  print(w2);print(paste(typeof(w2),mode(w2),length(w1)))
  print(w3);print(paste(typeof(w3),mode(w3),length(w1)))
  print(w4);print(paste(typeof(w4),mode(w4),length(w1)))
  print(w5);print(paste(typeof(w5),mode(w5),length(w1)))
  print(w6);print(paste(typeof(w6),mode(w6),length(w1)))
}
#вектор w4 содержит кроеме integer и другие значения, из-за чего
#его тип преобразуется к double
#       № 3
{
  w1 <- rep(c(0, -1, 1:3), times = 3)
  print(w1)
  w2 <- rep(c(0, -1, 1:3), each = 3)
  print(w2)
  w3 <- rep(c(0, -1, 1:3), times = 2, each=3)
  print(w3)
  w4 <- rep(c(0, -1, 1:3), each=3, times = 2)
  print(w4)
}
#сначала внутри вектора дублируется на своих местах
#each раз каждый элемент, а потом вектор полность дублируется
#в конец times раз
#       № 4
{
w <- seq(from = 0, to = 10, by = 2)
print(w)
w <- seq(from = 0, to = 10, length.out = 6)
print(w)
w <- seq(from = 0, to = 10, by = 2, length.out = 5)
}
#by определяет интервал выборки от from до to
#length.out делит этот интервал на указанное число частей
#       № 5
{
seq_len(100)
#возвращает элементы от 1 до n с шагом 1, аналогично
seq(from = 1, to = 100, by = 1)
}
#       № 6
{
  x <- scan(what = logical())
  x
}
#       № 7
{
  x <- scan(what = character())
  x
}
#       № 8
{
  fix(x)
  x1 <- edit(x)
  x1
}
#fix и edit в 1 строчке позволяют изменять текущий объект
#fix во 2 строчке заменяет текущий объект
#edit во 2 строчке создает (возвращает) новый объект
#       № 9
{
  a <- c(7:4, 0)
  b <- c(8, 10.5, 0, -2, 9)
  str(a)
  str(b)
  print("1) Сложение векторов a + b")
  print(paste0(a+b))
  print("2) Умножение векторов a * b")
  print(paste(a*b))
  print("3) Деление векторов a / b")
  print(a/b)
  print("4) Нахождение среднего арифметического для каждого вектора")
  print(sum(a)/length(a))
  print(sum(b)/length(b))
  print(mean(a))
  print(mean(b))
  print("5) Нахождение суммы элементов каждого вектора")
  print(sum(a))
  print(sum(b))
}

#       № 10
{
  w <- c(TRUE)
  print(typeof(w))
  str(w)
  
  w <- c(TRUE, NA, NULL)
  print(typeof(w))
  str(w)
  
  w <- c(TRUE, NA, NULL, 12L)
  print(typeof(w))
  str(w)
  
  w <- c(TRUE, NA, NULL, 12L, NaN)
  print(typeof(w))
  str(w)
  
  w <- c(TRUE, NA, NULL, 12L, Inf)
  print(typeof(w))
  str(w)
  
  w <- c(TRUE, NA, NULL, 12L, 123)
  print(typeof(w))
  str(w)
  
  w <- c(TRUE, NA, NULL, 12L, 23i)
  print(typeof(w))
  str(w)
  
  w <- c(TRUE, NA, NULL, 12L, Inf, NaN, 123i+3, "Hello")
  print(typeof(w))
  str(w)
  
}
#NA не влияет, NULL удаляется, далее по возрастанию значимости
#logical > integer > Nan,Inf,Double > complex > character

#       № 11
{
  x <- c(12L, 13L)
  y <- c(1L, 2L)
  print("1) одного типа, одного размера")
  str(x+y)
  
  x <- c(12L, 13L,14L,15L)
  y <- c(1L, 2L)
  print("2) одного типа, разных размеров")
  str(x+y)
  
  x <- c(12L, 13L)
  y <- c(1, 2)
  print("3) разных типов, одного размера")
  str(x+y)

  x <- c(12L, 13L,14L,15L)
  y <- c(1L, 2L)  
  print("4) разных типов, разного размера")
  str(x+y)
}
#Меньший вектор дополняется собой же бесконечным циклом до длины большего
#тип приводится к старшему (ранее веса типов были определены)
#       № 12
{
  v1 <- c(TRUE, FALSE, FALSE)
  v2 <- c(1L, 2L, 3L, 4L)
  v3 <- c(123,124,125,126,127)
  v4 <- c(1i,2i)
  v5 <- c('Hi')
  print(v1<v2)
  print((v1<v2)&&v3)
  print((v4==10)|(v5>'a'))
}
#при v1 и v2 количество элемтов в 1 добавляется +1 до кол-ва 2
#v1 logical приводится к integer и сравнивается
#во 2 сравнении полученный вектор TRUE FALSE а v3 приводится
#к logical и сравиваются только первые значения
#в третьем 10 приводится к complex И сравнивается с v4
#v5 сравнивается с a, далее сравниваются поэлементно вектора
#результирующие левой и правой стороны сравнения в третьем
#      № 13
{runif(10)*45-17}
#      № 14
{sample(1:1000,20)%%7-8}
#      № 15
{
  ?scan
  scan(what = integer(), n = 3, encoding = "UTF-8", sep = "/")
}
#      № 16
{
  w1 <- -3.3:4.67
  w2 <- rep(c(1:-2), 3)
  str(w1)
  str(w2)
  w1^w2
}
#w1 был дополнен 4мя элементами первыми себя же до длины w2
#далее элементы w1 возводились в степень элементов w2
#      № 17
{
  n <- as.integer(readline('Enter n: '))
  rus_alf <- as.vector(unlist(strsplit('абвгдеёжзийклмнопрстуфхцчшщЪыьэюя', "")))
  rus_alf[sample(1:33,n)]
}
#      № 18
{
  x <- sample(1:100, 20)
  print(x)
  print(sort(x))
  print(x[order(x)])
}
#отличие в том что sort возвращает отсортированный вектор
#когда order возвращает вектор индексов переданного вектора в отсортированном порядке
#и если заменить индексы на сами элементы получим отсортированный переданный вектор
#      № 19
{
  e1 <- scan(what = integer())
  e2 <- scan(what = integer())
  z <- (e1%%e2 == 0)|(e2%%e1 == 0)
  print(z)
}
#      № 20
{
  h1 = vector(mode = "double", length = 20)
  h2 <- vector(mode <-  "double", length <-  20)
  print(paste(length(h1), mode(h2), typeof(h1)))
  print(paste(length(h2), mode(h2), typeof(h2)))
}
rm(h1, h2)
#h2 <- vector(mode <-  "double", length <-  20)
#создает еще две переменные: mode и length