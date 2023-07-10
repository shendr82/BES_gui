#!/usr/bin/env python3
import mast_shot.shot_details as shot

print (shot.get_shot_details(True))
print (shot.timestring_to_datetime(shot.get_shot_datetime()))
print (shot.time_since_shot(shot.get_shot_datetime()))
print (shot.timestring_now())
print (shot.get_shot_details())
print (shot.timestring_to_epoch(shot.get_shot_details()[1]))
print (shot.timestring_to_epoch(shot.timestring_now()))
print (shot.timedelta_to_seconds(shot.time_since_shot(shot.get_shot_details()[1])))


