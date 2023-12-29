
def open_or_senior(data):
    return ["Senior" if int(i[0]) >= 55 and int(i[1]) > 7 else "Open" for i in data]


print(open_or_senior(input))

