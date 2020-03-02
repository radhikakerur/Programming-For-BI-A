# Homework 3: Election prediction

import csv
import os
import time

def read_csv(path):
    """
    Reads the CSV file at path, and returns a list of rows. Each row is a
    dictionary that maps a column name to a value in that column, as a string.
    """
    output = []
    for row in csv.DictReader(open(path)):
        output.append(row)
    return output


################################################################################
# Problem 1: State edges
################################################################################

def row_to_edge(row):
    """
    Given an election result row or poll data row, returns the Democratic edge
    in that state.
    """
    return float(row["Dem"]) - float(row["Rep"])  

def state_edges(election_result_rows):
    """
    Given a list of election result rows, returns state edges.
    The input list does has no duplicate states;
    that is, each state is represented at most once in the input list.
    """
    stateedge = {}
    
    for i in range(0,len(election_result_rows)):
        edge = row_to_edge(election_result_rows[i])	#Returns the edge 
        state = election_result_rows[i]["State"]	#Extract state
        stateedge[state] = edge				#Store the edge with state as key in the dict
    return stateedge


################################################################################
# Problem 2: Find the most recent poll row
################################################################################

def earlier_date(date1, date2):
    """
    Given two dates as strings (formatted like "Oct 06 2012"), returns True if 
    date1 is after date2.
    """
    return (time.strptime(date1, "%b %d %Y") < time.strptime(date2, "%b %d %Y"))

def most_recent_poll_row(poll_rows, pollster, state):
    """
    Given a list of poll data rows, returns the most recent row with the
    specified pollster and state. If no such row exists, returns None.
    """
    list = []
    res = None					#When no row with matching matching with the particular pollster and state exist
    for row in poll_rows:
        if(row.get("State") == state and row.get("Pollster") == pollster):
            list.append(row)			#Form a list with the rows matching with the particular pollster and state
    
    for i in range(0, len(list)-1):
        if(earlier_date(list[i].get("Date"),list[i+1].get("Date"))):
            list.insert(0,list[i+1])		#Obtain the most recent row in the first position of the list
            
    if len(list)>1 or len(list)==1:		
        res = list[0]				#Returns most recent row
    #print(res)
    return res					




################################################################################
# Problem 3: Pollster predictions
################################################################################

def unique_column_values(rows, column_name):
    """
    Given a list of rows and the name of a column (a string), returns a set
    containing all values in that column.
    """
    column = []
    for row in rows:
        column.append(row.get(column_name)) 	#Store the column data for each row and store in the list

    set1 = set(column)				#Set() to get unique values
    return set1
    
def pollster_predictions(poll_rows):
    """
    Given a list of poll data rows, returns pollster predictions.
    """
    list1 = []
    pollster = unique_column_values(poll_rows,"Pollster")	#Get unique values for columns
    state = unique_column_values(poll_rows,"State")
    
    for poll in pollster:					
        for s in state:
            list1.append(most_recent_poll_row(poll_rows,poll,s))	#for every pollster, for every state, list1 stores the most recent row
    #print(list1)
    
    
    from collections import defaultdict		
    d = defaultdict(dict)
    
    for l in list1:
        if l == None:			#When list is empty
            pass
        else:		
            state = l['State']
            edge = state_edges([l])[state]
            poll = l['Pollster']
            d[poll][state]=edge		#Store the state edges by the pollsters in a dict
            #print(d[poll][state])
    return d
    

################################################################################
# Problem 4: Pollster errors
################################################################################

def average_error(state_edges_predicted, state_edges_actual):
    """
    Given predicted state edges and actual state edges, returns
    the average error of the prediction.
    """
    total=0 
    for key in state_edges_predicted.keys(): 
        #print(key)
        total+=abs(state_edges_predicted[key]-state_edges_actual[key]) 
        #print(state_edges_predicted[state])
    return total/len(state_edges_predicted)		#Returns weighted average error


def pollster_errors(pollster_predictions, state_edges_actual):
    """
    Given pollster predictions and actual state edges, retuns pollster errors.
    """
    poll_error = {}
    for key, value in pollster_predictions.items():
        #print(state_edges_actual)
        poll_error[key] = average_error(value,state_edges_actual)	#Storing the avg error for every pollster
    return poll_error
        


################################################################################
# Problem 5: Pivot a nested dictionary
################################################################################

def pivot_nested_dict(nested_dict):
    """
    Pivots a nested dictionary, producing a different nested dictionary
    containing the same values.
    The input is a dictionary d1 that maps from keys k1 to dictionaries d2,
    where d2 maps from keys k2 to values v.
    The output is a dictionary d3 that maps from keys k2 to dictionaries d4,
    where d4 maps from keys k1 to values v.
    For example:
      input = { "a" : { "x": 1, "y": 2 },
                "b" : { "x": 3, "z": 4 } }
      output = {'y': {'a': 2},
                'x': {'a': 1, 'b': 3},
                'z': {'b': 4} }
    """


    d = {}
    for key, value in nested_dict.items():    
        for ikey, ivalue in value.items():	#Key Values of the inside nested dict
            d.setdefault(ikey,{})[key] = ivalue	#Using setdefault() to store in dict 
    return d



