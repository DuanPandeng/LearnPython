import time
import os
import array


import ctypes

#use "windll" for stdcall functions (eg. the Windows API)
#ctypes.

myLibrary = ctypes.LibraryLoader(ctypes.WinDLL).LoadLibrary("D:\\GerryHendratno\\ProjekteBsp\\CANape\\CANape_Automatisierung\\Python\\API_DLL_mitPython\\CANapAPI.dll")

#"cdll" for cdecl functions
#myLibrary = ctypes.windll.LoadLibrary("D:\\GerryHendratno\\ProjekteBsp\\CANape\\CANape_Automatisierung\\Python\\API_DLL_mitPython\\CANapAPI.dll")

gWorkDir = ctypes.c_char_p ("D:\\GerryHendratno\\00_MyTestSystem\\")
gDebugMode = ctypes.c_bool(True)
gClearDevList = ctypes.c_bool(False)
gModalMode = ctypes.c_bool(False)
hexmode = ctypes.c_bool(False)
Online = ctypes.c_bool(True)
myValueCalib = 0
MyXCPMdlHandle = ctypes.c_long(1)
myHandle = ctypes.c_long(1)
myValueCalib = ctypes.c_long(1)
ret = ctypes.c_bool(False)
#myRet = ctypes.c_int(1)
myRet = 1

ret = myLibrary.Asap3Init5(ctypes.byref(myHandle), ctypes.c_long(120000), gWorkDir, ctypes.c_long(2048), ctypes.c_long(1024), gDebugMode, gClearDevList, hexmode, gModalMode)
#ret = myLibrary.Asap3Init5(myHandle, 120000, gWorkDir, 2048, 1024, gDebugMode, gClearDevList, hexmode, gModalMode)
#ret = 0
ret = myLibrary.Asap3CreateModule2(myHandle, 'XCPsim', 'XCPsim2.a2l', 2 , 1, Online, ctypes.pointer(MyXCPMdlHandle))
myRet = 1
myRet = myRet & ret

ret = myLibrary.Asap3CreateModule2(myHandle, 'XCPsim', 'XCPsim.a2l', 2 , 1, Online, ctypes.pointer(MyXCPMdlHandle))
myRet = 1
myRet = myRet & ret

ret = myLibrary.Asap3ReadCalibrationObject(myHandle, MyXCPMdlHandle, "ampl", 1, ctypes.byref(myValueCalib))

myValue = myValueCalib.value
#ret = myLibrary.Asap3ReadCalibrationObject(myHandle, MyXCPMdlHandle, "testString", 1, myValueCalib);


#ret = myLibrary.Asap3ReadCalibrationObject(myHandle, MyXCPMdlHandle, "testString", 1, myValueCalib);


ret = myLibrary.Asap3Exit(myHandle)