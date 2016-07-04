setwd("D:/Jonathan/Documents/Magic Briefcase/Coursera/Exploratory Data Analysis/Project1/")
##setwd("Y:/My Documents/R/project1")
a<-read.csv("household_power_consumption.txt", sep = ";", head = TRUE)
b <- a[a$Date %in% c("1/2/2007", "2/2/2007"), ]
b$DateTime <- strptime(paste(b$Date,b$Time),"%d/%m/%Y %H:%M:%S")
c<-as.numeric(levels(b$Global_active_power))[b$Global_active_power]

png(file="plot1.png")
hist(c,col="red",main = "Global Active Power",xlab = "Global Active Power (kilowatts)")
dev.off()

png(file="plot2.png")
plot(b$DateTime,c,ylab = "Global Active Power(kilowatts)",xlab ="",type = "n")
lines(b$DateTime,c,type = "l")
dev.off()

d<-as.numeric(levels(b$Sub_metering_1))[b$Sub_metering_1]
e<-as.numeric(levels(b$Sub_metering_2))[b$Sub_metering_2]
f<-b$Sub_metering_3

png(file="plot3.png")
plot(b$DateTime,d,ylab = "Energy sub metering",xlab ="",type = "n")
lines(b$DateTime,d,type = "l",col = "black")
lines(b$DateTime,e,type = "l",col = "red")
lines(b$DateTime,f,type = "l",col = "blue")
legend("topright",c("Sub_metering_1","Sub_metering_2","Sub_metering_3"),lty="solid",col = c("black","red","blue"))
dev.off()

g<-as.numeric(levels(b$Voltage))[b$Voltage]
h<-as.numeric(levels(b$Global_reactive_power))[b$Global_reactive_power]
png(file = "plot4.png")
par(mfrow = c(2,2))
plot(b$DateTime,c,ylab = "Global Active Power",xlab ="",type = "n")
lines(b$DateTime,c,type = "l")
plot(b$DateTime,g,xlab="datetime",ylab="Voltage",type = "n")
lines(b$DateTime,g,type = "l")
plot(b$DateTime,d,ylab = "Energy sub metering",xlab ="",type = "n")
lines(b$DateTime,d,type = "l",col = "black")
lines(b$DateTime,e,type = "l",col = "red")
lines(b$DateTime,f,type = "l",col = "blue")
legend("topright",c("Sub_metering_1","Sub_metering_2","Sub_metering_3"),lty="solid",col = c("black","red","blue"),bty="n")
plot(b$DateTime,h,xlab="datetime",ylab="Global_reactive_power",type = "n")
lines(b$DateTime,h,type = "l")
dev.off()