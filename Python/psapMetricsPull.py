import csv
import sys
from datetime import date

def main():
    with open('psapMetrics.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        serviceDictionary = {}
        resolverDictionary = {}
        advisorDeflectionDictionary = {}

        try:
            for row in csv_reader:
                if line_count == 0:
                    #Find Column Numbers for values
                    columnDict = setColumnNumber(row)
                    line_count += 1 
                    
                else:
                    #Count Services
                    countColumnValue(serviceDictionary, {row[columnDict['Service']]})

                    #Count Resolvers
                    countColumnValue(resolverDictionary, {row[columnDict['ResolvedBy']]})

                    #Count Deflection
                    countColumnValue(advisorDeflectionDictionary, {row[columnDict['AdvisorDeflection']]})

                    line_count += 1

        except UnicodeDecodeError:
            print(f'Oops: {row} caused an UnicodeDecodeError')
        except:
            print('Unexpected error: ', sys.exc_info()[0])

    print(f'Processed {line_count} lines.')

    #Write Dictionaries out to Graph CSV
    writeOutGraphCsv(serviceDictionary, resolverDictionary, advisorDeflectionDictionary)

def setColumnNumber(firstRow):
    columnCount = 0
    columnList = {}
    for x in firstRow:
        if x == 'ResolvedByIdentity':
            columnList.update({'ResolvedBy': columnCount})
        elif x == 'Technology (string)':
            columnList.update({'Service': columnCount})
        elif x == 'Advisor deflection recommendation (string)':
            columnList.update({'AdvisorDeflection': columnCount})
        columnCount += 1
    return columnList


def countColumnValue(inputDict, inputService):
    serviceValue = " ".join(inputService)
    if serviceValue in inputDict:
        inputDict[serviceValue] += 1
    else:
        inputDict[serviceValue] = 1

def writeOutGraphCsv(svcDict, resDict, defDict):
    csv_file = f'GraphOutput_{date.today()}.csv'

    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.writer(csvfile)
            
            #Write Service Dictionary
            writer.writerow(['Service','Count'])
            for key, value in svcDict.items():
                writer.writerow([key, value])

            #Write Resolver Dictionary
            writer.writerow(' ')
            writer.writerow(['Resolver', 'Count'])
            for key, value in resDict.items():
                writer.writerow([key, value])

            #Write Deflection Dictionary
            writer.writerow(' ')
            writer.writerow(['Deflection Recommendation','Count'])
            for key, value in defDict.items():
                writer.writerow([key, value])

    except IOError:
        print(f'Oops: {data} caused an I/O error')

if __name__ == "__main__":
    main()