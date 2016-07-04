rankall <- function(outcome, num = "best") {
    ## Read outcome data
    setwd("~/Magic Briefcase/Coursera/R Programming/ProgrammingAssignment3") ## home computer directory
    ##setwd("~/R/ProgrammingAssignment3") ## work computer directory
    ocdata <-read.csv("outcome-of-care-measures.csv", colClasses = "character") 
    
    ## Check that state and outcome are valid
    if(!(outcome %in% c("heart attack", "heart failure", "pneumonia"))) stop("invalid outcome")
    
    ## For each state, find the hospital of the given rank
    statecolumn = 7
    namecolumn = 2
    if(outcome == "heart attack") {
    }
    else if (outcome == "heart failure") {
        occolumn = 17        
    }
    else {
        occolumn = 23
    }
    ## subset ocdata to exclude exclude "Not Available" for outcome
    allwithrank = subset(ocdata,ocdata[,occolumn]!="Not Available")
    ## convert occolumn to numeric
    allwithrank[,occolumn]<-as.numeric(allwithrank[,occolumn])
    ## sort allwithrank numerically by outcome order and then alphebetically by hospital name
    allwithrank <- allwithrank[order(allwithrank[,occolumn],allwithrank[,namecolumn],decreasing = FALSE),]

    ## Return a data frame with the hospital names and the
    ## (abbreviated) state name

    state<-NULL
    hospital<-NULL
    for (i in levels(factor(ocdata[,statecolumn])))
    {
        state[i] <- i
        hospital[i] <- rankhospital2(allwithrank,i,outcome,num)
    }   
    outputframe = data.frame(hospital,state)
}

rankhospital2 <- function(ocdata, state, outcome, num = "best") {
    
    ## Return hospital name in that state with the given rank
    ## 30-day death rate
    statecolumn = 7
    namecolumn = 2
    if(outcome == "heart attack") {
        occolumn = 11
    }
    else if (outcome == "heart failure") {
        occolumn = 17        
    }
    else {
        occolumn = 23
    }
    ## subset ocdata by two criteria: state and exclude "Not Available"
    allinstate = subset(ocdata,ocdata[,statecolumn]==state & ocdata[,occolumn]!="Not Available")
    ## convert occolumn to numeric
    allinstate[,occolumn]<-as.numeric(allinstate[,occolumn])
    ## sort allinstate numerically by outcome order and then alphebetically by hospital name
    allinstate <- allinstate[order(allinstate[,occolumn],allinstate[,namecolumn],decreasing = FALSE),]
    if(num == "best") {
        allinstate[1,namecolumn]
    }
    else if (num == "worst") {
        allinstate[nrow(allinstate),namecolumn]
    }
    else if (num <= nrow(allinstate)) {
        allinstate[num,namecolumn]
    }
    else {
        NA
    }
}