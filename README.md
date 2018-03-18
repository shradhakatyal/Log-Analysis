# Log Analysis Project
An internal reporting tool that helps draw conclusions about a database of news articles. This tool helps answer three questions regarding the news database and uses psycopg2 module for python. This project has been developed for Udacity's<a href="https://in.udacity.com/course/full-stack-web-developer-nanodegree--nd004"> Full Stack Nanodegree Course</a>

## Getting Started
The _following instructions_ will help you setup the project on your machine.

### Prerequisites
This project requires a virtual machine to be setup.
1. Install vagrant <a href="https://www.vagrantup.com/" target="_blank">here!</a>
2. Install VirtualBox <a href="https://www.virtualbox.org/" target="_blank">here!</a>
3. Download the setup files for vagrant from <a href="https://github.com/udacity/fullstack-nanodegree-vm" target="_blank">here!</a>
4. Download the data files from <a href="https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip" target="_blank">here!</a>

## Quick Start
Follow the instructions below to run the project on your machine.

_Starting the virtual machine_

1. Create a new folder where your vagrant file is to be setup.
2. Install vagrant file following the instructions in prerequisites.
3. Unzip the data files to get newsdata.sql, put it in the same folder as your vagrant setup.
4. Download the query.py file from this proejct and put it in the same folder as above.
5. Open terminal on your pc and cd into the directory/folder where you've stored all your files.
```
Example:
> cd FinalProject
```
6. Run the vagrant up and vagrant ssh commands to start the virtual machine and log into it.
```
> vagrant up
> vagrant ssh
```

_Running the project_

1. Load the database by using the following command
```
> psql -d news -f newsdata.sql
```
2. Run the query.py file using the following command
```
> python query.py
```

_Stopping the virtual machine_

1. After getting the results, to exit the virtual machine enter ctrl+d
2. To stop vagrant, run the following command
```
> vagrant halt
```

## Output
The output will be as following
```
Log Analysis Project


Question 1
What are the most popular 3 articles of all time?
Candidate is jerk, alleges rival - 338647 views
Bears love berries, alleges bear - 253801 views
Bad things gone, say good people - 170098 views


Question 2
Who are the most popular article authors of all time?
Ursula La Multa - 507594 views
Rudolf von Treppenwitz - 423457 views
Anonymous Contributor - 170098 views
Markoff Chaney - 84557 views


Question 3
On which days did more than 1% of requests lead to errors?
17-07-2016 - 2.300 % errors
```

## Program's Design
The query.py file runs the queries that generate the desired output. There are 4 functions in query.py, _run_, _popular\_articles_, _popular\_authors_ and _http\_errors_. The first function connects to the database using the psycopg2 module, executes a query and returns the result. The three latter functions call the run function and perform post processing of the results before printing them.