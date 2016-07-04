README.md

This repository contains the following elements:

1) This README.md file containing
	a) instructions on how to execute the run_analysis.R script
2) an R script called run_analysis.R
	a) this is the sole script responsible for transforming the source data according to the requirements of the projects
		i) It merges the training and the test sets to create one data set.
		ii) It extracts only the measurements on the mean and standard deviation for each measurement.
		iii) It uses descriptive activity names to name the activities in the data set
		iv) It appropriately labels the data set with descriptive variable names. 
		v) From the data set in step iv, creates a second, independent tidy data set with the average of each variable for each activity and each subject.
	b) reference the in-line documentation for a technical dive into the how these steps are completed
	c) the user of the script is responsible for
		i) setting the working directory at the top level of the source data directory.  The top level of the source data is called UCI HAR Dataset. The source data must be unzipped.
	d) the output files (aggtidydata.txt and tidydata.txt) will be placed one directory higher than the top level of the source directory.
3) aggtidydata.txt
	a) a tidy data file as required by the project instructions
	b) the code book to this file can be found later in this README.md file
4) tidydata.txt
	a) an extra file not required by the project
	b) this is a pre-processed version of the final file
	c) it is saved for documentation and troubleshooting purposes
5) project_codebook.md
	a) the codebook describing the output of aggtidydata.txt, the required outpot of the project


