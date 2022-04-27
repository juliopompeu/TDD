from teste import soma

print(soma(5, 6))
print(soma(5, 5))
print(soma(5, 4))

try:
    print(soma('5', 3))
except AssertionError as e:
    print(f'Conta invalida : {e}')
