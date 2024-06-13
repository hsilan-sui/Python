noodles={'牛肉麵': 80,'陽春麵': 75,'肉骨茶麵': 115,'榨菜肉絲麵': 65,'乾麵': 45,}
if (key:=input('請輸入麵名(key) =')) in noodles:
    print(f'{key},價格是{noodles[key]}元')
else:
    (value:=input('請輸入定價價格(value):'))
    noodles[key]=value
    print(f'已經新增麵名以及價格在noodles上',noodles)