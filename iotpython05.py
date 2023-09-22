def inputWidthLenght( ) :
    width = float( input('ความกว้างเท่ากับ '))
    lenght = float( input('ความยาวเท่ากับ '))
    return width,lenght

def inputBaseHigh( ) :
    base = float( input('ฐานเท่ากับ '))
    high = float( input('สูงเท่ากับ '))
    return base,high

def CalAndShowAreaSquare( width,lenght ) :
    area = width * lenght
    print(f'สี่เหลี่ยมมีความกว้าง {width} ความยาว {lenght} มีพื้นที่ทั้งหมดเท่ากับ {area}')

def CalAndShowAreaTriangle( base,high ) :
    area = base * high / 2
    print(f'สามเหลี่ยมมีฐาน {base} ความสูง {high} มีพื้นที่ทั้งหมดเท่ากับ {area}')

width, lenght = inputWidthLenght()
CalAndShowAreaSquare(width, lenght)
print('--------------------------------------')
base, high = inputBaseHigh()
CalAndShowAreaTriangle(base, high)