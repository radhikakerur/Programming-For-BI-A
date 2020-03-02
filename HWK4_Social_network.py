# Homework 4

import networkx as nx
import matplotlib.pyplot as plt
from operator import itemgetter
import operator

###
### Problem 1a
###

practice_graph = nx.Graph()

practice_graph.add_edge("A", "B")
practice_graph.add_edge("A", "C")
practice_graph.add_edge("B", "C")
practice_graph.add_edge("B", "D")
practice_graph.add_edge("C", "D")
practice_graph.add_edge("C", "F")
practice_graph.add_edge("D", "F")
practice_graph.add_edge("D", "E")


assert len(practice_graph.nodes()) == 6
assert len(practice_graph.edges()) == 8

# Test shape of practice graph
assert set(practice_graph.neighbors("A")) == set(["B", "C"])
assert set(practice_graph.neighbors("B")) == set(["A", "D", "C"])
assert set(practice_graph.neighbors("C")) == set(["A", "B", "D", "F"])
assert set(practice_graph.neighbors("D")) == set(["B", "C", "E", "F"])
assert set(practice_graph.neighbors("E")) == set(["D"])
assert set(practice_graph.neighbors("F")) == set(["C", "D"])

def draw_practice_graph():
    """Draw practice_graph to the screen.
    """
    nx.draw_networkx(practice_graph)
    plt.show()

# Comment out this line after you have visually verified your practice graph.
# Otherwise, the picture will pop up every time that you run your program.
draw_practice_graph()


###
### Problem 1b
###

# (Your code for Problem 1b goes here.)
rj = nx.Graph()

rj.add_edge("Nurse", "Juliet")
rj.add_edge("Juliet", "Tybalt")
rj.add_edge("Juliet", "Capulet")
rj.add_edge("Juliet","Romeo")
rj.add_edge("Juliet", "Friar Laurence")
rj.add_edge("Tybalt", "Capulet")
rj.add_edge("Capulet", "Escalus")
rj.add_edge("Capulet", "Paris")
rj.add_edge("Friar Laurence", "Romeo")
rj.add_edge("Romeo", "Benvolio")
rj.add_edge("Romeo", "Montague")
rj.add_edge("Romeo", "Mercutio")
rj.add_edge("Benvolio", "Montague")
rj.add_edge("Montague", "Escalus")
rj.add_edge("Escalus", "Mercutio")
rj.add_edge("Escalus", "Paris")
rj.add_edge("Mercutio", "Paris")


assert len(rj.nodes()) == 11
assert len(rj.edges()) == 17

# Test shape of Romeo-and-Juliet graph
assert set(rj.neighbors("Nurse")) == set(["Juliet"])
assert set(rj.neighbors("Friar Laurence")) == set(["Juliet", "Romeo"])
assert set(rj.neighbors("Tybalt")) == set(["Juliet", "Capulet"])
assert set(rj.neighbors("Benvolio")) == set(["Romeo", "Montague"])
assert set(rj.neighbors("Paris")) == set(["Escalus", "Capulet", "Mercutio"])
assert set(rj.neighbors("Mercutio")) == set(["Paris", "Escalus", "Romeo"])
assert set(rj.neighbors("Montague")) == set(["Escalus", "Romeo", "Benvolio"])
assert set(rj.neighbors("Capulet")) == \
    set(["Juliet", "Tybalt", "Paris", "Escalus"])
assert set(rj.neighbors("Escalus")) == \
    set(["Paris", "Mercutio", "Montague", "Capulet"])
assert set(rj.neighbors("Juliet")) == \
    set(["Nurse", "Tybalt", "Capulet", "Friar Laurence", "Romeo"])
assert set(rj.neighbors("Romeo")) == \
    set(["Juliet", "Friar Laurence", "Benvolio", "Montague", "Mercutio"])

def draw_rj():
    """Draw the rj graph to the screen and to a file.
    """
    nx.draw_networkx(rj)
    plt.savefig("romeo-and-juliet.pdf")
    plt.show()

# Comment out this line after you have visually verified your rj graph and
# created your PDF file.
# Otherwise, the picture will pop up every time that you run your program.
draw_rj()


###
### Problem 2
###

def friends(graph, user):
    """Returns a set of the friends of the given user, in the given graph.
    """
    # This function has already been implemented for you.
    # You do not need to add any more code to this (short!) function.
    return set(graph.neighbors(user))


