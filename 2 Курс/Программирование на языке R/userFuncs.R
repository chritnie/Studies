# Задание 1

# Функция
DEBUG_ON <- TRUE
DEBUG_OFF <- FALSE
pow <- function(x, y, z, isDebug = DEBUG_OFF) {
  if (isDebug) {
    return(print(paste0('pow: x =', x, ', y = ', y, ', z = ', z, ', расчет = ', (x ^ y) / z)))
  } else{
    return((x ^ y) / z)
  }
}

# Программа
z <- 