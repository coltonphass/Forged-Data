# Math import for calculations
import math

def main():
   # List of files to analyze
   forgedDataFiles = [
       'P02_DataFile_0.dat',
       'P02_DataFile_1.dat',
       'P02_DataFile_2.dat',
       'P02_DataFile_3.dat',
       'P02_DataFile_4.dat',
       'P02_DataFile_5.dat',
       'P02_DataFile_6.dat',
       'P02_DataFile_7.dat',
       'P02_DataFile_8.dat',
       'P02_DataFile_9.dat'
   ]
   # Store results for summary table at end
   summary_data = []

   # Process each file
   for fileName in forgedDataFiles:
       try:
           analysisResult = analyzeDataFile(fileName)
           frequencyTotals = analysisResult["frequencyTotals"]
           relativeFrequencies = analysisResult["relativeFrequencies"]
           benfordOffsets = analysisResult["benfordOffsets"]
           forgeryCoefficient = analysisResult["forgeryCoefficient"]
           totalCount = analysisResult["totalCount"]

       # Error Handling
       except FileNotFoundError:
           print(f"File {fileName} not found!")
           continue
           
       except:
           print(f"An error occurred with file {fileName}!")
           continue

       # Save for summary table
       summary_data.append((fileName, forgeryCoefficient))
       
       # Print analysis for this file
       print(f"{totalCount} integer elements were encountered and analyzed in:")       
       print(fileName)
       print()
       print("FREQUENCY TOTALS")
       print(", ".join(f"FREQ_{digit:02d} = {frequencyTotals[digit]:5d}" for digit in range(1, 10)))
       print("\nRELATIVE FREQUENCY TOTALS")
       print(", ".join(f"RELA_{digit:02d} = {relativeFrequencies[digit]:.3f}" for digit in range(1, 10)))
       print("\nBENFORD OFFSET VALUES")
       print(", ".join(f"BOFF_{digit:02d} = {benfordOffsets[digit]:.3f}" for digit in range(1, 10)))
       
       # Print file summary
       print("-" * 50)
       print("DATA FILE ANALYSIS SUMMARY")
       print("File Name: {}".format(fileName))
       print("Forgery Coefficient: {:.3f}".format(forgeryCoefficient))
       print("-" * 50)
       print()
   
   # Final table comparing all files
   print("\nFINAL SUMMARY TABLE")
   print("FILE NAME           | FORGERY COEFFICIENT")
   print("-" * 40)
   for fileName, coefficient in summary_data:
       print(f"{fileName:<18} | {coefficient:.3f}")

def calculateBenfordProbability(digit):
   # Takes a digit 1-9 and returns its expected frequency according to Benford's Law
   return math.log10(digit + 1) - math.log10(digit)

def analyzeDataFile(filePath):    
   # Arrays to store our analysis results
   frequencyTotals = [0] * 10       # Actual count of each leading digit
   benfordOffsets = [0.0] * 10      # How far each digit deviates from Benford's Law
   relativeFrequencies = [0.0] * 10 # Observed frequency of each digit
 
   # Count leading digits from file and make sure its just digits
   file = open(filePath, 'r')
   for line in file:
       try:
           num = int(line.strip())
           firstDigit = int(str(num)[0])
           frequencyTotals[firstDigit] += 1
       except ValueError:
           print(f"WARNING: Invalid data found in {filePath}")
           continue
   file.close()
   totalCount = sum(frequencyTotals)
  
   # Calculate metrics for digits 1-9
   for digit in range(1, 10):
       benfordProbability = calculateBenfordProbability(digit)
       relativeFrequencies[digit] = frequencyTotals[digit] / totalCount
       benfordOffsets[digit] = abs(relativeFrequencies[digit] - benfordProbability)
 
   # Total deviation from Benford's Law (higher = more suspicious)
   forgeryCoefficient = sum(benfordOffsets)
   return {
       "frequencyTotals": frequencyTotals,
       "relativeFrequencies": relativeFrequencies,
       "benfordOffsets": benfordOffsets,
       "forgeryCoefficient": forgeryCoefficient,
       "totalCount": totalCount
   }

# Call main function
main()