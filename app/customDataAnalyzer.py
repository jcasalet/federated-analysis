import sys

def run(myFDA):
    try:
        tripleNegatives = list()
        tripleValues = list()
        nonTripleNegatives = list()
        for myIndex, myRow in myFDA.dataFile.iterrows():
            # if all fields != NA, then add to that list
            if (isTripleValue(myRow)):
                tripleValues.append(myIndex)
                # if triple negative, add to that list
                if(isTripleNegative(myRow)):
                    tripleNegatives.append(myIndex)
            else:
                nonTripleNegatives.append(myIndex)

        if myFDA.configFile.outputFile == "":
            fileObject = sys.stdout
        else:
            fileObject = open(myFDA.configFile.outputFile, mode='a')
        print("number of triple negatives = " + str(len(tripleNegatives)), file=fileObject)
        print("number of triple values = " + str(len(tripleValues)), file=fileObject)
        print("number of non-triple negatives = " + str(len(nonTripleNegatives)), file=fileObject)
        return True

    except:
        return False


def isTripleNegative(myRow):
    if myRow['ER'] == 'Negative' and myRow['PgR'] == 'Negative' and myRow['HER2'] == 0:
        return True
    else:
        return False

def isTripleValue(myRow):
    if myRow['ER'] != 'NA' and myRow['PgR'] != 'NA' and myRow['HER2'] != 'NA':
        return True
    else:
        return False