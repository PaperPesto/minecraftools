def mergeJson(sourceJson, key, targetJson):
    sourceJson[key] = targetJson
    return sourceJson

if __name__ == "__main__":

    testJson = {"nome": "Leonardo", "cognome": "Fantozzi"}

    print(mergeJson(testJson, "lavoro", {"nome":"aeffegroup"}))
    