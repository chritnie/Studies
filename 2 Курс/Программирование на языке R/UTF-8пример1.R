# секция объявления глобальных констант

G_MAX <- 10000000 # количество товаров
M_MAX <- 1000000 # количество покупателей

PRICE_MIN <- 20
PRICE_MAX <- 4000

BUY_MIN <- 1
BUY_MAX <- 20

t0 <- unclass(Sys.time())


#=============================================
# секция объявления переменных

#============================================= Код вариант №1

price <- double(length = G_MAX) # цены на товары

amount.m <- integer(length = M_MAX) # кол-во покупок покупателями
price.m <- double(length = M_MAX)
payCache.m <- logical(length = M_MAX)


for (i in 1:G_MAX) {
  price[i] <- runif(min = PRICE_MIN, max = PRICE_MAX, n = 1)
  price[i] <-  round(price[i], 2)
}


for (i in 1:M_MAX) {
  # покупки покупателей
  amount.m[i] <- sample(x = BUY_MIN:BUY_MAX, size = 1, replace = TRUE)

  # варианты оплаты
  payCache.m[i] <- sample(c(TRUE, FALSE, TRUE, TRUE), size = 1, replace = TRUE)
  
  # цены за покупки
  price.m[i] <- sample(x = price, size = 1, replace = T)
  
}

# считаем итоги

vol <- 0 # общая выручка от продажи всех товаров

for (i in 1:M_MAX) {
  vol <- vol + amount.m[i] * price.m[i]
}

vol.cache <- 0 # наличные от продажи всех товаров

for (i in 1:M_MAX) {
  vol.cache <- vol.cache + amount.m[i] * price.m[i] * payCache.m[i]
}

# определим долю наличных в общей выручке, в процентах
res <- round(vol.cache / vol * 100, 2)

# для больших сумм перейдем к миллионам
vol.cache <- round(vol.cache / 1000000, 1)

print(paste('Выручка за день, наличные = ', vol.cache, 'млн. руб'))
print(paste('Доля наличных в общей выручке = ', res, '%'))

t1 <- unclass(Sys.time())


#=============================================================================
#=============================================================================

# Версия №2

t00 <- unclass(Sys.time())

price <- runif(min = PRICE_MIN, max = PRICE_MAX, n = G_MAX)
price <-  round(price, 2)


  # покупки покупателей
amount.m <- sample(x = BUY_MIN:BUY_MAX, size = M_MAX, replace = TRUE)
  # варианты оплаты
payCache.m <- sample(c(TRUE, FALSE, TRUE, TRUE), size = M_MAX, replace = TRUE)
  
  # цены за покупки
price.m <- sample(x = price, size = M_MAX, replace = T)
  

# считаем итоги


vol <- sum(amount.m * price.m)

vol.cache <- sum(amount.m * price.m * payCache.m)


# определим долю наличных в общей выручке, в процентах
res <- round(vol.cache / vol * 100, 2)

# для больших сумм перейдем к миллионам
vol.cache <- round(vol.cache / 1000000, 1)

print(paste('Выручка за день, наличные = ', vol.cache, 'млн. руб'))
print(paste('Доля наличных в общей выручке = ', res, '%'))

t11 <- unclass(Sys.time())

print(paste('Время расчета = ', round((t1 - t0), 2), 'сек'))
print(paste('Время расчета = ', round((t11 - t00), 2), 'сек'))
