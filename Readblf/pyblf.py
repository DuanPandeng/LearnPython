"""
note:
put binlog.dll, binlog.lib, bl.dll, bl.lib of x64_release at pyblf.py file folder
"""

from ctypes import *

BL_OBJ_TYPE_CAN_MESSAGE = 1


class FileStatisticsEx(Structure):
    _fields_ = [
        ("mStatisticsSize", c_uint32),
        ("mApplicationID", c_ubyte),
        ("mApplicationMajor", c_ubyte),
        ("mApplicationBuild", c_ubyte),
        ("mApplicationID", c_ubyte),
        ("mFileSize", c_uint64),
        ("mUncompressedFileSize", c_uint64),
        ("mObjectCount", c_uint32),
        ("mObjectsRead", c_uint32),
        ("startYear", c_uint16),
        ("startMonth", c_uint16),
        ("startDayOfWeek", c_uint16),
        ("startDay", c_uint16),
        ("startHour", c_uint16),
        ("startMinute", c_uint16),
        ("startSecond", c_uint16),
        ("startMilliseconds", c_uint16),
        ("lastYear", c_uint16),
        ("lastMonth", c_uint16),
        ("lastDayOfWeek", c_uint16),
        ("lastDay", c_uint16),
        ("lastHour", c_uint16),
        ("lastMinute", c_uint16),
        ("lastSecond", c_uint16),
        ("lastMilliseconds", c_uint16)]


class HeaderBase(Structure):
    _fields_ = [
        ("mSignature", c_uint32),
        ("mHeaderSize", c_uint16),
        ("mHeaderVersion", c_uint16),
        ("mObjectSize", c_uint32),
        ("mObjectType", c_uint32)]


class CANMessage(Structure):
    _fields_ = [
        ("mSignature", c_uint32),
        ("mHeaderSize", c_uint16),
        ("mHeaderVersion", c_uint16),
        ("mObjectSize", c_uint32),
        ("mObjectType", c_uint32),
        ("mObjectFlags", c_uint32),
        ("mClientIndex", c_uint16),
        ("mObjectVersion", c_uint16),
        ("mObjectTimeStamp", c_uint64),
        ("mChannel", c_uint16),
        ("mFlags", c_ubyte),
        ("mDLC", c_ubyte),
        ("mID", c_uint32),
        ("Data", c_ubyte * 8)]


def Open(file):
    fileStatisticsEx = FileStatisticsEx()
    success = bl_Dll.OpenBLFile(file.encode("utf-8"), byref(fileStatisticsEx))
    if success:
        return fileStatisticsEx
    else:
        return None


def Read():
    headerBase = HeaderBase()
    canMessage = CANMessage()
    success = bl_Dll.ReadBLObject(byref(headerBase), byref(canMessage))
    if success and headerBase.mObjectType == BL_OBJ_TYPE_CAN_MESSAGE:
        return canMessage
    else:
        return None


def Close():
    return bl_Dll.CloseBLFile()


def Test(file):
    # open
    fileStatisticsEx = Open(file)
    if fileStatisticsEx == None:
        return
    print(fileStatisticsEx.mObjectCount)
    # read
    for i in range(0, fileStatisticsEx.mObjectCount):
        canMessage = Read()
        if canMessage != None:
            print("Index={},TimeStamp={},Channel={},ID={},DLC={},Data={}".format(i, canMessage.mObjectTimeStamp,
                                                                                 canMessage.mChannel,
                                                                                 canMessage.mID, canMessage.mDLC,
                                                                                 bytearray(canMessage.Data)))
            # print(canMessage.Data[0])
    # close
    print(Close())


# load dll
bl_Dll = cdll.LoadLibrary("bl.dll")
# print(vars(bl_Dll))

# interface
# open
bl_Dll.OpenBLFile.argtypes = [c_char_p, POINTER(FileStatisticsEx)]
bl_Dll.OpenBLFile.restype = c_bool
# read
bl_Dll.ReadBLObject.argtypes = [POINTER(HeaderBase), POINTER(CANMessage)]
bl_Dll.ReadBLObject.restype = c_bool
# close
bl_Dll.CloseBLFile.restype = c_bool

