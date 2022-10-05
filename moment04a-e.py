'''
b = int(input('Vad är basen?'))
h = int(input('Vad är höjden?'))
area = b*h
volym = 0
print("Arean är {0}".format(area))
print("Höjden | Volym")
while true:
    for i in range(1, 10):
        volym = area * i
        print(f"{i:<7.0f}| {volym:2.0f}")
'''
listB = []
listS= []
listR = []
def areaskap(btest, htest):
    global area
    area = b * h
#latest = 0
while True:
    b = int(input('Vad är basen?'))
    h = int(input('Vad är höjden?'))
    listB.append(b)
    listS.append(h)
    areaskap(b, h)
    #area = listB[latest] * listS[latest]
    volym = 0
    print("Arean är {0}".format(area))
    while True:
        try:
            r = int(input('Hur många höjder ska visas?'))
            if r > 10:
                r = 10
            elif r < 1:
                r = 1
            listR.append(r)
            break
        except:
            print('That failed. Please try again.')
    print("Höjden | Volym")
    for i in range(1, r+1):
        volym = area * i
        print(f"{i:<7.0f}| {volym:2.0f}")
    #for i in range(1, listR[latest]+1)
        #volym = area * i
    #latest =+ 1
    if input('Vill du avsluta? Y/N') == 'Y':
        break
