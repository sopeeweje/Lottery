#!/usr/bin/env python
# coding: utf-8

# ## (Press the play button at the top to run!)

# In[2]:


# Initialization
import itertools
import operator
rotations = ["medicine", "surgery", "neuro-psych-EM", "peds-obgyn"]

#----------------------------------------------------------------------------------#

#Create your rules
class Rule:
    def __init__(self, weight, rule):
        self.weight = weight
        self.rule = rule
    
    def get_score(self, permutation):
        score = self.rule(permutation)*self.weight
        return score    

#----------------------------------------------------------------------------------#

# For each rule, you have to specify:
#1. How important that rule is to you (give it a weight)
#2. What the rule is (using a lambda function). 
# The below rules act as an examples, you can write rules using similar format
    
# This rule makes medicine the first rotation is weighted to be more important than the others
med_first = Rule(10, lambda x: x.index("medicine") == 0)

# This rule makes neuro-psych-EM the second rotation but isn't weighted heavily
npm_second = Rule(3, lambda x: x.index("neuro-psych-EM") == 1)

# This rule avoids putting medicine and surgery back to back
no_b2b_medsurg = Rule(6, lambda x: abs(x.index("medicine")-x.index("surgery")) > 1)

# This rule promotes puting medicine before surgery
med_b4_surg = Rule(8, lambda x: x.index("medicine") > x.index("surgery"))

# This rule avoids putting surgery last
not_surg_last =  Rule(4, lambda x: x.index("surgery") != 3)

#********MAKE SURE ALL YOUR RULES ARE IN THIS LIST****************
rules = [med_first, npm_second, no_b2b_medsurg, med_b4_surg, not_surg_last]

#----------------------------------------------------------------------------------#

# Figure out your order
order = {}
for rotation_order in list(itertools.permutations(rotations)):
    score = sum([rule.get_score(rotation_order) for rule in rules])
    order[" | ".join(rotation_order)] = score

#----------------------------------------------------------------------------------#    

# Print your order
index = 1
for element in sorted(order.items(), key=operator.itemgetter(1), reverse=True):
    print("{}: {} = {}".format(str(index), element[0], str(element[1])))
    index+=1
    print("{}: {} = {}".format(str(index), element[0], str(element[1])))
    index+=1


# In[ ]:




