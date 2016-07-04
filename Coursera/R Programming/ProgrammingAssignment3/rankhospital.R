rankhospital <- function(state, outcome, num = "best") {
    ## Read outcome data
    setwd("~/Magic Briefcase/Coursera/R Programming/ProgrammingAssignment3")
    ocdata <-read.csv("outcome-of-care-measures.csv", colClasses = "character") 
    
    ## Check that state and outcome are valid
    if(!(state %in% unique(ocdata[,7]))) stop("invalid state")
    if(!(outcome %in% c("heart attack", "heart failure", "pneumonia"))) stop("invalid outcome")
    
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