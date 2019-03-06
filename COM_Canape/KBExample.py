import win32com.client # the module needed for win32 COM API functions
import time
import os
import array
# -*- coding: utf-8 -*-

canape = win32com.client.Dispatch('CANape.Application')
print'\n'
print'CANape dispatched.'

#Init CANape
canape.Open1("D:\\VectorTools\\CANape13SP2\\Examples\\XCPDemo",1,50000,True) 	
print'CANape initialized.'

#Init XCP Device
dev = canape.Devices.Add("XCPsim_1","XCPsim.a2l","XCP",1)
print'Device \'XCPsim_1\' added.'

#Adding the ampl object
dev.CalibrationObjects.Add("ampl")
calob = dev.CalibrationObjects.Item("ampl")
print'ampl added as calibration object.'

#Adding the PWM object with polling and configuring it for MDF file
XCP_1_Task = dev.Tasks("polling")
XCP_1_Task.SamplingTime = 500;
XCP_1_Task.Channels.Add("PWM")
XCP_1_Task.Channels("PWM").Save2MDF=1

print'Start the measurement.....'
canape.Measurement.Start()

calob.Read()
myValue = calob.Value

print'Value of ampl: %i.' % myValue

calob.value = 95
calob.write()

calob.Read()
myValue = calob.Value

print'Value of ampl: %i.' % myValue

time.sleep(10)

canape.Measurement.Stop()
time.sleep(10)
print'\nStop the measurement.....\n'
print'\nExit CANape...Thank you for using!\n'
canape.Quit()

