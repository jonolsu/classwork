best <- function(state, outcome) {
    ## Read outcome data
    setwd("~/Magic Briefcase/Coursera/R Programming/ProgrammingAssignment3")
    ocdata <-read.csv("outcome-of-care-measures.csv", colClasses = "character")   
    
    ## Check that state and outcome are valid
    if(!(state %in% unique(ocdata[,7]))) stop("invalid state")
    if(!(outcome %in% c("heart attack", "heart failure", "pneumonia"))) stop("invalid outcome")

    ## Return hospital name in that stat with lowest 30-day death rate
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
    ## sort allinstate alphebetically by hospital name
    allinstate <- allinstate[order(allinstate[,namecolumn],decreasing = FALSE),]
    ocrow = match(min(allinstate[,occolumn]),allinstate[,occolumn])
    allinstate[ocrow,namecolumn]
}
