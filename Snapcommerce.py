#python code to display the data in the form of table

import re

def dataclean(data):
    header_row = data.split("\n")[0] #splitting the rows based on new line
    each_header_col = header_row.split(";") #splitting the first header row into separate header names
    header_to, header_from = each_header_col[-1].split("_") #splitting the last header value into to and from values
    for each_col in each_header_col[0:-1]: #printing all headers except the last
        print(each_col.ljust(20), end="\t") #printing with padded zeros to the values
    print(header_to.upper().ljust(20) + "\t" + header_from.upper().ljust(20)) #appending the to and from col names to the last
    temp_code = None #taking temp variable to store the flight code of previous flight
    other_rows = data.split("\n")[1:] #taking all the data cols and one row at a time, everything expect the first column
    for each_row in other_rows:  #take one row at a time
        if each_row is not None and each_row != "": #proceed only if there is data
            each_col = each_row.split(";") #split each row into separate values by taking delimiter
            r_airline_code, r_delay_time, r_flight_code, r_to_from = each_col #unpack the list to the 4 variables
            c_airline_code = re.sub(r'[^a-zA-Z ]+', '', r_airline_code).strip() #remove everything expect alphabets and the space in middle
            c_to, c_from = r_to_from.split("_") #split to and from values and unpack the list
            if(r_flight_code is not None and r_flight_code != ""): #only if my flight code is not null
                c_flight_code = int(float(r_flight_code))
                temp_code = c_flight_code
            else: #othwerwise take old code and add 10 to it
                c_flight_code = temp_code + 10
                temp_code = c_flight_code
            print(c_airline_code.ljust(20) + "\t" + r_delay_time.ljust(20) + "\t" + str(c_flight_code).ljust(20) + "\t" + c_to.upper().ljust(20) + "\t" + c_from.upper().ljust(20))


data = '''Airline Code;DelayTimes;FlightCodes;To_From\nAir Canada (!);[21, 40];20015.0;WAterLoo_NEWYork\n<Air France> (12);[];;Montreal_TORONTO\n(Porter Airways. );[60, 22, 87];20035.0;CALgary_Ottawa\n12. Air France;[78, 66];;Ottawa_VANcouvER\n""".\\.Lufthansa.\\.""";[12, 33];20055.0;london_MONTreal\n'''
dataclean(data)




#####Query To Retrieve Flights Leaving Form Waterloo
#Select * from `Table` where `FROM` = "WATERLOO"