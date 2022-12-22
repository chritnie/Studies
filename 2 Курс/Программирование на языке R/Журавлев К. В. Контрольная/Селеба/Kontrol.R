SUPPLY <- 1
SALE <- 2

FILE_SUPPLY <- 'in'
FILE_SALE <- 'out'

SHOP_COUNT = 10

SHOP_NAME = 'Селеба'

GOODS <- list(
  list(name = 'Молоко, уп.', min = 600, max = 800, p_supply = 5500, p_sale = 8000, p_util = 400),
  list(name = 'Кефир, уп.', min = 200, max = 300, p_supply = 4600, p_sale = 6000, p_util = 300),
  list(name = 'Хлеб, шт.', min = 30, max = 50, p_supply = 200, p_sale = 340, p_util = 15),
  list(name = 'Вода, бут.', min = 400, max = 430, p_supply = 780, p_sale = 1000, p_util = 25),
  list(name = 'Соль, пачка', min = 18, max = 22, p_supply = 431, p_sale = 731, p_util = 32),
  list(name = 'Гречка, пачка', min = 50, max = 60, p_supply = 874, p_sale = 1432, p_util = 12),
  list(name = 'Торт, шт.', min = 20, max = 30, p_supply = 2572, p_sale = 5432, p_util = 540)
)


wrong.temp <- c('День',
                'Молоко..уп.',
                'Кефир..уп.',
                'Хлеб..шт.',
                'Вода..бут.',
                'Соль..пачка',
                'Гречка..пачка',
                'Торт..шт.')
right.temp <- c('День недели',
                'Молоко, уп.',
                'Кефир, уп.',
                'Хлеб, шт.',
                'Вода, бут.',
                'Соль, пачка',
                'Гречка, пачка',
                'Торт, шт.')


#Генерация данных в тек. директории
generate.supply <- 
  function(way = '',
           file.name = 'Поставка',
           days = 7,
           goods = 'Молоко, уп.',
           dataType = SUPPLY,
           sale.level = NULL){
    
    if (way != ''){
      isFoundDir <- dir.exists(way)
      if (isFoundDir == FALSE){
        dir.create(path = way, showWarnings = FALSE)
        isFoundDir <- dir.exists(way)
        if (isFoundDir == FALSE){
          print('Папка назначения не существует, создать её нельзя!')
          return(NULL)
        }
      }
    }
    if (dataType == SALE){
      file.in <- paste0(way, file.name,'.', FILE_SUPPLY)
      isFoundFile <- file.exists(file.in)
      if (isFoundFile) {
        data.in <- read.table(file = file.in,
                              header = TRUE,
                              encoding = 'UTF-8')
      } else {
        data.in <-
          generate.supply(way = way,
                           file.name = file.name,
                           days = days,
                           goods = goods,
                           dataType = SUPPLY)
      }
    }
    tab1 <- data.frame('День' = 1:days)
    if (dataType == SALE){
      if (!is.null(sale.level)){
        for (i in 1:length(goods)){
          tab1[i+1] <- 
            as.integer(data.in[, i+1]*sale.level[i]/100)
        }
      } else {
        for (i in 1:length(goods)){
          tab1[i+1] <-
            sample(x = 1:goods[[i]]$max,
                   size = days,
                   replace = TRUE
            )
          colnames(x=tab1)[i+1] = goods[[i]]$name
        }
      }

    } else {
      
      for (i in 1:length(goods)){
        tab1[i+1] <-
          sample(x = goods[[i]]$min:goods[[i]]$max,
                 size = days,
                 replace = TRUE
          )
        colnames(x=tab1)[i+1] = goods[[i]]$name
      }
    }
    if (dataType == SALE){
      for (i in 1:length(goods)){
        tab1[, i+1] <- 
          ifelse(tab1[, i+1] > data.in[, i+1], 
                 data.in[, i+1],
                 tab1[, i+1])
      }
    }
    ext <- switch (dataType, FILE_SUPPLY, FILE_SALE)
    write.table(
      x = tab1,
      file = paste0(way, file.name, '.', ext),
      col.names = TRUE,
      row.names = FALSE,
      fileEncoding = 'UTF-8'
    )
    return(tab1)
  }

