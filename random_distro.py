"""
randomly assign people to groups

"""

import random
#group 1: for megan
#grop2 : for padma
#group3 : for suresh

members=5
participants=['Tony','Natraj','Mahesh','Nitin','Raghu','Rama','Ravi','Saravanan','Latha','Suneetha','Taskeen','Vijay','Sateesh','Krishna','Cynthia']
random.shuffle(participants)
for i in range(len(participants) // members+1):
    print('Group {} consists of:'.format(i+1))
    group=participants[i*members:i*members+members]
    for participant in group:
        print(participant)
