
from pymongo import MongoClient
import pandas as pd
import numpy as np
import scipy.stats as stats
import seaborn as sns
import pickle


def writeHistogramsToFile(histogram, filename):
    outfile = open(filename, 'wb')
    pickle.dump(histogram, outfile)
    outfile.close()
    return


def build_histogram_for_feature(feature, allData):
    print("formatting data for "+feature)
    featureList = {}
    for dbname in allData.keys():
        featureList[dbname] = []
        for i in range(len(allData[dbname]['uniqueNaturalProduct'].tolist())):
            if feature in allData[dbname]['uniqueNaturalProduct'][i].keys():
                featureList[dbname].append(allData[dbname]['uniqueNaturalProduct'][i][feature])
    print("done formatting data")
    # featureList is a dict dbname - list of values
    # need to create a dict: dbname : list of lists histogram
    try:
        allHistograms = {}
        for dbname in allData.keys():
            if dbname != "nubbe":
                #density = stats.gaussian_kde(featureList[dbname])
                allHistograms[dbname] = np.histogram(featureList[dbname], bins='auto', density=True)
                #allHistograms[dbname] = y, density(x), x
                print(allHistograms[dbname])
    except ValueError:
        print("Some ValueError happened")
    return allHistograms


def getDataFromMongo():
    print("Reading data from mongo")
    client = MongoClient("localhost:27017")
    db = client.COCONUTnovember7


    alldbData = {}

    # get all databases
    collection = db.sourceNaturalProduct
    alldb = pd.DataFrame(list(collection.distinct('source')))

    print("done reading data")

    for dbname in alldb[0]:
        collection = db.sourceNaturalProduct
        cdb = pd.DataFrame(list(collection.find({'source': dbname})))
        # del cdb['_id']
        # del cdb['_class']
        alldbData[dbname] = cdb

    print("done transforming data to pandas")

    return alldbData


def main():
    allData = getDataFromMongo()

    descriptors_list = ["npl_score", "alogp", "apol", "eccentricConnectivityIndexDescriptor",
                        "fmfDescriptor", "fragmentComplexityDescriptor", "fsp3", "hybridizationRatioDescriptor",
                        "kappaShapeIndex1", "manholdlogp", "molecular_weight", "petitjeanNumber",
                        "topoPSA", "tpsaEfficiency", "vertexAdjMagnitude", "weinerPathNumber",
                        "weinerPolarityNumber", "xlogp", "zagrebIndex"]

    for descriptor in descriptors_list:
        histogram = build_histogram_for_feature(descriptor, allData)
        writeHistogramsToFile(histogram, "archive/"+descriptor+"_hist_backup")


if __name__ == '__main__':
    main()