#Генерация файла с ценами
generate.price <- function(goods){
  empty.raw <- rep(NA, length(goods))
  price.frame <- data.frame('цена поставки' = empty.raw,
                            'цена продажи' = empty.raw,
                            'цена утилизации' = empty.raw)
  for (i in 1:length(goods)){
    price.frame[i,1] <- goods[[i]]$p_supply
    price.frame[i,2] <- goods[[i]]$p_sale
    price.frame[i,3] <- goods[[i]]$p_util
    row.names(price.frame)[i] <- goods[[i]]$name
  }
  write.table(x = price.frame,
              file = paste0('Анализ/цены.txt'),
              col.names = TRUE,
              row.names = TRUE,
              fileEncoding = 'UTF-8')
}



#Создание файлов и папок с данными
generate.data <- function(goods = list(name = 'Молоко, уп.', min = 600, max = 800, p_supply = 5500, p_sale = 8000, p_util = 400),
                         shop.count = SHOP_COUNT,
                         sale.level = NULL,
                         days = 7){
  dir.create(path = 'Анализ', showWarnings = FALSE)
  generate.price(goods = goods)
  for (i in 1:shop.count){
    folder.name <- paste0('Магазин ', i)
    way <- paste0(folder.name, '/')
    dir.create(path = way, showWarnings = FALSE)
    isFoundDir <- dir.exists(way)
    if (isFoundDir == FALSE){
      print('Папка назначения не существует, создать её нельзя!')
      return(NULL)
    }
    
    for (dataType in c(SUPPLY, SALE)){
      generate.supply(way = way,
                      file.name = SHOP_NAME,
                      days = days,
                      goods = goods,
                      dataType = dataType,
                      sale.level = sale.level
      )
      ext <- switch (dataType, FILE_SUPPLY, FILE_SALE)
      file_name = paste0(SHOP_NAME,'.',ext)
      from <- paste0(way, file_name)
      to <- paste0('Анализ/', 'Магазин', i, '_', file_name)
      isFoundFile <- file.exists(to)
      if (isFoundFile){
        file.remove(to)
      }
      file.copy(from, to)
    }
    
  }
}





# Генерация исходных данных
generate.data(goods = GOODS)


#Генерация таблицы
tab.layout <- function(){
  rev <- rep(NA, SHOP_COUNT+2)
  returned <- data.frame('Выручка, руб.' = rev,
                         'Прибыль, руб' = rev,
                         'Реализация, шт' = rev,
                         'Списание, шт' = rev,
                         'Равномерность продаж' = rev,
                         'Продажи макс' = rev,
                         'День макс продаж' = rev,
                         'Продажи мин' = rev,
                         'День мин продаж' = rev,
                         'Списание макс' = rev,
                         'День макс списания' = rev
  )
  rows.init <- c()
  for (i in 1:SHOP_COUNT){
    rows.init <- c(rows.init, paste0('Магазин', i))
  }
  rows.init <- c(rows.init, 'Итого', 'Среднее')
  row.names(returned) <- rows.init
  return(returned)
}

#Функция для записи в файл
goods.lst.write <- function(goods.lst){
  goods.names <- names(goods.lst)
  for (i in 1:length(goods.lst)){

    write.table(x = goods.lst[[i]],
                file = paste0('Анализ/', goods.names[i], '.csv'),
                col.names = TRUE,
                row.names = TRUE,
                sep = ';',
                dec = ',',
                fileEncoding = 'UTF-8')
  }
}


data.reader <- function(){
  data.lst <- list()
  for (j in 1:SHOP_COUNT){
    shop.in <- 
      read.table(file = paste0('Анализ/Магазин',j,"_",SHOP_NAME,'.in'),
                 header = TRUE,
                 encoding = 'UTF-8'
      )
    
    colnames(shop.in)[colnames(shop.in) == wrong.temp] <- right.temp
    shop.out <- 
      read.table(file = paste0('Анализ/Магазин',j,"_",SHOP_NAME,'.out'),
                 header = TRUE,
                 encoding = 'UTF-8'
      )
    colnames(shop.out)[colnames(shop.out) == wrong.temp] <- right.temp
    data.lst[[j]] <- list('in' = shop.in, 'out' = shop.out)
    names(data.lst)[[j]] <- paste0('Магазин ', j)
    
  }
  return(data.lst)
}

