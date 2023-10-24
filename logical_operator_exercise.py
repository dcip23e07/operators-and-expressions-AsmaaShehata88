"""
What do the following expressions evaluate to? (5 > 4) and (3 == 5) not (5 > 4) (5 > 4) or 
(3 == 5) not ((5 > 4) or (3 == 5)) (True and True) and (True == False) (not False) or (not True)
"""

(5 > 4) and (3 == 5) #False

not (5 > 4)  #False

(5 > 4) or (3 == 5) #True

not ((5 > 4) or (3 == 5)) # False
#not((true) or (false))
#not(true) = false

(True and True) and (True == False) #False

(not False) or (not True) # True