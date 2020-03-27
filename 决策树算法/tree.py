from math import log
import operator

def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels

# -p*log(p)
def calcShannonEnt(dataSet):
    shannonEnt = 0
    labelCol = {}
    count = len(dataSet)
    for data in dataSet:
        label = data[-1]
        if label not in labelCol.keys():
            labelCol[label] = 0
        labelCol[label] += 1
    for label in labelCol:
        p = labelCol[label] / count
        shannonEnt -= p*log(p, 2)
    return shannonEnt


def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

def chooseBestFeatureToSplit(dataSet):
    # 属性个数（除了标签）
    numFeatures = len(dataSet[0]) - 1
    # 计算数据集的原始香农值
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0; bestFeature = -1
    for i in range(numFeatures):
        #所有数据的某一属性
        featList = [example[i] for example in dataSet]
        #去重，获得的是数据中所有的种类
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            #数据中第i个属性为 value的数据
            subDataSet = splitDataSet(dataSet, i, value)
            #计算数据在整体数据中所占的比例
            prob = len(subDataSet)/float(len(dataSet))
            # 计算香农值后乘上概率，然后累加
            newEntropy += prob * calcShannonEnt(subDataSet)

        infoGain = baseEntropy - newEntropy
        #如果有划分后的数据集香农值比原始数据集香农值要好，则返回对应的索引，否则返回-1
        if infoGain > bestInfoGain:
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys(): classCount[vote] = 0
        classCount[vote] += 1
    # 根据第二个属性排序（也就是数量）
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    # 返回数量最多的属性的键名
    return sortedClassCount[0][0]
def createTree(dataSet, labels):
    # 数据集中的所有分类值
    classList = [example[-1] for example in dataSet]
    # 所有数据都是同一个分类
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    # 数据集只有分类值，没有属性值
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel: {}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree

def classify(inputTree, featLabels, testVec):
    firstStr = inputTree.keys()[0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)
    for key in secondDict.keys():
        if testVec[featIndex] == key:
            if type(secondDict[key]).__name__ == 'dict':
                classLabel = classify(secondDict[key], featLabels, testVec)
            else: classLabel = secondDict[key]
    return classLabel

def storeTree(inputTree, filename):
    import pickle
    fw = open(filename, 'w'),
    pickle.dump(inputTree, fw)
    fw.close()

def grabTree(filename):
    import pickle
    fr = open(filename)
    return pickle.load(fr)
#
myDat, labels = createDataSet()
print(createTree(myDat, labels))
# print(myDat)
# print(calcShannonEnt(myDat))