#Обработка данных с csv
create.tables.csv <- function(data.lst, price.data){
  goods.lst <- list()
  
  for (j in 1:length(data.lst)){
    shop.in <- data.lst[[j]]$'in'
    shop.out <- data.lst[[j]]$'out'
    for (i in 1:(length(shop.in)-1)){
      if (j == 1){
        goods.lst[[i]] <- tab.layout()
        names(goods.lst)[i] <- names(shop.in)[i+1]
      }
      p.supply <- price.data[names(shop.in)[i+1], 'цена.поставки']
      p.sale <- price.data[names(shop.in)[i+1], 'цена.продажи']
      p.util <- price.data[names(shop.in)[i+1], 'цена.утилизации']
      Q_supply <- sum(shop.in[,i+1])
      Q_sale <- sum(shop.out[,i+1])
      Q_util <- Q_supply - Q_sale
      TR <- Q_sale*p.sale
      TC <- Q_util*p.util + Q_supply*p.supply
      Pr <- TR-TC
      sd.sale <-  sd(shop.out[,i+1])
      max.sale <- max(shop.out[,i+1])
      max.day.sale <- which.max(shop.out[,i+1])
      
      min.sale <- min(shop.out[,i+1])
      min.day.sale <- which.min(shop.out[,i+1])
      
      max.util <- max(shop.in[,i+1] - shop.out[,i+1])
      max.day.util <- which.max(shop.in[,i+1] - shop.out[,i+1])
      
      row.values <- c(TR, Pr, Q_sale, Q_util, sd.sale, max.sale, max.day.sale, 
                      min.sale, min.day.sale, max.util, max.day.util)  
      goods.lst[[i]][j,] <- row.values
      
      
      if (j == SHOP_COUNT){
        for (k in 1:5){
          goods.lst[[i]][SHOP_COUNT+1,k] <- 
            sum(goods.lst[[i]][1:SHOP_COUNT,k])
          
          goods.lst[[i]][SHOP_COUNT+2, k] <- 
            mean(goods.lst[[i]][1:SHOP_COUNT,k])
        }
      }
    }
  }
  goods.lst.write(goods.lst)
  return(goods.lst)
}


#Обработка и получение данных

price.data <- 
  read.table(file = 'Анализ/цены.txt',
             header = TRUE,
             row.names = 1,
             encoding = 'UTF-8'
  )
data.lst <- data.reader()

create.tables.csv(data.lst = data.lst,
                  price.data = price.data)



#Графики1
#1ый магазин х
#1ый продукт i
x <- 1  
i <- 1
sale.volume <- data.lst[[x]]$'out'[[i+1]]
supply.volume <- data.lst[[x]]$'in'[[i+1]]
util.volume <- supply.volume - sale.volume
util.price <- util.volume*price.data[i,3]
sale.revenue <- sale.volume*price.data[i,2]
sale.profit <- sale.revenue -
  supply.volume*price.data[i,1] - 
  util.price

profitability <- sale.profit/sale.revenue*100

all.lines <-
  list('объем продаж' = sale.volume,
       'выручка' = sale.revenue,
       'прибыль' = sale.profit,
       'списание' = util.price,
       'рентабельность' = profitability)
cls.lst = colors()[c(17,115, 54, 43, 98)]
par(mfrow = c(2,3))
for (j in 1:length(all.lines)){
  plot(all.lines[[j]],
       type = "b",
       col = cls.lst[j],
       sub = names(data.lst[[x]]$'out')[i+1],
       xlab = "день",
       ylab = "Показатель",
       main = names(all.lines)[j]
  )
}


#Графики2


x <- 3
all.lines <-
  list('прибыль' = list(),
       'списание' = list(),
       'рентабельность' = list())


