#Function 3 : No Parameter/Have Returns *** return มากกว่า 1 ค่าต้องมี "," เขียนปนกับอะไรซักอย่าง
def funcA( ) :
    print('AAA')
    print('BBB')
    return 'Woo Woo'

def funcB( ) :
    return 567, True, 10+20 #return มากกว่า 1 ค่า ให้สร้างตัวแปรมาเก็บ

#funcA( ) เขียนได้ แต่ไม่ทำกัน ไม่เขียนโดดๆ
print( funcA( ) )
x = funcA( ) # เก็บไว้ใน RAM

a, b, c = funcB( ) #***
print(f'{c} {b} {a}')