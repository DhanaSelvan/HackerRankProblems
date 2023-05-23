s = input()
print("{}\n{}\n{}\n{}\n{}\n".format(
        any([i.isalnum() for i in s]),                 
        any([i.isalpha() for i in s]),
        any([i.isdigit() for i in s]),
        any([i.islower() for i in s]),
        any([i.isupper() for i in s])))