assert friends(rj, "Mercutio") == set(['Romeo', 'Escalus', 'Paris'])


def friends_of_friends(graph, user):
    """Returns a set of friends of friends of the given user, in the given 
    graph. The result does not include the given user nor any of that user's
    friends.
    """
    s = set()
    for f1 in friends(graph, user):
        for f2 in friends(graph, f1):
            if(f2 != user) and (f2 not in friends(graph,user)):
                s.add(f2)
    return s

assert friends_of_friends(rj, "Mercutio") == \
    set(['Benvolio', 'Capulet', 'Friar Laurence', 'Juliet', 'Montague'])


def common_friends(graph, user1, user2):
    """Returns the set of friends that user1 and user2 have in common.
    """
    
    a = set(friends(graph,user1)) & set(friends(graph,user2))
    return a
    #print ("Remove this print statement once common_friends is implemented")


assert common_friends(practice_graph,"A", "B") == set(['C'])
assert common_friends(practice_graph,"A", "D") == set(['B', 'C'])
assert common_friends(practice_graph,"A", "E") == set([])
assert common_friends(practice_graph,"A", "F") == set(['C'])
assert common_friends(rj, "Mercutio", "Nurse") == set()
assert common_friends(rj, "Mercutio", "Romeo") == set()
assert common_friends(rj, "Mercutio", "Juliet") == set(["Romeo"])
assert common_friends(rj, "Mercutio", "Capulet") == set(["Escalus", "Paris"])


def number_of_common_friends_map(graph, user):
    """Returns a map (a dictionary), mapping from each user U to the number 
    of friends U has in common with the given user. The map keys are the 
    users who have at least one friend in common with the given user, 
    and are neither the given user nor one of the given user's friends.
    Example: a graph called my_graph and user "A" 
    (Note: This is NOT the practice_graph used in the assignment writeup.)
    Here is what is relevant about my_graph:
        - "A" and "B" have two friends in common
        - "A" and "C" have one friend in common
        - "A" and "D" have one friend in common
        - "A" and "E" have no friends in common
        - "A" is friends with "D" (but not with "B" or "C")
    Here is what should be returned:
      number_of_common_friends_map(my_graph, "A")  =>   { 'B':2, 'C':1 }
    """
    dict = {}
    for f0 in friends(graph,user):
        for f1 in friends(graph,f0):
            if ((f1 != user) and f1 not in friends(graph,user)):
                #print(f1)   
                if f1 not in dict.keys():
                    dict[f1] = 1
                else:
                    dict[f1] += 1
    return dict
    #print ("Remove this print statement once " + \
        #"number_of_common_friends is implemented")


assert number_of_common_friends_map(practice_graph, "A") == {'D': 2, 'F': 1}
assert number_of_common_friends_map(rj, "Mercutio") == \
    { 'Benvolio': 1, 'Capulet': 2, 'Friar Laurence': 1, 
      'Juliet': 1, 'Montague': 2 }


def number_map_to_sorted_list(map_with_number_vals):
    """Given map_with_number_vals, a dictionary whose values are numbers, 
    return a list of the keys in the dictionary.
    The keys are sorted by the number value they map to, from greatest
    number down to smallest number.
    When two keys map to the same number value, the keys are sorted by their
    natural sort order for whatever type the key is, from least to greatest.
    """
    #sorts the dictionary by key in ascending order and turns it into a list of tuples
    map_with_number_vals = sorted(map_with_number_vals.items(),key = operator.itemgetter(0))
    #sorts the list of tuples in descending order by its value
    map_with_number_vals = sorted(map_with_number_vals, key = operator.itemgetter(1),reverse=True)
   
    map_with_number_vals_list = [i for i,j in map_with_number_vals]
    return map_with_number_vals_list

assert number_map_to_sorted_list({"a":5, "b":2, "c":7, "d":5, "e":5}) == \
    ['c', 'a', 'd', 'e', 'b']


def recommend_by_number_of_common_friends(graph, user):
    """Return a list of friend recommendations for the given user.
    The friend recommendation list consists of names/IDs of people in
    the graph who are not yet a friend of the given user.  The order
    of the list is determined by the number of common friends (people
    with the most common friends are listed first).  In the
    case of a tie in number of common friends, the names/IDs are
    sorted by their natural sort order, from least to greatest.
    """
    
    common_friends = number_of_common_friends_map(graph, user)

    return(number_map_to_sorted_list(common_friends))
    #print ("Remove this print statement once " + \
    #    "recommend_by_number_of_common_friends is implemented")