cls.lst = colors()[sample(1:length(colors()),(length(data.lst[[x]]$'in')-1) , replace = FALSE)]

for (i in 1:(length(data.lst[[x]]$'in')-1)){
  
  sale.volume <- data.lst[[x]]$'out'[[i+1]]
  supply.volume <- data.lst[[x]]$'in'[[i+1]]
  util.volume <- supply.volume - sale.volume
  util.price <- util.volume*price.data[i,3]
  sale.revenue <- sale.volume*price.data[i,2]
  sale.profit <- sale.revenue -
    supply.volume*price.data[i,1] - 
    util.price
  
  profitability <- sale.profit/sale.revenue*100
  
  all.lines[['прибыль']][[names(data.lst[[x]]$'out')[i+1]]] <- sale.profit
  all.lines[['списание']][[names(data.lst[[x]]$'out')[i+1]]] <- util.volume
  all.lines[['рентабельность']][[names(data.lst[[x]]$'out')[i+1]]] <- profitability
  
}




par(mfrow = c(1,3))
for (j in 1:length(all.lines)){
  max_ <- 0
  min_ <- 0
  for (el in all.lines[[j]]){
    if (max(el)>max_){
      max_ <- max(el)
    }
    if(min(el)<min_){
      min_ <- min(el)
    }
  }
  plot(0,0,
       type = "n",
       ylim = c(min_, max_),
       xlim = c(1,7),
       sub = names(data.lst[[x]]$'out')[i+1],
       xlab = "день",
       ylab = "Показатель",
       main = names(all.lines)[j]
       )
  
  for (i in 1:length(all.lines[[j]])){

    lines(all.lines[[j]][[i]],
         type = "b",
         ylim = c(min(unlist(all.lines[[j]])),max(unlist(all.lines[[j]]))),
         sub = names(data.lst[[x]]$'out')[i+1],
         col = cls.lst[i],
         xlab = "день",
         ylab = "Показатель",
         main = names(all.lines)[j]
    )
  }
}

legend(x = "bottomright",
       legend = names(all.lines[[1]]),
       lty = c(1),
       col = cls.lst,
       lwd = 4)


#Графики3
#i продукт
par(mfrow = c(1,1))
i <- 3
volume.lst <- c()
cls.lst = colors()[sample(1:length(colors()),length(data.lst) , replace = FALSE)]

for (x in 1:length(data.lst)){
  volume.lst <- c(volume.lst, sum(data.lst[[x]]$'out'[[i+1]]))
}

pie(volume.lst,
    labels = volume.lst,
    main = "Объем продаж по магазинам",
    col = cls.lst)

legend("topright",
       legend = names(data.lst),
       lty = c(1),
       col = cls.lst,
       lwd = 3)

#Графики4
#nmb - номера товаров
nmb <- c(6,7)
max_ <- 0
min_ <- 0
lns.lst <- list()

cls.lst = colors()[sample(1:length(colors()),length(data.lst) , replace = FALSE)]

data.lst

for (x in 1:length(data.lst)){
  lns.lst[[names(data.lst)[x]]] <- list(
    data.lst[[x]]$'out'[[nmb[1]+1]],
    data.lst[[x]]$'out'[[nmb[2]+1]]
  )
  names(lns.lst[[x]])[1] <- names(data.lst[[x]]$'out')[nmb[1]+1]
  names(lns.lst[[x]])[2] <- names(data.lst[[x]]$'out')[nmb[2]+1]
  
  max.temp <- max(max(lns.lst[[x]][[1]]), max(lns.lst[[x]][[2]]))
  min.temp <- min(min(lns.lst[[x]][[1]]), min(lns.lst[[x]][[2]]))
  if (max.temp > max_){
    max_ <- max.temp
  }
  if (min.temp < min_){
    min_ <- min.temp
  }
}

plot(0,0,
     type = "n",
     ylim = c(min_, max_),
     xlim = c(1,10),
     xlab = "день",
     ylab = "шт",
     main = 'Объемы продаж по двум товарам по всем магазинам'
)

