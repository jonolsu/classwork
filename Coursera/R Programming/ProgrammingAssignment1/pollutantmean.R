pollutantmean <- function(directory, pollutant, id = 1:332) {
    ## 'directory' is a character vector of length 1 indicating
    ## the location of the CSV files
    
    ## 'pollutant' is a character vector of length 1 indicating
    ## the name of the pollutant for which we will calculate the
    ## mean; either "sulfate" or "nitrate".
    
    ## 'id' is an integer vector indicating the monitor ID numbers
    ## to be used
    
    ## Return the mean of the pollutant across all monitors list
    ## in the 'id' vector (ignoring NA values)

    ## Sample Output
    ## source("pollutantmean.R")
    ## pollutantmean("specdata", "sulfate", 1:10)
    ## [1] 4.064
    ## pollutantmean("specdata", "nitrate", 70:72)
    ## [1] 1.706
    ## pollutantmean("specdata", "nitrate", 23)
    ## [1] 1.281
        
    pollutanterror <- FALSE
    if (pollutant == "sulfate"){
            importcols <- c("NULL","numeric","NULL","NULL")
    } else if (pollutant == "nitrate") {
            importcols <- c("NULL","NULL","numeric","NULL")
    } else {
            pollutanterror <- TRUE
    }
    
    pollutantreads <- NULL
    
    if (!pollutanterror) {
        for (i in id) {
            filename <- paste(sprintf("%03d",i),".csv", sep = "")
            fileandpath <-paste(directory,"/",filename, sep = "")
            pollutantreads <- c(pollutantreads,read.table(fileandpath, 
                                header = TRUE, sep=",",colClasses = importcols))
            pollutantreads <- unlist(pollutantreads, use.names = FALSE)
        }
    }   
    if (pollutanterror){
        "ERROR in pollutant name parameter"
    } else {
        round(mean(pollutantreads, na.rm=TRUE),3)
    }
}