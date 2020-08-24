#!/usr/bin/env python

import os
import datetime

Current_Date = datetime.datetime.today().strftime ('%d-%b-%Y')
os.rename(r'/var/backup/scripts/test1.txt',r'/var/backup/scripts/test2_' + str(Current_Date) + '.txt')

