# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 13:35:19 2023

@author: ShendR
"""

import os


DAProxy_path = 'D:\\IRVB\\mastda\\DAProxy'
DAProxy_file = 'prx' + target_folder.translate({ord('-'):None})[2:] + '.log'
DAProxy_full_path = DAProxy_path+'\\log\\'+DAProxy_file
print('checking file '+DAProxy_full_path)
while not os.path.exists(DAProxy_full_path):
    print('checking file '+DAProxy_full_path)
    test = input('the log file '+DAProxy_full_path+" doesn't exists. r to rety or input the full path to the log file (including log file name)")
    if test == 'r':
        continue
    else:
        DAProxy_full_path = test
def return_shot_and_state(DAProxy_full_path=DAProxy_full_path):
    done = 0
    while done==0:
        try:
            f = open(DAProxy_full_path,'r')
            for row in f:
                None
            last_pulse = int(row[row.find('shot=') + len('shot='):row.find('&state')])
            MASTU_state = int(row[row.find('state=') + len('state='):row.find('&)\n')])
            done = 1
        except:
            print('shot info missing in log')
            wait_while_moving_mouse(10/60,wait_for_move=2)
    return last_pulse,MASTU_state

if __name__ == '__main__':

    last_pulse,MASTU_state = return_shot_and_state()
