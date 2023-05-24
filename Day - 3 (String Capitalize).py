
def solve(s):
    string = s.split(" ")
    print(string)
    string_list = []
    for i in string:
        string_list.append(i.capitalize())
    print(string_list)
    return (" ".join(string_list))
    

if __name__ == '__main__':

    s = input()

    result = solve(s)

    print(result)