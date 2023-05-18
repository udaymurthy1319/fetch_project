# fetch_project
Objective: The goal of the program is to monitor the health of a list of HTTP endpoints and log the availability percentage for each domain.
Input: The input is a YAML configuration file containing the list of HTTP endpoints to monitor.

Components:
a. load_config(file_path) is a function that reads a file in YAML format that contains a list of HTTP endpoints. It then returns this list of endpoints so that they can be used in other parts of the program.
b. check_health(endpoint) is a function that takes an HTTP endpoint as input and checks if it is healthy. It does this by sending an HTTP request to the endpoint and checking if the response status code is between 200 and 299 (which means the request was successful) and if the response time is less than 500ms. If the endpoint is healthy, the function returns True, otherwise it returns False.
c. main(file_path) is the main function that controls the entire program. It first loads the list of endpoints from the YAML file using the load_config function. It then initializes some statistics for each endpoint, such as the total number of times it has been checked and the number of times it has been found to be healthy. The function then enters an infinite loop where it checks the health of each endpoint every 15 seconds using the check_health function. It updates the statistics for each endpoint based on whether it is healthy or not, and then logs the availability percentage for each endpoint. This allows you to see how often each endpoint is available and how reliable it is.

Flow:
The program checks if the user provided the correct input (the path to the YAML configuration file). If not, it shows a helpful message and stops.
The main function starts, and it reads the YAML file to get the list of websites to monitor.
The program sets up a storage system to keep track of each website's health statistics.
The program starts a never-ending loop to continuously monitor the websites.
In each loop iteration, the program goes through the list of websites and checks if they are working correctly by sending a request to each one.
If a website is working fine, the program updates its health statistics accordingly.
The program calculates the percentage of time each website has been available and shows this information on the screen.
The program takes a 15-second break before starting the next loop iteration to check the websites again.

Instructions to run:
Install Python 3 if you haven't already. You can download it from the official website: https://www.python.org/downloads/
Install the required libraries. Open a terminal (or command prompt on Windows) and run the following command:
pip install requests PyYAML
Create a new file named health_check.py and copy the provided Python code into it.
Create a YAML configuration file named config.yaml with the list of HTTP endpoints you want to monitor, following the format specified in the problem statement. You can use the example I provided in the previous response.
Open a terminal (or command prompt on Windows) and navigate to the directory where you saved health_check.py and config.yaml. Run the following command:
python health_check.py config.yaml
The script will start monitoring the health of the specified HTTP endpoints every 15 seconds and log the availability percentage for each domain to the console.
To stop the program, press CTRL+C in the terminal (or command prompt on Windows).
