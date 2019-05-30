import struct
import numpy as np
import pandas as pd
import util
import time
import os
import math

class ETH:

    VAR_SIZE = {'E_VT_sint8': 1,
              	'E_VT_uint8': 1,
               	'E_VT_bool': 1,
             	'E_VT_sint16': 2,
               	'E_VT_uint16': 2,
               	'E_VT_sint32': 4,
               	'E_VT_uint32': 4,
               	'E_VT_float': 4,
               	'E_VT_double': 8}

    VAR_CMD = {'E_VT_sint8': '<b',
			   'E_VT_uint8': '<B',
			   'E_VT_bool': '<?',
			   'E_VT_sint16': '<h',
			   'E_VT_uint16': '<H',
			   'E_VT_sint32': '<l',
			   'E_VT_uint32': '<L',
			   'E_VT_float': '<f',
			   'E_VT_double': '<d'}
			   
    def __init__(self, data_file, config_file):
        """
        parse class constructor\n
        :param data_file :    eth dat file\n
        :param config_file :  ethVarList.info file\n
        """
        self.file = data_file
        self.conf = config_file
        self.file_size = os.path.getsize(data_file)
        self.packet_header = 40  # 40 bytes of header in each packet
        self.packet_end = 8  # 8 bytes of ender in each packet
        self.dat_end = 1024  # 1024 bytes of added version information in each dat file
        self.start_time = util.get_time_str(self.file)
        self.info = pd.read_csv(config_file, sep='\s+', names=['name', 'offset', 'datatype'])
        self.info['datasize'] = [self.VAR_SIZE[x] for x in self.info['datatype']]
        self.packet_size = int(math.ceil((self.info['offset'].iloc[-1] + self.VAR_SIZE[self.info['datatype'].iloc[-1]])/4.0)*4)+ self.packet_header + self.packet_end
        self.packet_num = (self.file_size - self.dat_end) / self.packet_size


    def find_first_packet(self):
        return 0
    
    def match(self, pattern):
        return []

    def signals(self, var_list=None):        
        if var_list is not None:
            all_signals = list(self.info['name'])
            idx = [x in var_list for x in all_signals]
            return self.info[idx]
        else:
            return self.info
            
    def parseAll(self):
        return self.parse(list(self.info['name']))
        
    def parse(self, var_list):
        """
        main parse function\n
        :param sigs: list of signal names\n
        :return: DataFrame object containing all data\n 
        """
        if len(var_list) == 0:
            print "Nothing to parse, exit..."
            return None
        else:
            print "Start to parse {} signal(s)...".format(len(var_list))
            
        start_time = time.time()

        signals = self.signals(var_list)
        M = int(self.packet_num)
        N = len(signals)
        P = self.packet_size
        sig_offset = list(signals['offset'])
        sig_size   = list(signals['datasize'])
        sig_pack   = [ self.VAR_CMD[x] for x in signals['datatype'] ]
                
        result = np.zeros((M, N))
        
        with open(self.file, 'rb') as f:
            packets = f.read(M*P)

        for i in range(M):
            for j in range(N):
                sig_loc  =  i*P + self.packet_header + sig_offset[j]               
                sig_byte = packets[ sig_loc : sig_loc + sig_size[j] ]
                result[i][j] = struct.unpack(sig_pack[j], sig_byte)[0]

        elapsed_time = time.time() - start_time
        print "Elapsed {} seconds".format(elapsed_time)
        
        df = pd.DataFrame(result, columns=signals['name']);
        return df

    def __str__(self):
		return "" + \
          "====================================================================\n" + \
          "Pandora Ethernet Data:\n" + \
          "--------------------------------------------------------------------\n" + \
		"data file     : "+ self.file + "\n" +\
		"config file   : "+ self.conf + "\n" +\
           "file size     : " + str(self.file_size) + "\n" +\
           "start time    : " + self.start_time + "\n" +\
           "packet size   : " + str(self.packet_size) + "\n" +\
           "num packets   : " + str(self.packet_num) + "\n" +\
           "num variables : " + str(len(self.info)) + "\n" +\
          "====================================================================\n" + \
		 ""
   
    def __repr__(self):
        return self.__str__()
		
if __name__ == '__main__':
    
	# select file
    eth = ETH(data_file='/adas_data/PP0-02/20180531T135920/eth_20180531T141424.dat',
              config_file='/adas_data/PP0-02/20180531T135920/ethVarList.info' )
    print str(eth)

    print "================================================================================="
    eth.parse(['VehSts-Veh_Spd'])
    

'''
jiayou@webdev:~/adp/PandoraSDK/package$ head /adas_data/PP0-02/20180531T135920/ethVarList.info
VehSts-Veh_Spd	0	E_VT_float
VehSts-Veh_dphiYawRate	4	E_VT_float
VehSts-Veh_phiStrngWhlAg	8	E_VT_float
VehSts-Veh_flgStrngWhlAgDir	12	E_VT_uint8
VehSts-Veh_stActGear	13	E_VT_uint8
VehSts-pad0#0	14	E_VT_uint8
VehSts-pad0#1	15	E_VT_uint8
GPS-Longitude#0	16	E_VT_uint8
GPS-Longitude#1	17	E_VT_uint8
GPS-Longitude#2	18	E_VT_uint8
jiayou@webdev:~/adp/PandoraSDK/package$ tail /adas_data/PP0-02/20180531T135920/ethVarList.info
MeasList-PSD_lGapFrnt_mp	126800	E_VT_double
MeasList-PSD_lGapRear_mp	126808	E_VT_double
MeasList-PSD_lPrkSlotLngth_mp	126816	E_VT_double
MeasList-PSD_lPrkSlotWidthFrnt_mp	126824	E_VT_double
MeasList-PSD_lPrkSlotWidthRear_mp	126832	E_VT_double
MeasList-PSD_lPrkSlotWidth_mp	126840	E_VT_double
MeasList-PSD_locVehPosX_mp	126848	E_VT_double
MeasList-PSD_locVehPosY_mp	126856	E_VT_double
MeasList-PSD_phiDeltaYaw_mp	126864	E_VT_double
MeasList-PSD_stStatus_mp	126872	E_VT_double
'''
