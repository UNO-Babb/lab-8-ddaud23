#ProcessData.py
#Name:
#Date:
#Assignment:

import random

def main():

  #Open the files we will be using

  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')


  #Process each line of the input file and output to the CSV file
  #line = inFile.readline()
  for line in inFile:
    data = line.split()
    first = data[0]
    last = data[1]
    school_year = data[3]
    major = data[4]
    idNum = data[3]

    school_year_str = makeSchoolYear(school_year)
    major_abbr = makeMajor(major)

    output = last + "," + first + "," + school_year_str + "," + major_abbr + "\n"
    outFile. write(output)
    print(school_year_str, major_abbr)

  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

def makeSchoolYear(year):
  return year.capatalize()

def makeMajor(major):
  return major[3:].capatalize()
  
if __name__ == '__main__':
  main()
