def canUnlockAll(boxes):
    key = []
    listKey = [0]
    skippedKey = []
    for i in range(len(boxes)):
        if i == 0:
            for k in boxes[i]:

                listKey.append(k)

        if i in listKey:
            # key.append(boxes[i])

            for k in boxes[i]:

                listKey.append(k)

        if i not in listKey:
            skippedKey.append(i)

    for i in skippedKey:
        if i in listKey:
            # key.append(boxes[i])

            for k in boxes[i]:

                listKey.append(k)

    value = True
    for i in range(len(boxes)):
        if i not in listKey:
            value = False

    # print(f'skipped key: {skippedKey}')

    # print(listKey)

    return value
