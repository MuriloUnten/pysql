def jsonFormat(result, cols):
    output = []
    for row in result:
        # rowObject = JsonObject()
        rowObject = {}
        for i in range(len(cols)):
            rowObject[cols[i]] = row[i]
        output.append(rowObject)

    return output
