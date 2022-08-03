# Tip calculator in Python
tip = None
stop = True

while exit:
    price = float(input('Enter the total cost (ex: 12.97): '))
    percent = float(input('Enter the % tip you\'d like to give: '))
    try:
        total = (price * (percent // 100)) + price
        print(f'With a {percent}% tip, The total comes to: {total}')
    except ValueError:
        print('Looks like you mistyped something')
        continue


