from tabulate import tabulate

itemList = ['в', 'п', 'б', 'а', 'и', 'н', 'т', 'о', 'ф', 'д', 'к', 'р']
itemSize = [3, 2, 2, 2, 1, 1, 3, 1, 1, 1, 2, 2] # itemsSpace
itemsPoint = [25, 15, 15, 20, 5, 15, 20, 25, 15, 10, 20, 20]
itemsDict = dict(zip(itemList, itemSize))
totalSpace = 9
Survival_Points = 10


def get_table(itemsList=itemList, itemsSpace=itemSize, itemsPoint=itemsPoint,totalSpace=totalSpace,
             Survival_Points=Survival_Points):
    """функция, которая находит максимально возможное значение и комбинацию с использованием динамического программирования"""
    memoTable = []
    memoCombination = []
    numberOfItems = len(itemsSpace)

    for itemindex in range(numberOfItems + 1):
        memoTable.append([0] * (totalSpace + 1))
        memoCombination.append([[]] * (totalSpace + 1))

    for itemindex in range(numberOfItems + 1):
        for space in range(totalSpace + 1):
            if itemindex == 0 or space == 0:
                memoTable[itemindex][space] = Survival_Points
                memoCombination[itemindex][space] = []
            else:
                if itemsSpace[itemindex - 1] <= space:
                    memoTable[itemindex][space] = max(
                        itemsPoint[itemindex - 1] + memoTable[itemindex - 1][space - itemsSpace[itemindex - 1]],
                        memoTable[itemindex - 1][space])
                    if max(itemsPoint[itemindex - 1] + memoTable[itemindex - 1][space - itemsSpace[itemindex - 1]],
                           memoTable[itemindex - 1][space]) == itemsPoint[itemindex - 1] + memoTable[itemindex - 1][
                        space - itemsSpace[itemindex - 1]]:
                        memoCombination[itemindex][space] = memoCombination[itemindex - 1][
                                                                space - itemsSpace[itemindex - 1]] + [
                                                                itemsList[itemindex - 1]]
                    else:
                        memoCombination[itemindex][space] = memoCombination[itemindex - 1][space]

                else:
                    memoTable[itemindex][space] = memoTable[itemindex - 1][space]
                    memoCombination[itemindex][space] = memoCombination[itemindex - 1][space]
    return memoTable, memoCombination, memoTable[numberOfItems][totalSpace],  memoCombination[numberOfItems][totalSpace]

maxPoint = get_table()[2]
maxCombo = get_table()[3]
finalPoint = maxPoint-(sum(itemsPoint)-maxPoint)

def createArray(gridColumn, maxPoint=maxPoint, maxCombo=maxCombo, itemsDict=itemsDict, finalPoint=finalPoint):
    'функция, которая возвращает ответ в виде строки в виде 2d-массива и конечного результата'
    if finalPoint >= 0:
        solutionList = []
        for key in maxCombo:
            for i in range(itemsDict[key]):
                solutionList.append(f'[{key}] ')
        solution = ''
        for a in solutionList:
            if (len(solution.replace('\n', '')) / 4) % gridColumn == 0:
                solution += '\n'
            solution += a
        solution += f'\nИтоговые очки выживания: {finalPoint}'
        return solution
    else:
        return 'решения не существует, напоминание, вычитаемое из максимального количества баллов, является отрицательным'

# 1. Решение для варианта 3, ячейки 2Х4 и заражения
print(f'1. Решение для варианта 10, ячейки 3Х3 {createArray(3)}')


# 2. Допзадание,возможные комбинации с положительными результатами
memoTable = get_table()[0]
memoCombination = get_table()[1]

print('\n2. возможные комбинации с положительными результатами')
for i in range(len(itemSize)+1):
    for j in range(totalSpace+1):
        if (memoTable[i][j]-(sum(itemsPoint)-memoTable[i][j])) > 0:
            print(memoCombination[i][j])

# 3. Допзадание,  ячейки7
optimized = get_table(totalSpace=7)
maxPoint = optimized[2]
maxCombo = optimized[3]
finalPoint = maxPoint-(sum(itemsPoint)-maxPoint)
print(f'\n3. Решение для ячейки 7 {createArray(4, maxPoint=maxPoint, maxCombo=maxCombo, finalPoint=finalPoint)}')