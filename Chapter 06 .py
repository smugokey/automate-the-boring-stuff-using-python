table_data = [
    ["apples", "oranges", "cherries", "banana"],
    ["Alice", "Bob", "Carol", "David"],
    ["dogs", "cats", "moose", "goose"],
]


def tabulate(table):
    for i in range(len(table) + 1):
        output = ""
        for element in table:
            ma = len(max(element, key=len))
            output += element[i].rjust(ma + 1)
        print(output)


tabulate(table_data)
