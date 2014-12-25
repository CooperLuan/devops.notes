from celery import group, chain, chord
from tasks import add, mul, xsum

result = add.delay(2, 2).get()
print(result)

result = add.apply_async((2, 2)).get()
print(result)

result = add.s(2, 2).delay().get()
print(result)

result = add.s(2).delay(12).get()
print(result)

result = group(add.s(i, i) for i in range(10, 20))().get()
print(result)

result = chain(add.s(2, 2) | mul.s((4)))().get()
print(result)

result = chord((mul.s(i, i) for i in range(10)), xsum.s())().get()
print(result)

result = (group(mul.s(i, i) for i in range(10)) | xsum.s())().get()
print(result)
