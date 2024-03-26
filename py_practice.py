def foo(element: list[str]) -> list[str]:
    return [elm.upper() for elm in element]
    
l1: list[str]= foo(['rishabh', 'verma', 'ritik'])
l2: list[str]= foo(['1', '2', '3'])

print(l1)
print(l2)