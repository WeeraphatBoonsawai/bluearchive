import csv
import numpy
import pandas

def main():
    filename = 'age.csv'
    df = pandas.read_csv(
        filename,
        header=0,
        sep=',',
        lineterminator='\n')
    #print(df[(df['QUARTER'].str.contains('ไตรมาสที่ 4/2565'))])
    #sum = df[(df.QUARTER == 'ไตรมาสที่ 4/2565')]

    #print(sum)
    
    #country = df.iloc[1158:1266, 5]
    REG = df.iloc[792:800, 5]
    #AREA = df.iloc[1158:1266, 5]
    show = REG
    sum = REG.sum()
    max = REG.max()
    min = REG.min()
    mean = REG.mean()
    std = REG.std()
    var = REG.var()
    SD1 = (1*std)
    SD2 = (2*std)
    SD1MEAN1 = mean + SD1
    SD1MEAN2 = mean - SD1
    SD2MEAN1 = mean + SD2
    SD2MEAN2 = mean - SD2

    print('โชว์ข้อมูล',show)
    print('ผลรวม =',sum)
    print('ค่าสูงสุด =',max)  
    print('ค่าตํ่าสุด =',min)
    print('ค่าเฉลี่ย =',mean)
    print('ค่าส่วนเบี่ยงเบนมารตฐาน =',std)
    print('ค่าความแปรปรวน =',var)
    print('ค่าส่วนเบี่ยงเบนมารตฐาน 1 =',SD1)
    print('ค่าส่วนเบี่ยงเบนมารตฐาน 2 =',SD2)
    print('STD1 + =',SD1MEAN1)
    print('STD1 - =',SD1MEAN2)
    print('STD2 + =',SD2MEAN1)
    print('STD2 - =',SD2MEAN2)

    ##เขต
    SHOWT12 = df.iloc[792:800, 5]
    show = SHOWT12
    sum = SHOWT12.sum()
    print(show)

    #print(numpy.std(num_pop))

if __name__ == '__main__':
    main()
