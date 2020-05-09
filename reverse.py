def reverse(x):
    x = x.split()
    x.reverse()
    return ' '.join(x)
print (reverse(input('Напиши предложение: ')))
