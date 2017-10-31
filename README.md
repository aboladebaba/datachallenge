Welcome to my submission.

I implemented my attempted solution to this challenge in python. I have some experiences with python language recently, this made it a language of choice in my solution.

After careful consideration of the challenge instructions, the following tasks were identified:

1. Data Loading: in this task I used pandas DataFrame as means of getting the data into a table structure for further processing to arrive at the required solution to the challenge. During this task I ensured that only the columns that are required in this challenge were loaded and column names were assigned as required. Transaction date column TRANSACTION_DT was parsed as data string during data loading.


2. Data Filtering: this was a two step task. Step one was where I preserved any rows with empty cell in the OTHER_ID column and step two was where any row with empty cell in either the CMTE_ID or TRANSACTION_AMT columns. The ZIP_CODE column was also trimmed to contain only the first 5 characters of the zip code values.

3. File Generation: the two required files were generated in the following order;
a. medianvals_by_zip.txt: I accessed each row from data frame and select the columns of interest for the purpose of generating this file.I also leveraged dict and list data structures in arriving at the file required.

b. medianvals_by_date.txt: I also relied on pandas grouping functions and join mechanisms to effectively create this file. Please see the source file for details.

4. Testing: I ran test_1 using the example file itcont.txt for this challenge. I also created a sample file from data I downloaded from Federal Election Commission for individual contributions since this was what this challenge was about. My test file has a thousand transactions or rows, was store in test_2 folder in input and the corressponding output were written into the output folder under test_2.

5. Running against larger file: my code was ran against a bigeger file that has relatively large rows 800000+ rows of data.

To run my solution against any file with the directory as setup, I ran this at the command line:

python src/political_donors.py input/itcont.txt output/medianvals_by_zip.txt output/medianvals_by_date.txt

I used the sys.argv[] to extract the arguments passed at the command line (see the source file for details) 
