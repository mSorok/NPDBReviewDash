
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient("localhost:27017")
db=client.COCONUTnovember7

###################
#prepare data

#get all databases
collection = db.sourceNaturalProduct
alldb = pd.DataFrame(list(collection.distinct('source')))


nbDatabases = len(alldb)-1

alldbData = {}

for dbname in alldb[0]:
    collection = db.sourceNaturalProduct
    cdb = pd.DataFrame(list(collection.find({'source':dbname})))
    del cdb['_id']
    del cdb['_class']
    alldbData[dbname] = cdb



def create_db_df(dict_hist):
    dfObj = pd.DataFrame(columns=['dbname','x','y'])

    for dbname in dict_hist.keys():
        for i in range(len(dict_hist[dbname]) ):
            dfObj = dfObj.append({'dbname': dbname, 'x': dict_hist[dbname][1][i], 'y': dict_hist[dbname][0][i]}, ignore_index=True)
    # print(dfObj)
    return dfObj


alogp = {}
apol = {}
eccentricConnectivityIndexDescriptor = {}
fmfDescriptor = {}
fragmentComplexityDescriptor = {}
fsp3 = {}
hybridizationRatioDescriptor = {}
kappaShapeIndex1= {}
lipinskiRuleOf5Failures= {}
manholdlogp = {}
molecular_weight = {}
npl_score = {}
petitjeanNumber = {}
topoPSA = {}
tpsaEfficiency = {}
vertexAdjMagnitude = {}
weinerPathNumber = {}
weinerPolarityNumber = {}
xlogp = {}
zagrebIndex = {}

for dbname in alldbData.keys():
    print(dbname)
    alogp[dbname] = []
    apol[dbname] = []
    eccentricConnectivityIndexDescriptor[dbname] = []
    fmfDescriptor[dbname] = []
    fragmentComplexityDescriptor[dbname] = []
    fsp3[dbname] = []
    hybridizationRatioDescriptor[dbname] = []
    kappaShapeIndex1[dbname] = []
    lipinskiRuleOf5Failures[dbname] = []
    manholdlogp[dbname] = []
    molecular_weight[dbname] = []
    npl_score[dbname] = []
    petitjeanNumber[dbname] = []
    topoPSA[dbname] = []
    tpsaEfficiency[dbname] = []
    vertexAdjMagnitude[dbname] = []
    weinerPathNumber[dbname] = []
    weinerPolarityNumber[dbname] = []
    xlogp[dbname] = []
    zagrebIndex[dbname] = []
    for i in range(len(alldbData[dbname]['uniqueNaturalProduct'].tolist())):
        if "npl_score" in alldbData[dbname]['uniqueNaturalProduct'][i].keys():
            npl_score[dbname].append(alldbData[dbname]['uniqueNaturalProduct'][i]['npl_score'])
        if "alogp" in alldbData[dbname]['uniqueNaturalProduct'][i].keys():
            alogp[dbname].append(alldbData[dbname]['uniqueNaturalProduct'][i]['alogp'])
        if "apol" in alldbData[dbname]['uniqueNaturalProduct'][i].keys():
            apol[dbname].append(alldbData[dbname]['uniqueNaturalProduct'][i]['apol'])
        if "eccentricConnectivityIndexDescriptor" in alldbData[dbname]['uniqueNaturalProduct'][i].keys():
            eccentricConnectivityIndexDescriptor[dbname].append(
                alldbData[dbname]['uniqueNaturalProduct'][i]['eccentricConnectivityIndexDescriptor'])
        if "fmfDescriptor" in alldbData[dbname]['uniqueNaturalProduct'][i].keys():
            fmfDescriptor[dbname].append(alldbData[dbname]['uniqueNaturalProduct'][i]['fmfDescriptor'])
        if "fragmentComplexityDescriptor" in alldbData[dbname]['uniqueNaturalProduct'][i].keys():
            fragmentComplexityDescriptor[dbname].append(
                alldbData[dbname]['uniqueNaturalProduct'][i]['fragmentComplexityDescriptor'])
        if "fsp3" in alldbData[dbname]['uniqueNaturalProduct'][i].keys():
            fsp3[dbname].append(alldbData[dbname]['uniqueNaturalProduct'][i]['fsp3'])
        if "hybridizationRatioDescriptor" in alldbData[dbname]['uniqueNaturalProduct'][i].keys():
            hybridizationRatioDescriptor[dbname].append(
                alldbData[dbname]['uniqueNaturalProduct'][i]['hybridizationRatioDescriptor'])
        if "kappaShapeIndex1" in alldbData[dbname]['uniqueNaturalProduct'][i].keys():
            kappaShapeIndex1[dbname].append(alldbData[dbname]['uniqueNaturalProduct'][i]['kappaShapeIndex1'])
        if "lipinskiRuleOf5Failures" in alldbData[dbname]['uniqueNaturalProduct'][i].keys():
            lipinskiRuleOf5Failures[dbname].append(
                alldbData[dbname]['uniqueNaturalProduct'][i]['lipinskiRuleOf5Failures'])
        if "manholdlogp" in alldbData[dbname]['uniqueNaturalProduct'][i].keys():
            manholdlogp[dbname].append(alldbData[dbname]['uniqueNaturalProduct'][i]['manholdlogp'])
        if "molecular_weight" in alldbData[dbname]['uniqueNaturalProduct'][i].keys():
            molecular_weight[dbname].append(alldbData[dbname]['uniqueNaturalProduct'][i]['molecular_weight'])
        if "petitjeanNumber" in alldbData[dbname]['uniqueNaturalProduct'][i].keys():
            petitjeanNumber[dbname].append(alldbData[dbname]['uniqueNaturalProduct'][i]['petitjeanNumber'])
        if "topoPSA" in alldbData[dbname]['uniqueNaturalProduct'][i].keys():
            topoPSA[dbname].append(alldbData[dbname]['uniqueNaturalProduct'][i]['topoPSA'])
        if "tpsaEfficiency" in alldbData[dbname]['uniqueNaturalProduct'][i].keys():
            tpsaEfficiency[dbname].append(alldbData[dbname]['uniqueNaturalProduct'][i]['tpsaEfficiency'])
        if "vertexAdjMagnitude" in alldbData[dbname]['uniqueNaturalProduct'][i].keys():
            vertexAdjMagnitude[dbname].append(alldbData[dbname]['uniqueNaturalProduct'][i]['vertexAdjMagnitude'])
        if "weinerPathNumber" in alldbData[dbname]['uniqueNaturalProduct'][i].keys():
            weinerPathNumber[dbname].append(alldbData[dbname]['uniqueNaturalProduct'][i]['weinerPathNumber'])
        if "weinerPolarityNumber" in alldbData[dbname]['uniqueNaturalProduct'][i].keys():
            weinerPolarityNumber[dbname].append(alldbData[dbname]['uniqueNaturalProduct'][i]['weinerPolarityNumber'])
        if "xlogp" in alldbData[dbname]['uniqueNaturalProduct'][i].keys():
            xlogp[dbname].append(alldbData[dbname]['uniqueNaturalProduct'][i]['xlogp'])
        if "zagrebIndex" in alldbData[dbname]['uniqueNaturalProduct'][i].keys():
            zagrebIndex[dbname].append(alldbData[dbname]['uniqueNaturalProduct'][i]['zagrebIndex'])


# TODO save the data separately to load on the fly
