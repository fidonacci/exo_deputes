#! /usr/bin/env python3
# coding: utf-8

import argparse
import analysis.csv as c_an
import analysis.xml as x_an



def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--extension", help="""Type of file to analyse. Is it a CSV or an XML?""")
    parser.add_argument("-d", "--datafile", help="""CSV file containing pieces of information about the members of parliament""")
    return parser.parse_args()
 

if __name__ == "__main__":
    args = parse_arguments()
    datafile = args.datafile


    
    print(args)

    if args.extension == 'xml':
        try:
            x_an.launch_analysis(datafile)
        except:
            print("Problème de fichier man! : " )
    elif args.extension == 'csv':
        try:
            c_an.launch_analysis(datafile)
        except:
            print("Problème de fichier man! : ")
        
    

