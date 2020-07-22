import re
# These are threee different read functions

# readline() - prints the first line if iterated can print the whole file
# readlines()- prints all the lines
# read() - can be given with an integer in the paramter
with open('test.txt', 'r') as f:
    f_content = f.read(20)
    # patter = re.compile(r'Anurag', re.I)
    # match = patter.match(f_content)
    # print(match)
    print(f_content)
print(f.closed)
