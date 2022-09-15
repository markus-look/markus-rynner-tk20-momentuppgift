
#moment02b
if(input('Vill du skriva in tiden i sekunder, eller vill du skriva in i timmar/minuter? Y/N:')=='Y'):
    s = int(input('Hur många sekunder?'))
    t1 = s
    m = int(s//60)
    h = int(m//60)
    m = m-(h*60)
    s = s-(m*60)-(h*3600)
    print('{0:02d}h{1:02d}m{2:02d}s'.format(h, m, s))
else:
    h = int(input('Hur många timmar?'))
    m = int(input('Hur många minuter?'))
    s = int(input('Hur många sekunder?'))

    s = ((h*3600) + (m*60) + s)
    print('{0} sekunder!'.format(s))
    t1 = s
if(input('jämför?') == 'Y'):
    t2 = int(input('tid i sekunder'))
    if t2 > t1:
        diff = t2 - t1
        print('Tid2 är {0} sekunder snabbare än tid1'.format(diff))
    else:
        diff = t1 - t2
        print('Tid1 är {0} sekunder snabbare än tid2'.format(diff))

