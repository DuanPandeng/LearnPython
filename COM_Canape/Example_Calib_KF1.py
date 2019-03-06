import win32com.client # the module needed for win32 COM API functions
import time
import os
import array
# -*- coding: utf-8 -*-

canape = win32com.client.Dispatch('CANape.Application')
print'\n'
print'CANape dispatched.'

#Init CANape
canape.Open1("D:\\GerryHendratno\\Programme\\Vector\\CANape\\11.0 SP3 (Released)\\Examples\\CCPDemo\\",1,50000,False) 	
print'CANape initialized.'

#Init CCP Device
dev = canape.Devices.Add("CCPsim","CCPsim.a2l","CCP",1)
print'Device \'CCPsim\' added.'

#Adding the calib. object
dev.CalibrationObjects.Add("KF1")
calob = dev.CalibrationObjects.Item("KF1")
print'KF1 added as calibration object.'

#Getting the dimension of the calib. object
XDim = calob.XDim
print'XDim of KF1: %i.' % XDim
YDim = calob.YDim
print'YDim of KF1: %i.' % YDim

#Create table for the values
myArray_KF1 = [ [ 0 for col in range(YDim) ] for row in range(XDim) ]

#Reading KF1
calob.Read()
myArray_KF1_tuple = calob.Value

# show original table
print '=========================================='
print 'ORIGINAL_TUPLE'
print '=========================================='
for row in myArray_KF1_tuple:
    print row
print '=========================================='

for a in range(YDim):
    for b in range(XDim):
        myArray_KF1[a][b] = myArray_KF1_tuple[a][b]
        #print 'KF1 [%i,%i]: %f' % (a, b, myArray_KF1[a][b])

# show copied table as array
print '=========================================='
print 'ORIGINAL_TUPLE_COPIED_ARRAY'
print '=========================================='
for row in myArray_KF1:
    print row
print '=========================================='

#Calibrating KF1 on the 1st line element
for a in range(XDim):
    myArray_KF1[a][0] = 0.1 - (a * 0.01)
    #print 'KF1 [%i,0]: %f' % (a, myArray_KF1[a][0])

#show changed array
print '=========================================='
print 'CHANGED_TUPLE_COPIED_ARRAY'
print '=========================================='
for row in myArray_KF1:
    print row
print '=========================================='

#Create table for rotating the array
myArray_KF1_rotated = [ [ 0 for col in range(YDim) ] for row in range(XDim) ]

#Rotate the array
for a in range(YDim):
    for b in range(XDim):
        myArray_KF1_rotated[a][b] = myArray_KF1[b][a]
            
#Rotated array
print '=========================================='
print 'ROTATED_CHANGED_TUPLE_COPIED_ARRAY'
print '=========================================='
for row in myArray_KF1_rotated:
    print row
print '=========================================='

calob.Value = myArray_KF1_rotated

#Write the changes
calob.Write()
time.sleep(1)   #Giving CANape 1s to write down the value to ECU
print'Some values of KF1 have been changed.'

#Reading KF1 again
calob.Read()
myArray_KF1_tuple = calob.Value

# show it
print '=========================================='
print 'ORIGINAL_TUPLE_READBACK'
print '=========================================='
for row in myArray_KF1_tuple:
    print row
print '=========================================='

#Checking the values
#for a in range(1):
#    for b in range(XDim):
#        if KF1_Changes[a][b] == myArray_KF1_tuple[a][b]:
#            print 'KF1 [%i,%i] new value: %f' % (a, b, myArray_KF1_tuple[a][b])
#        else:
#            print 'KF1 [%i,%i] new value: %f  ---> Nicht OK.' % (a, b, myArray_KF1_tuple[a][b])

print'\nExit CANape...Thank you for using!\n'
canape.QuitNonModal()

