# federated-analysis

While HIPAA requires that medical information be kept private, scientists need medical information in order to conduct their research.  So instead of sharing data, hospitals and clinics can run software on that data and share the summarized, aggregated results with the interested scientists.  In this way, people's privacy is protected, and science can move forward on important research.

This software repository contains scripts that achieve the above goal.  Specifically, this software allows users to run a Docker container which has the necessary code to perform the statistical analysis and validity checking.  There's a configuration file that the cooperating owner of the data must fill out in conjunction with the scientist to define the fields of interest in the data set.  

There are two Python modules in this repository: one which performs default analysis (dataAnalyzer.py) and one that performs custom analysis (customDataAnalyzer.py).  

The default data analysis outputs the following information:
1. data file name 
2. data file header present?
3. data file field delimiter
4. total records read from data file
5. for each field of interest
    - name of field
    - type of field (numerical, categorical, or free-form)
    - total counts for each value
    - for numerical data, the min, max, mean, and median values
6. bad values (those that don't conform to the type)
7. missing values (fields that are not populated)

Note that the default data analysis is generic -- it's completely devoid of any application or context.  If the scientist wishes to perform specific analyses on the data, then they must implement the custom data analyzer.  The custom data analyzer is provided an object that encapsulates all the default data analysis.  The custom code can then perform application-specific analyses on the data. 


In order to use this solution, perform the following steps.

1. Edit the config/conf.json file to reflect the metadata regarding the data file (file name, header line, field delimiter) as well as the correct fields of interest.

2. Edit the runMe.sh script to point to the correct location of the local repository.

3. Run the runMe.sh script. 



To run the unit tests, perform the following steps:

1. change directory to the top-level directory of the repository

2. run the following command:

python -m unittest tests.test_dataAnalyzer
