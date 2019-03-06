## Draw a scatter plot
library(ggplot2)
qplot(mtcars$wt,mtcarts$mpg)

#this is equivalent to the following
ggplot(mtcars, aes(x = wt, y = mpg)) + geom_point()

qplot(wt, mpg, data = mtcars)

##plot

plot(mtcars$wt,mtcars$mpg)
#################################
#Draw a lin graph

plot(pressure$temperature,pressure$pressure, type = "l")
points(pressure$temperature,pressure$pressure)

lines(pressure$temperature,pressure$pressure/2, col = "red")
points(pressure$temperature,pressure$pressure/2, col = "red")

#ggplot2

library(ggplot2)
qplot(presure$temperature,pressure$pressure, geom = "line")

#this is equivalent to the following

ggplot(pressure, aes(x = temperature, y = pressure)) + geom_line()

## add data point

qplot(pressure$temperature, pressure$pressure, geom = c("line", "point"))

ggplot(pressure, aes(x = temperature, y = pressure)) + geom_line() + geom_point()

############################################
#Draw a bar chat

barplot(BOD$demand, name.arg = BOD$Time)
