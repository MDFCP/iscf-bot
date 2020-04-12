import os
import pandas as pd
import html
import heapq
from datetime import datetime

WB_INDEX = 'webinars'

def submit(db, args):

    if len(args) != 3:
        return 'Something is missing. You should follow "<NAME> <DD/MM/YYYY hh:mm AM/PM> <WEBINAR_LINK>" format to submit a webinar'
    
    if not db.get('WB_INDEX', False):
        db[WB_INDEX] = []
    
    try:
        parsed_date = datetime.strptime(args[1], '%d/%m/%Y %I:%M %p')
    except:
        return 'Date should be formatted as <DD/MM/YYYY hh:mm AM/PM>. eg: "12/04/2020 3:05 PM"'

    if parsed_date < datetime.now():
        return 'Is this webinar a ghost? Buddy, check the date. You are living in the past.'

    temp_heap = db[WB_INDEX]

    heapq.heappush(temp_heap, (parsed_date, {
        'name': args[0],
        'link': args[2]
    }))

    db[WB_INDEX] = temp_heap
    
    return 'Thanks!! You submitted **' + args[0] + '** which is scheduled at **' + datetime.strftime(parsed_date, '%d %b, %Y %I:%M %p') + '**.'

# args: !wb get 3
def get(db, args):
    if len(args) != 1:
        return 'You should enter number of upcoming webinars as an argument.'
    
    num = 0
    try:
        num = int(args[0])
    except:
        return 'You entered a non numeric value as the argument.'

    res = ''
    #stop_at = num if num < len(db[WB_INDEX]) else len(db[WB_INDEX])
    heap = db[WB_INDEX]
    cnt = 0
    while(True):
        if cnt >= num or len(heap) == 0 or cnt >= len(heap):
            break
        
        if heap[0][0] < datetime.now():
            heapq.heappop(heap)
        else:
            res = res + 'Name: <' + heap[cnt][1]['link'] + '|**' + heap[cnt][1]['name'] + '**>. \nDate and Time: **' + datetime.strftime(heap[cnt][0], '%d %b, %Y %I:%M %p') + '** \n\n'
            cnt = cnt + 1

    print(res[:-2])

def notify(self):
    self.send(self.build_identifier("#bot-test"), 'notify')

if '__main__' == __name__:
    print(submit({}))