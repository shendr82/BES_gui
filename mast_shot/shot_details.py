#!/usr/bin/env python

from ftplib import FTP
import datetime as DT
import time
FTP_SERVER = 'daq0.mast.l'
SHOT_FILE_NAME = 'mshot.dat'
DATE_TIME_FORMAT = '%d-%b-%Y %H:%M:%S'

def get_mshot_file():
   """
   To get the mshot file from daq0 machine.
   mshot file contains the latest shot number and the shot date time
   """
   try:
      ftp = FTP(FTP_SERVER)
      ftp.login()
      with open(SHOT_FILE_NAME, 'wb') as fp:
         ftp.retrbinary('RETR ' + SHOT_FILE_NAME, fp.write)
      ftp.quit()
   except Exception as ex:
      print (ex)

def get_shot_number():
   """
   To get the shot number from the LOCAL mshot file.
   Make sure the get_mshot_file() function called prior to get the latest shot number.
   """
   try:
      with open(SHOT_FILE_NAME, 'rb') as fp:
         return fp.readlines()[0].strip().decode("utf-8")
   except Exception as ex:
      print (ex)

def get_shot_datetime():
   """
   To get the shot date time from the LOCAL mshot file.
   Make sure the get_mshot_file() function called prior to get the latest shot date and time.
   """
   try:
      with open(SHOT_FILE_NAME, 'rb') as fp:
         return fp.readlines()[1].strip().decode("utf-8")
   except Exception as ex:
      print (ex)

def get_shot_details(is_latest = True):
   """
   To get the latest shot number and shot date time from the latest mshot file, if is_latest is true
   This function download the mshot.dat file and retrive the information.
   So, it is returning the latest shot details.
   """
   try:
      if (is_latest):
         get_mshot_file()
      with open(SHOT_FILE_NAME, 'rb') as fp:
         shot_details = fp.readlines()[0:2]
      return [line.strip().decode("utf-8") for line in shot_details]
   except Exception as ex:
      print (ex)

def timestring_now():
   """
   To get the time string format as same as shot time string.
   This function shall be useful to do any manipulation with shot time string.
   To convert to DataTime object, use timestring_to_datetime function.
   """
   return DT.datetime.now().strftime(DATE_TIME_FORMAT)

def timestring_to_datetime(shot_datetime):
   """
   To convert shot time string format to DataTime object.
   """
   return DT.datetime.strptime(shot_datetime, DATE_TIME_FORMAT)

def time_since_shot(shot_datetime):
   """
   To get the elapsed time between now and the given shot time.
   """
   return (DT.datetime.now() - timestring_to_datetime(shot_datetime))

def time_since_last_shot():
   """
   To get the elapsed time between now and the latest shot.
   """
   return time_since_shot(timestring_to_datetime(get_shot_details()[1]))

def timestring_to_epoch(time_string):
   """
   To get the timestring to epoch
   """
   return float(time.mktime(timestring_to_datetime(time_string).timetuple()))

def timedelta_to_seconds(time_delta):
   """
   To get the time delta to seconds
   use *_since* APIs to convert as seconds
   """
   return float(time_delta.total_seconds())

def get_filename(is_latest = True):
   """
   To get file name
        If is_latest is True, then get the latest shot detail and form file name string
        Else use the already downloaded mshot.dat file and form file name string
   """
   shot_details = get_shot_details(is_latest)
   shot_datetime = timestring_to_datetime(timestring_now()).strftime("%Y%m%d_%H%M")
   return shot_details[0] + "_" + shot_datetime