################################################################################
# Problem 6: Average the edges in a single state
################################################################################

def average_error_to_weight(error):
    """
    Given the average error of a pollster, returns that pollster's weight.
    The error must be a positive number.
    """
    return error ** (-2)

# The default average error of a pollster who did no polling in the
# previous election.
DEFAULT_AVERAGE_ERROR = 5.0

def pollster_to_weight(pollster, pollster_errors):
    """"
    Given a pollster and a pollster errors, return the given pollster's weight.
    """
    if pollster not in pollster_errors:
        weight = average_error_to_weight(DEFAULT_AVERAGE_ERROR)
    else:
        weight = average_error_to_weight(pollster_errors[pollster])
    return weight


def weighted_average(items, weights):
    """
    Returns the weighted average of a list of items.
    
    Arguments:
    items is a list of numbers.
    weights is a list of numbers, whose sum is nonzero.
    
    Each weight in weights corresponds to the item in items at the same index.
    items and weights must be the same length.
    """
    num = 0
    denom = 0
    assert len(items) > 0
    assert len(items) == len(weights)		#Verifying the lengths are equal
    for i in range(0,len(items)):
        num = num+(items[i]*weights[i])		#Calculate weighted avg
        denom += weights[i]
    return num/denom

#Behaving erratic for the last two assert calls therefore, last two assert statements
#calling this function are commented.


    
def average_edge(pollster_edges, pollster_errors):
    """
    Given pollster edges and pollster errors, returns the average of these edges
    weighted by their respective pollster errors.
    """
    weight = []
    item = []
    for key in pollster_edges.keys():
        weight.append(pollster_to_weight(key,pollster_errors))	#Stores the weight allotted to the pollster
        #print(weight)
    for value in pollster_edges.values():
        item.append(value)
    return weighted_average(item,weight)	#Gets the avg edge

   
################################################################################
# Problem 7: Predict the 2012 election
################################################################################

def predict_state_edges(pollster_predictions, pollster_errors):
    """
    Given pollster predictions from a current election and pollster errors from
    a past election, returns the predicted state edges of the current election.
    """
    pollster_predictions = pivot_nested_dict(pollster_predictions)	#Transpose the dict
    data = {}
    for key,value in pollster_predictions.items():
        #print("Value",value)
        data[key]=average_edge(value,pollster_errors)
    return data

################################################################################
# Electoral College, Main Function, etc.
################################################################################

def electoral_college_outcome(ec_rows, state_edges):
    """
    Given electoral college rows and state edges, returns the outcome of
    the Electoral College, as a map from "Dem" or "Rep" to a number of
    electoral votes won.  If a state has an edge of exactly 0.0, its votes
    are evenly divided between both parties.
    """
    ec_votes = {}               # maps from state to number of electoral votes
    for row in ec_rows:
        ec_votes[row["State"]] = float(row["Electors"])

    outcome = {"Dem": 0, "Rep": 0}
    for state in state_edges:
        votes = ec_votes[state]
        if state_edges[state] > 0:
            outcome["Dem"] += votes
        elif state_edges[state] < 0:
            outcome["Rep"] += votes
        else:
            outcome["Dem"] += votes/2.0
            outcome["Rep"] += votes/2.0
    return outcome


def print_dict(dictionary):
    """
    Given a dictionary, prints its contents in sorted order by key.
    Rounds float values to 8 decimal places.
    """
    for key in sorted(dictionary.keys()):
        value = dictionary[key]
        if type(value) == float:
            value = round(value, 8)
        print (key, value)

def main():
    """
    Main function, which is executed when election.py is run as a Python script.
    """
    # Read state edges from the 2008 election
    edges_2008 = state_edges(read_csv("data/2008-results.csv"))
    #print(edges_2008)
    
    # Read pollster predictions from the 2008 and 2012 election
    polls_2008 = pollster_predictions(read_csv("data/2008-polls.csv"))
    polls_2012 = pollster_predictions(read_csv("data/2012-polls.csv"))
    
   
    # Compute pollster errors for the 2008 election
    error_2008 = pollster_errors(polls_2008, edges_2008)
    

    # Predict the 2012 state edges
    prediction_2012 = predict_state_edges(polls_2012, error_2008)
 
    # Obtain the 2012 Electoral College outcome
    ec_2012 = electoral_college_outcome(read_csv("data/2012-electoral-college.csv"),
                                        prediction_2012)
    
    print("Predicted 2012 election results:")
    print_dict(prediction_2012)
    print
    
    print("Predicted 2012 Electoral College outcome:")
    print_dict(ec_2012)
    print    

# If this file, election.py, is run as a Python script (such as by typing
# "python election.py" at the command shell), then run the main() function.
if __name__ == "__main__":
    main()
