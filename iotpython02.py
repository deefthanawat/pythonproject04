#Function 2 : Have Parameters/No Return จะ call function ต้องส่ง 'ข้อมูล(Argument)'
#parameter คือ ตัวแปรประเภทหนึ่ง ขอบเขตการใช้งาน parameter
#จะใช้ได้เฉพาะใน function นั้นๆ เท่านั้น 

def funcA( x , y ) :
    print('Hi....')
    z = x + y
    print(f'{x} + {y} = {z}')
    #ไม่มีคำสั่ง return

def funcB( x ) :
    print(f"X is {x} 555...")

funcA(10, 20) #Argument
funcA(5, 6)
funcB( 'SAU IoT' )