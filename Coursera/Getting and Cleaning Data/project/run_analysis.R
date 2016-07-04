## Set working directory
## setwd("C:/Users/jbennett02/Documents/R/project/UCI HAR Dataset")

## Read both the test and train subject file and begin combining them into a tidy data format
tdata <- rbind(read.table("test/subject_test.txt",head=FALSE),read.table("train/subject_train.txt",head=FALSE))

## Read both the test and train activity file and contune combining them and bind them to the prior read
tdata <- cbind(tdata,rbind(read.table("test/y_test.txt",head=FALSE),read.table("train/y_train.txt",head=FALSE)))

## Replace activity labels (ie numeric) with better descriptor (ie "Walking")
## Note . . . newly introduced activities must be added b/c this approach is not robust to identify new ones
tdata[2] <- replace(tdata[2],tdata[2]==1,"WALKING")
tdata[2] <- replace(tdata[2],tdata[2]==2,"WALKING_UPSTAIRS")
tdata[2] <- replace(tdata[2],tdata[2]==3,"WALKING_DOWNSTAIRS")
tdata[2] <- replace(tdata[2],tdata[2]==4,"SITTING")
tdata[2] <- replace(tdata[2],tdata[2]==5,"STANDING")
tdata[2] <- replace(tdata[2],tdata[2]==6,"LAYING")

## only read in data associated with features containing "std" for standard deviation or "mean"
## this concept comes from http://r.789695.n4.nabble.com/how-to-count-occurrences-of-string-td898646.html
features <- read.table("features.txt",head=FALSE)
featureindex <-1:length(features[[1]])
usefeatures <- featureindex %in% grep("mean",features[[2]]) | featureindex %in% grep("std",features[[2]])  ## element-wise boolean
observationnames <- features[which(usefeatures==TRUE),] ## find elements of features where userfeatures is TRUE
usefeatures  <- replace(usefeatures,usefeatures==TRUE,"numeric") ## replace TRUE with "numeric" to build in colClasses vector
usefeatures  <- replace(usefeatures,usefeatures==FALSE,"NULL") ## replace FALSE with "NULL" to build in colClasses vector
observations <-rbind(read.table("test/X_test.txt",colClasses=usefeatures),read.table("train/X_train.txt",colClasses=usefeatures))

## combine observations with tidydata
tdata <- cbind(tdata,observations)

## construct the names of the tidy data to conform to better naming practices
names(tdata)<-c("subject","activity",as.character(observationnames[,2]))
names(tdata) <- gsub("-","_",names(tdata)) #substitute "-" for "_" to confirm to better naming practices
names(tdata) <- gsub("\\()","",names(tdata)) #substitute "()" for "_" to confirm to better naming practices

#output the tidy data table as a space-delimited file
write.table(tdata,"../tidydata.txt",sep= " ",row.name=FALSE,col.name=TRUE)

## Find average of each variable for each activity and each subject
aggtdata <-aggregate(tdata,list(subjectgrouped = tdata$subject,activitygrouped = tdata$activity),mean)
aggtdata$subject <- NULL # drop this column
aggtdata$activity <- NULL # drop this column

## construct the names of the tidy data to conform to better naming practices
names(aggtdata) <- paste("groupedavg_",names(aggtdata),sep="") #preceed all by "groupedavg_"

#output the tidy data table as a space-delimited file
write.table(aggtdata,"../aggtidydata.txt",sep= " ",row.name=FALSE,col.name=TRUE)