for (i in 1:length(lns.lst)){
  
  lines(lns.lst[[i]][[1]],
        type = "b",
        col = cls.lst[i],
        pch = 1
  )
  lines(lns.lst[[i]][[2]],
        type = "b",
        col = cls.lst[i],
        pch = 2
  )
}

legend("bottomright",
       legend = c(names(data.lst),names(lns.lst[[1]])),
       lty = c(1),
       pch = c(rep(NA, length(data.lst)),1,2),
       col = c(cls.lst, 'black', 'black'),
       lwd = 2)

#Графики5
#i - номер товара
i <- 4

readnumber <- function()
{ 
  n <- readline(prompt="Введите количество магазинов: ")
  n <- as.integer(n)
  if (is.na(n)){
    n <- readnumber()
  }
  Numbers<-c()
  for (i in 1:n){
    num <- readline(prompt=paste0("Введите номер магазина",i,': '))
    Numbers[i]<-as.numeric(num)
  }
  return(Numbers)    
}

magaz <- readnumber()


all.magaz <- list()
max_ <- rep(0,5)
min_ <- max_
for (x in magaz){
  sale.volume <- data.lst[[x]]$'out'[[i+1]]
  supply.volume <- data.lst[[x]]$'in'[[i+1]]
  util.volume <- supply.volume - sale.volume
  util.price <- util.volume*price.data[i,3]
  sale.revenue <- sale.volume*price.data[i,2]
  sale.profit <- sale.revenue -
    supply.volume*price.data[i,1] - 
    util.price
  
  profitability <- sale.profit/sale.revenue*100
  
  all.lines <-
    list('объем продаж' = sale.volume,
         'выручка' = sale.revenue,
         'прибыль' = sale.profit,
         'списание' = util.price,
         'рентабельность' = profitability)
  
  for (k in 1:5){
    
    mx <- max(unlist(all.lines[k]))
    mn <- min(unlist(all.lines[k]))
    mx
    mn
    if(mx > max_[k]) {
      max_[k] <- mx
    }
    
    if(mn < min_[k]){
      min_[k] <- mn
    }
  }
  all.magaz[[names(data.lst)[x]]] <- all.lines
}



cls.lst = colors()[sample(1:length(colors()),7, replace = FALSE)]

par(mfrow = c(2,3))
for (j in 1:length(all.magaz[[1]])){
  plot(0,0,
       xlim = c(1,7),
       ylim = c(min_[j], max_[j]),
       type = "n",
       sub = names(data.lst[[x]]$'out')[i+1],
       xlab = "день",
       main = names(all.magaz[[1]])[j]
  )
  for (i in 1:length(all.magaz)){
    lines(all.magaz[[i]][[j]],
          type = "b",
          col = cls.lst[i]
    )
  }
}
plot.new()

legend("bottomright",
       legend = names(data.lst)[magaz],
       lty = c(1),
       col = cls.lst,
       lwd = 2,
       cex = 1.6)

#Графики6
volume.lst <- c()
good.lengt <- length(data.lst[[1]]$'out')-1
cls.lst = colors()[sample(1:length(colors()),good.lengt , replace = FALSE)]
for (x in 1:length(data.lst)){
  for (i in 1:good.lengt){
    
    volume.lst <-  c(volume.lst, sum(data.lst[[x]]$'out'[[i+1]]))
  }
  
}
volume.matrix <-
  matrix(volume.lst,
         ncol = length(data.lst),
         nrow = (length(data.lst[[x]]$'out')-1)
         )

layout(mat = matrix(c(1,2), nrow = 1, ncol = 2),
       heights = c(1), # Heights of the two rows
       widths = c(3,2)) # Widths of the two columns

barplot(volume.matrix,
        xlab = 'Магазины',
        names.arg = names(data.lst),
        ylab = 'Объемы продаж по товарам',
        beside = FALSE,
        col = cls.lst)

plot.new()
legend("center",
       legend = names(data.lst[[1]]$'out')[1:good.lengt+1],
       lty = c(1),
       col = cls.lst,
       lwd = 7,
       cex = 0.8)