#Function 1 : No Parameter/No return ไม่มีไรในวงเล็บ เรียกกันไปกันมาไม่ได้ อย่าเรียกย้อนกลับ
def  funcA( ) :
    print('WOW')
    print('Woo')
    print('Wee')
    print('Wea')
    funcB( )
#ไม่มีคำสั่ง return เขียนโดดๆได้เลย

def funcB( ):
    print('Hi')

funcA( )
funcA( )
funcB( )
funcA( )