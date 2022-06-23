#!usr/bin/python3
"""
You have n number of locked boxes in front of you. 
Each box is numbered sequentially from 0 to n - 1 and 
each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """unlock all function"""
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
