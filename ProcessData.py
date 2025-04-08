#ProcessData.py
#Name:
#Date:
#Assignment:

import random

def main():

  # Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  # Process each line of the input file and output to the CSV file
  for line in inFile:
    data = line.strip().split()

    # Skip lines that don't have enough data
    if len(data) < 7:
      print("Skipping invalid line:", line.strip())
      continue

    
    first = data[0]        
    last = data[1]         
    studentID = data[3]  
    year = data[5]        
    major = data[6]        

    # Generate UserID and Major-Year
    user_id = makeID(first, last, studentID)
    major_year = makeMajorYear(major, year)

    # Write the formatted output line
    output = last + "," + first + "," + user_id + "," + major_year + "\n"
    outFile.write(output)
    print(output.strip())

  # Close files to save and prevent corruption
  inFile.close()
  outFile.close()

def makeID(first, last, num):
  
  if len(last) < 5:
    last = last + "xxxxx"
  last = last[0:5]

  # Use first initial + last name (5 chars) + last 3 digits of student ID
  last3 = num[-3:]
  id = first[0].lower() + last.lower() + last3
  return id

def makeMajorYear(major, year):
  first3 = major[0:3].upper()
  year = year.upper()
  
  yearAb = "GR"
  if year == "FRESHMAN":
    yearAb = "FR"
  elif year == "SOPHOMORE":
    yearAb = "SO"
  elif year == "JUNIOR":
    yearAb = "JR"
  elif year == "SENIOR":
    yearAb = "SR"

  majorYear = first3 + "-" + yearAb
  return majorYear

if __name__ == '__main__':
  main()

