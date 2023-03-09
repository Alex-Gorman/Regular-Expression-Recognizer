import time

from FAdo.reex import str2regexp
from FAdo.conversions import *
from FAdo.fa import *
from FAdo.reex import *
from FAdo.fio import *
from prettytable import PrettyTable

# Get the Regular Expression as an input string from user
regularExpressionString = input("Enter a Regular Expression: ")

# Get the strings to check if they are in the language of the regular expression
string = input("Enter a list of strings: ")
strings = string.split(" ")

# Put all the character of the regular expression string into a hashset
regularExpressionSet = set(regularExpressionString)

# Check if one of the strings contains a character not in the language of the regular expression
for s in strings:
    for c in s:
        if c not in regularExpressionSet:
            print("You entered a string that does not contain a character in the Language of" +
                    "the regular expression. Please try again. ")
            exit()

# Convert the regular expression string to regular expression object
regularExpression = str2regexp(regularExpressionString)

# Convert the regular expression to an NFA
nfa_convert_start_time = time.time()
nfa = regularExpression.nfaThompson()
nfa_convert_end_time = time.time()

# Convert the NFA to a DFA
dfa_convert_start_time = time.time()
dfa = nfa.toDFA()
dfa_convert_end_time = time.time()

# Create the table to display
my_table = PrettyTable()
my_table.field_names = ["Strings", "e-NFA Accepted ", "Time NFA", "DFA Accepted", "Time DFA"]

# Go through every string
for s in strings:
    nfa_start_time = time.time()
    nfa_accepted = nfa.evalWordP(s)
    timeNFA = (time.time()-nfa_start_time)
    dfa_start_time = time.time()
    dfa_accepted = dfa.evalWordP(s)
    timeDFA = (time.time() - dfa_start_time)
    my_table.add_row([s, nfa_accepted, timeNFA, dfa_accepted, timeDFA])


# Print the time to convert the DFA and NFA and the number of states for both
print("Time to convert to NFA: "+str(nfa_convert_end_time-nfa_convert_start_time)+" seconds")
print("Time to convert to DFA: "+str(dfa_convert_end_time-dfa_convert_start_time)+" seconds")
print("Number of states in the NFA: "+str(len(nfa)))
print("Number of states in the DFA: "+str(len(dfa)))

# Display the table
print(my_table)

# Display the DFA and NFA
dfa.display()




# # m3 = regularExpression.nfaPosition().toDFA()
#
# m3 = regularExpression.nfaThompson()
#
# m4 = m3.toDFA()
# print(type(m4))
#
# m5 = DFA()
# print(type(m5))
# # print(m5.evalWordP("001"))
#
# # try
# print(m4.evalWordP("aaa"))




