import argparse
from parser.ETH import ETH
from parser import util
import os
import numpy as np
from asammdf import MDF, Signal

def mdfsave(mdf, df, filename):
    t = 0.05 * df.index.values
    sigs=[]
    for v in df.columns:
	sigs += [Signal(df[v].values, t, name=v)]
    mdf.append(sigs)
    mdf.save(filename, overwrite=True, compression=1)
	

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Get useful input signal from Ethernet Data')
    parser.add_argument('-i', '--infile', help='Input file', required=True)
    parser.add_argument(
        '-o', '--outfile', help='Output file', required=False)
    parser.add_argument(
        '-c', '--config', help='Configuration file', required=False)
    parser.add_argument(
        '-s', '--signal', help='Signal to dump', required=False, action='append')
    parser.add_argument(
        '-v', '--variable', help='A file contains variable list', required=False)
    args = parser.parse_args()

#%% Mandantory Data File and Config File
    if args.config is None:
        config_file = os.path.join(os.path.dirname(args.infile), 'ethVarList.info')
    else:
        config_file = os.path.abspath(args.config)
		
    data_file = args.infile
    
#%% Initialize Data File
    eth = ETH(data_file=data_file, config_file=config_file)
    print eth

#%% Signal List

    varlist = []
    if args.variable is not None:
		varlist = util.varlist_from_file(args.variable)

    if args.signal is not None:
        varlist += args.signal

  # print varlist
    
#%% return pandas data frame
    
    df = eth.parse(varlist)

#%% Output
    if args.outfile is not None:
        f, extension = os.path.splitext(args.outfile)
        print "Write output to " + args.outfile
        
        if extension == '.csv':
            df.to_csv(args.outfile)

        elif extension == '.json':
            df.to_json(args.outfile)

	elif extension == '.mdf':
	    mdf = MDF(version='4.00')
	    mdfsave(mdf, df, args.outfile)

	elif extension == '.mf4':
	    mdf = MDF(version='4.10')
	    mdfsave(mdf, df, args.outfile)
		
        else:
            print "Not supported output file type."


#%% END
