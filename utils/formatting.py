def jsonFormat(result, cols):
    # class JsonObject:
    #     def __init__(self):
    #         pass

    output = []
    for row in result:
        # rowObject = JsonObject()
        rowObject = {}
        for i in range(len(cols)):
            rowObject[cols[i]] = row[i]
        output.append(rowObject)

    return output


def csvFormat(result, cols):
    pass
