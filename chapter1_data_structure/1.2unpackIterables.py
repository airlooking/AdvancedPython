# --------------------------------------------------------------------
# example1
# --------------------------------------------------------------------
record1 = ("Dave","dave@example.com", '773-555-1212','847-555-1211')
name, email, *phone_numbers = record1
print(name, phone_numbers)
# >> Dave ['773-555-1212', '847-555-1211']


# --------------------------------------------------------------------
# example2
# --------------------------------------------------------------------
record2 = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

def do_foo(x,y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in record2:
    if tag =='foo':
        do_foo(*args)
    if tag =='bar':
        do_bar(*args)

# --------------------------------------------------------------------
# example3
# --------------------------------------------------------------------
record3 = ('ACME', 50, 123.45, (4, 18, 2020))
name, *_, (*_, year) = record3
print(name, year)