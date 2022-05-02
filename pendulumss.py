#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 22:12:55 2022

@author: morganstump
"""

import pendulum

print("Welcome to Pendulum")

print("This is an example of what pendulum strings looks like: ")
now = pendulum.now("Europe/Paris")
x = now.in_timezone("America/New_York")
x = now.to_iso8601_string()
x = now.add(days=2)
print(x)

enter1 = input("Press enter to get local time zone: ")
#local time zone
dt = pendulum.local(2022, 4, 4)
print("Your local timezone is: ", dt.timezone.name, "\n")
    
enter2 = input("Press enter to get Shanghai timezone and offset: ")
#using datetime()
dt1 = pendulum.datetime(2022, 4, 4, tz = 'Asia/Shanghai', dst_rule=pendulum.POST_TRANSITION)
tz = pendulum.timezone('Asia/Shanghai')
time = pendulum.datetime(2022, 4, 4, tz=tz, dst_rule=pendulum.POST_TRANSITION)
print("The timezone in Shanghai is: ", time)
print("The time offset for Shanghai is: ", pendulum.from_timestamp(0, 'Asia/Shanghai').offset_hours, "hours.")
print()

enter3 = input("Press enter to get the current date and time: ")
#using now() method
#gives current time
current = pendulum.now()
print("The current date and time is: " , current)
print()

enter4 = input("Press enter to get today's date: ")
#uses today() method
#prints today date
today = pendulum.today()
print("The date today is: ", today)
print()

enter5 = input("Press enter to get tomorrow's and yesterday's date: ")
#uses tomorrow() method
#prints tomorrow date
tomorrow = pendulum.tomorrow()
print("The date tomorrow is: ", tomorrow)
print()
yesterday = pendulum.yesterday()
print("The date yesterday was: ", yesterday)
print()


enter6 = input("Press enter to see the format() method in use: ")
#uses the from_format() method
dt3 = pendulum.from_format('2022-04-04 23', 'YYYY-MM-DD HH')
print(dt3)
print()

enter7 = input("Press enter to see the parse() method used to find specific information from a string: ")
#use the parse method and its attributes.properties to print the strings information piece by piece
dt = pendulum.parse('1970-03-16T12:45:11.134724')
print(dt)
print("The year of this timestamp is: ", dt.year)
print("The month of this timestamp is: ", dt.month)
print("The day of this timestamp is: ", dt.day)
print("The hour of this timestamp is: ", dt.hour)
print("The minute of this timestamp is: ", dt.minute)
print("The second of this timestamp is: ", dt.second)
print("The microsecond of this timestamp is: ", dt.microsecond)
print("The day of the week of this timestamp is: ", dt.day_of_week)
print("The day of the year of this timestamp is: ", dt.day_of_year)
print("The week of the month of this timestamp is: ", dt.week_of_month)
print("The week of the year of this timestamp is: ", dt.week_of_year)
print("The days in the month of this timestamp is: ", dt.days_in_month)
print("The timestamp of this is: ", dt.timestamp())
print("The float timestamp of this is: ", dt.float_timestamp)
print("The int timestamp of this is: ", dt.int_timestamp)

#finding the age of timestamp
dt = pendulum.parse('1970-03-16T12:45:11.134724').age
print("The age of this timestamp is: ", dt)

enter8 = input("Press enter to look at different time zones and differences: ")
#time difference, user input
#hour is off by 1 hour depending on DST
input1 = input("Pick a time zone: \na-Austrailia/Adelaide, \nb-America/Vancouver, \nc-America/New_York, \nd-Europe/Berlin \n")
input2 = input("Pick a time to compare to it: \na-Asia/Seoul, \nb-Pacific/Rarotonga, \nc-Pacific/Marquesas\n")
if input1 == 'a':
    dt_adelaide = pendulum.datetime(2022, 1, 1, tz='Australia/Adelaide', dst_rule=pendulum.POST_TRANSITION) 
    if input2 == 'a':
        dt_seoul = pendulum.datetime(2022, 1, 1, tz='Asia/Seoul', dst_rule=pendulum.POST_TRANSITION)
        print("The hour difference between Adelaide and Seoul: ", dt_seoul.diff(dt_adelaide).in_hours(), "hours.")
        print()
    if input2 == 'b':
        dt_rarotonga = pendulum.datetime(2022, 1, 1, tz='Pacific/Rarotonga', dst_rule=pendulum.POST_TRANSITION)
        print("The hour difference between Adelaide and Rarotonga: ", dt_rarotonga.diff(dt_adelaide).in_hours(), "hours.")
        print()
    if input2 == 'c':
        dt_marquesas = pendulum.datetime(2022, 1, 1, tz='Pacific/Marquesas', dst_rule=pendulum.POST_TRANSITION)
        print("The hour difference between Adelaide and Marquesas: ", dt_marquesas.diff(dt_adelaide).in_hours(), "hours.")
        print()   
if input1 == 'b':
    dt_vancouver = pendulum.datetime(2022, 1, 1, tz='America/Vancouver', dst_rule=pendulum.POST_TRANSITION)
    if input2 == 'a':
        dt_seoul = pendulum.datetime(2022, 1, 1, tz='Asia/Seoul', dst_rule=pendulum.POST_TRANSITION)
        print("The hour difference between Vancouver and Seoul: ", dt_seoul.diff(dt_vancouver).in_hours(), "hours.")
        print()
    if input2 == 'b':
        dt_rarotonga = pendulum.datetime(2022, 1, 1, tz='Pacific/Rarotonga', dst_rule=pendulum.POST_TRANSITION)
        print("The hour difference between Vancouver and Rarotonga: ", dt_rarotonga.diff(dt_vancouver).in_hours(), "hours.")
        print()
    if input2 == 'c':
        dt_marquesas = pendulum.datetime(2022, 1, 1, tz='Pacific/Marquesas', dst_rule=pendulum.POST_TRANSITION)
        print("The hour difference between Vancouver and Marquesas: ", dt_marquesas.diff(dt_vancouver).in_hours(), "hours.")
        print() 
if input1 == 'c':
    dt_newyork = pendulum.datetime(2022, 1, 1, tz='America/New_York', dst_rule=pendulum.POST_TRANSITION) 
    if input2 == 'a':
        dt_seoul = pendulum.datetime(2022, 1, 1, tz='Asia/Seoul', dst_rule=pendulum.POST_TRANSITION)
        print("The hour difference between New York and Seoul: ", dt_seoul.diff(dt_newyork).in_hours(), "hours.")
        print()
    if input2 == 'b':
        dt_rarotonga = pendulum.datetime(2022, 1, 1, tz='Pacific/Rarotonga', dst_rule=pendulum.POST_TRANSITION)
        print("The hour difference between New York and Rarotonga: ", dt_rarotonga.diff(dt_newyork).in_hours(), "hours.")
        print()
    if input2 == 'c':
        dt_marquesas = pendulum.datetime(2022, 1, 1, tz='Pacific/Marquesas', dst_rule=pendulum.POST_TRANSITION)
        print("The hour difference between New York and Marquesas: ", dt_marquesas.diff(dt_newyork).in_hours(), "hours.")
        print() 
if input1 == 'd':
    dt_berlin = pendulum.datetime(2022, 1, 1, tz='Europe/Berlin', dst_rule=pendulum.POST_TRANSITION) 
    if input2 == 'a':
        dt_seoul = pendulum.datetime(2022, 1, 1, tz='Asia/Seoul', dst_rule=pendulum.POST_TRANSITION)
        print("The hour difference between Berlin and Seoul: ", dt_seoul.diff(dt_berlin).in_hours(), "hours.")
        print()
    if input2 == 'b':
        dt_rarotonga = pendulum.datetime(2022, 1, 1, tz='Pacific/Rarotonga', dst_rule=pendulum.POST_TRANSITION)
        print("The hour difference between Berlin and Rarotonga: ", dt_rarotonga.diff(dt_berlin).in_hours(), "hours.")
        print()
    if input2 == 'c':
        dt_marquesas = pendulum.datetime(2022, 1, 1, tz='Pacific/Marquesas', dst_rule=pendulum.POST_TRANSITION)
        print("The hour difference between Berlin and Marquesas: ", dt_marquesas.diff(dt_berlin).in_hours(), "hours.")
        print() 


enter9 = input("Press enter to pick from a list of timezones: ")
#allow user to pick a time zone they want to look at
user = input("Pick a time zone you want to look at: \na-Qatar, \nb-Bermuda, \nc-Egypt, \nd-Antarctica/Palmer, \ne-Los Angeles, \nf-Samoa\n")
if user == 'a':
    dt = pendulum.datetime(2022, 4, 4, tz = 'Asia/Qatar', dst_rule=pendulum.POST_TRANSITION)
    tz = pendulum.timezone('Asia/Qatar')
    time = pendulum.datetime(2022, 4, 4, tz=tz)
    print("The timezone in Asia/Qatar is: ", time)
if user == 'b':
    dt = pendulum.datetime(2022, 4, 4, tz = 'Atlantic/Bermuda', dst_rule=pendulum.POST_TRANSITION)
    tz = pendulum.timezone('Atlantic/Bermuda')
    time = pendulum.datetime(2022, 4, 4, tz=tz)
    print("The timezone in Atlantic/Bermuda is: ", time)
if user == 'c':
    dt = pendulum.datetime(2022, 4, 4, tz = 'Egypt', dst_rule=pendulum.POST_TRANSITION)
    tz = pendulum.timezone('Egypt')
    time = pendulum.datetime(2022, 4, 4, tz=tz)
    print("The timezone in Egypt is: ", time)
if user == 'd':
    dt = pendulum.datetime(2022, 4, 4, tz = 'Antarctica/Palmer', dst_rule=pendulum.POST_TRANSITION)
    tz = pendulum.timezone('Antarctica/Palmer')
    time = pendulum.datetime(2022, 4, 4, tz=tz)
    print("The timezone in Antarctica/Palmer is: ", time)
if user == 'e':
    dt = pendulum.datetime(2022, 4, 4, tz = 'America/Los_Angeles', dst_rule=pendulum.POST_TRANSITION)
    tz = pendulum.timezone('America/Los_Angeles')
    time = pendulum.datetime(2022, 4, 4, tz=tz)
    print("The timezone in Los Angeles is: ", time)
if user == 'f':
    dt = pendulum.datetime(2022, 4, 4, tz = 'Pacific/Samoa', dst_rule=pendulum.POST_TRANSITION)
    tz = pendulum.timezone('Pacific/Samoa')
    time = pendulum.datetime(2022, 4, 4, tz=tz)
    print("The timezone in Samoa is: ", time)
    
print("\nThank you for your time!")