assert recommend_by_number_of_common_friends(practice_graph,"A") == ['D', 'F']

assert recommend_by_number_of_common_friends(rj, "Mercutio") == \
    ['Capulet', 'Montague', 'Benvolio', 'Friar Laurence', 'Juliet']


###
### Problem 3
###

def influence_map(graph, user):
    """Returns a map (a dictionary) mapping from each person P to their 
    influence score, with respect to the given user. The map only 
    contains people who have at least one friend in common with the given 
    user and are neither the user nor one of the users's friends. 
    See the assignment for the definition of influence scores.
    """

    
    influencer_scores = dict()
    for fof in friends_of_friends(graph,user):
        score = 0 
        for item in common_friends(graph,user,fof):
              
            score = score + (1/(len(friends(graph,item))))
            influencer_scores[fof] = score
    return influencer_scores
    
    print ("Remove this print statement once influence_map is implemented")




assert influence_map(rj, "Mercutio") == \
    { 'Benvolio': 0.2, 'Capulet': 0.5833333333333333, 
      'Friar Laurence': 0.2, 'Juliet': 0.2, 'Montague': 0.45 }


def recommend_by_influence(graph, user):
    """Return a list of friend recommendations for the given user.
    The friend recommendation list consists of names/IDs of people in
    the graph who are not yet a friend of the given user.  The order
    of the list is determined by the influence score (people
    with the biggest influence score are listed first).  In the
    case of a tie in influence score, the names/IDs are sorted
    by their natural sort order, from least to greatest.
    """
    
    influence_mapping = influence_map(graph, user)
    #print(influence_mapping)
    return number_map_to_sorted_list(influence_mapping)



assert recommend_by_influence(rj, "Mercutio") == \
    ['Capulet', 'Montague', 'Benvolio', 'Friar Laurence', 'Juliet']


###
### Problem 4
###
    
def recommendation_check(graph):
    same_list = []
    diff_list = []
    for node in graph.nodes():
        if(recommend_by_influence(graph,node) == recommend_by_number_of_common_friends(graph,node)):
            same_list.append(node)
        else:
            diff_list.append(node)
    print("Unchanged Recommendations:",same_list)
    print("Changed Recommendations:",diff_list)
    
recommendation_check(rj)

###
### Problem 5
###

import pandas as pd

facebook = nx.Graph()
def create_facebook_graph():
    df = pd.read_table('./facebook-links.txt', delim_whitespace=True, names=('Node1', 'Node2', 'Timestamp'))    
    for line in range(1,len(df)):
        n1 = int(df.at[line,'Node1'])
        n2 = int(df.at[line,'Node2'])
        facebook.add_edge(n1,n2)
    
create_facebook_graph()
assert len(facebook.nodes()) == 63731
assert len(facebook.edges()) == 817090

###
### Problem 6
###

def recommend_by_number_of_common_friends_list(facebook,node):
    list_of_friends = recommend_by_number_of_common_friends(facebook,node)

    if(len(list_of_friends)<10):
        print(node,"(by number_of_common_friends):",list_of_friends)
        return(list_of_friends)
    else:
        print(node,"(by number_of_common_friends):",list_of_friends[:10])
        return(list_of_friends[:10])
        


###
### Problem 7
###


def recommend_by_influence_list(facebook,node):
    
    list_of_friends = recommend_by_influence(facebook,node)

    if(len(list_of_friends)<10):
        print(node,"(by influence):",list_of_friends)
        return(list_of_friends)
    else:
        print(node,"(by influence):",list_of_friends[:10])
        return(list_of_friends[:10])

#for n in facebook.nodes():   
#    if(n%1000==0):     
#        recommend_by_influence_list(facebook,n)

###
### Problem 8
###
        
same_list = []
diff_list = []
for node in facebook.nodes():
    if int(node)%1000 == 0:
        l1 = recommend_by_number_of_common_friends_list(facebook,node)
        l2 = recommend_by_influence_list(facebook,node)
        if(l1==l2):
            same_list.append(node)
        else:
            diff_list.append(node)
            
print("Same:",same_list)
print("Different:",diff_list)
    
    




