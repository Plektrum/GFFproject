#!/usr/bin/python2.7
# encoding: utf-8

__author__ = 'Plektrum'
__version__ = '1.0'
__title__ = 'GffReader'

import os
import sys

def read_file():
    data=[]
    section_end=0
    with open('data/Conus_on_aplysia.gff','r') as fh:  #.gff file reading
        for line in fh.readlines():
            if line.startswith('#'):
                section_end+=1
                if section_end < 20:
                    continue
                else:
                    break
            line=line.strip().split('\t')
            for i in line:
                f= open(r'ouput.txt', "a") #adding used data into .txt file 
                f.write(i+'\t')
                f.close()
            length= int(line[4])-int(line[3])
            data = {'Seqname': line[0],'Source': line[1],'Score': line[5], 'Type': line[ 2 ].lower(), 'PartofGene_start': line[ 3 ] , 'PartofGene_end': line[ 4 ], 'additionalInfo': line[ 8 ]} #creating dictionary
            print("Information about part of the gene: ")
            print("-----------------------------------------")
            print("Source: "+ data['Source'])
            print("Sequence name: "+data['Seqname'])
            print("Type/method: "+ data['Type'])
            print("Start: "+data['PartofGene_start'])
            print("End: "+data['PartofGene_end'])
            print("Length: " + str(length))
            print("Score: "+data['Score'])
            print("Additional Information & Comments: "+data['additionalInfo'])
            print
read_file()

def show_information():
    print("About Program: ")
    print("Title:  " '%s' % __title__)
    print ("Autor: "'%s' % __author__)
    print ("Version: "'%s' % __version__)
    print
    print \
	'''%s :: Information about data:
    -Source:    The program that generated this feature.
    -Sequence name:  This is the ID of the sequence that is used to establish the coordinate system of the annotation.
    -Type/method:     The annotation method. This field describes the type of the annotation, such as "CDS". Together the method and source describe the annotation type.
    -Start:    The starting position of the feature in the sequence.
    -End:    The ending position of the feature (inclusive).
    -Length:       Length of the feature in the sequence.
    -Score:   For annotations that are associated with a numeric score (for example, a sequence similarity), this field describes the score.
    -Additional Information & Comments:    GFF provides a simple way of generating annotation hierarchies ("is composed of" relationships) by providing a group field.
    The group field contains the class and ID of an annotation which is the logical parent of the current one.
    The group field is also used to store information about the target of sequence similarity hits, and miscellaneous notes.'''  % __title__
    sys.exit(0)
show_information()


