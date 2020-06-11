import sys
import os
import pandas as pd
import numpy as np
sys.path.append(os.getcwd() + '/../model')
from tableDataFrame import TableDataFrame as Tdf


class TableModifier:
    def __init__(self):
        self.tdf = Tdf

    def modifyGroup(self, rows, groupnum):
        """
        Let the user set the group for a list of selected rows.
        returns the modified dataframe
        """
        self.df = Tdf.getTable(self)
        for row in rows:
            self.df.at[row, 'Fraction_Group'] = groupnum

        Tdf.setTable(self, self.df)

    def modifyFraction(self, rows, *argv):
        """
        Let the user set the fraction for a list of selected rows.
        enabled, when only parsing one number as fraction
        returns the modified dataframe
        """
        self.df = Tdf.getTable(self)
        if len(argv) == 1:
            for row in rows:
                self.df.at[row, 'Fraction'] = argv[0]
        elif len(argv) == 2:
            count = 0
            for row in rows:
                fracnum = argv[0] + count
                self.df.at[row, 'Fraction'] = fracnum
                if fracnum >= argv[1]:
                    count = 0
                else:
                    count += 1

        Tdf.setTable(self, self.df)

    def modifyLabelSample(self, labelnum, continuous):
        """
        Let the user change the multiplicity of the selected rows
        """
        self.df = Tdf.getTable(self)
        if continuous:
            ndf = []
            for row in self.df.index:
                for cl in range(labelnum):
                    label = cl+1
                    self.df.at[row, 'Label'] = label
                    dfrow = self.df.loc[[row]]
                    ndf.append(dfrow)

            ndf = pd.concat(ndf, ignore_index=True)
            prevsample = 0
            for row in ndf.index:
                if (row == 0):
                    samplenum = 1
                    ndf.at[row, 'Sample'] = samplenum
                elif(ndf.at[row, 'Fraction_Group'] != ndf.at[row-1, 'Fraction_Group']):
                    prevsample = ndf.at[row-1, 'Sample']
                    samplenum = ndf.at[row, 'Label'] + prevsample
                    ndf.at[row, 'Sample'] = samplenum
                else:
                    samplenum = ndf.at[row, 'Label'] + prevsample
                    ndf.at[row, 'Sample'] = samplenum

        else:
            ndf = []
            for row in self.df.index:
                for cl in range(labelnum):
                    label = cl+1
                    self.df.at[row, 'Label'] = label
                    dfrow = self.df.loc[[row]]
                    ndf.append(dfrow)

            ndf = pd.concat(ndf, ignore_index=True)

            for row in ndf.index:
                samplenum = ndf.at[row, 'Label']
                ndf.at[row, 'Sample'] = samplenum

        Tdf.setTable(self, ndf)

    def searchTable(self, dataframe, searchstring):
        """
        Let the user search in all cells of the dataframe.
        returns the a 2d list which corresponds to the cells, contains -1 if
        nothing is found the indeces of the searchstring if found. !!!NOT WORKING!!!
        """
        header = list(dataframe.columns.values)
        indexesfound = []
        for col in header:
            indexesfound.append(dataframe[col].str.find(searchstring))

        return indexesfound
