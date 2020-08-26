'''
Created on Aug 25, 2020

@author: haels
'''
import random
intervals = {'minor second': 1, 'major second': 2, 'minor third': 3, 'major third': 4, 'perfect fourth': 5,\
            'tritone': 6, 'perfect fifth': 7, 'minor sixth': 8, 'major sixth': 9, 'minor seventh': 10, 'major seventh': 11}

sharps = ['G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#']
flats = ['G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb']
directions = {'up': 1, 'down': -1}

sharp = True
while(True):
    user_answer = None
    interval = random.choice(list(intervals))
    direction = random.choice(list(directions))
    
    if(sharp==True):
        print('Use sharps in your answer. (e.g. \"A#\")')
        starting = random.choice(sharps)
        correct_answer = sharps[(sharps.index(starting)+intervals[interval]*directions[direction])%12]
    else:
        print('Use flats in your answer. (e.g. \"Ab\")')
        starting = random.choice(flats)
        correct_answer = flats[(flats.index(starting)+intervals[interval]*directions[direction])%12]
        
    print('What is a ' + interval + ' ' + direction + ' from ' + starting + '?')
    user_answer = input()
    
    while(user_answer.lower() != correct_answer.lower()):
        print("Incorrect. What is a " + interval  + ' ' + direction + ' from ' + starting + '?')
        user_answer = input()
        
    print("Correct. \r")
    sharp = not sharp