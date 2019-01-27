import sys

filename = 'input_EC.txt'
# opening the file
fp = open(filename)

# initializing nest_cnt varaiable to 0
nest_cnt = 0
# iterating through each line in file
for each_line in fp:
    each_line = each_line.strip()
    # checking if line starts with '{'
    if each_line.startswith('{'):
        nest_cnt += 1
        print(nest_cnt, each_line)

    # checking if line starts with '}'
    elif each_line.startswith('}'):
        print(nest_cnt, each_line)
        nest_cnt -= 1

    else:
        print(nest_cnt, each_line)

fp.close()
