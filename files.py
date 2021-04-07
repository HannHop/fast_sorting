import random
# Part responsible for making str files
# f = open("words.txt", "r")  # https://www.wordgamedictionary.com/english-word-list/download/english.txt
# big_list = f.readlines()
# big_list = [word[:-1] for word in big_list]  # remove '\n' from each line
# f.close()
#
# arr_rand_32k_str = random.choices(big_list, k=32000)
# arr_rand_64k_str = random.choices(big_list, k=64000)
# arr_rand_128k_str= random.choices(big_list, k=128000)
# arr_rand_512k_str = random.choices(big_list, k=512000)
# arr_rand_1024k_str = random.choices(big_list, k=1024000)
#
# with open("32k_str.txt", 'w') as f:
#     for word in arr_rand_32k_str:
#         f.write('%s\n' % word)
#
# with open("64k_str.txt", 'w') as f:
#     for word in arr_rand_64k_str:
#         f.write('%s\n' % word)
#
# with open("128k_str.txt", 'w') as f:
#     for word in arr_rand_128k_str:
#         f.write('%s\n' % word)
#
# with open("1024k_str.txt", 'w') as f:
#     for word in arr_rand_1024k_str:
#         f.write('%s\n' % word)
#
# with open("512k_str.txt", 'w') as f:
#     for word in arr_rand_512k_str:
#         f.write('%s\n' % word)

# opening files with strings
f = open("32k_str.txt", "r")
arr_rand_32k_str = f.readlines()
arr_rand_32k_str = [word[:-1] for word in arr_rand_32k_str]  # remove '\n' from each line
f.close()

f = open("64k_str.txt", "r")
arr_rand_64k_str = f.readlines()
arr_rand_64k_str = [word[:-1] for word in arr_rand_64k_str]  # remove '\n' from each line
f.close()

f = open("128k_str.txt", "r")
arr_rand_128k_str = f.readlines()
arr_rand_128k_str = [word[:-1] for word in arr_rand_128k_str]  # remove '\n' from each line
f.close()

f = open("512k_str.txt", "r")
arr_rand_512k_str = f.readlines()
arr_rand_512k_str = [word[:-1] for word in arr_rand_512k_str]  # remove '\n' from each line
f.close()

f = open("1024k_str.txt", "r")
arr_rand_1024k_str = f.readlines()
arr_rand_1024k_str = [word[:-1] for word in arr_rand_1024k_str]  # remove '\n' from each line
f.close()

# block of code responsible for randomizing data that is then put into file,
# so that later I can use the same datasets
# for each sorting function:
# rand_4096k_int = random.choices(range(1, 5000000), k=4096000)
# rand_2048k_int = random.choices(range(1, 5000000), k=2048000)
# rand_1024k_int = random.choices(range(1, 5000000), k=1024000)
# rand_512k_int = random.choices(range(1, 5000000), k=512000)
# rand_128k_int = random.choices(range(1, 5000000), k=128000)

# with open('4096k_int.txt', 'w') as f:
#     for number in rand_4096k_int:
#         f.write('%s\n' % number)
#
# with open('2048k_int.txt', 'w') as f:
#     for number in rand_2048k_int:
#         f.write('%s\n' % number)
#
# with open('1024k_int.txt', 'w') as f:
#     for number in rand_1024k_int:
#         f.write('%s\n' % number)
#
# with open('512k_int.txt', 'w') as f:
#     for number in rand_512k_int:
#         f.write('%s\n' % number)
#
# with open('128k_int.txt', 'w') as f:
#     for number in rand_128k_int:
#         f.write('%s\n' % number)

# Part for opening already existing files with ints
f = open("128k_int.txt", "r")
file = f.readlines()
arr_rand_128k_int = [int(word[:-1]) for word in file]  # remove '\n' from each line
f.close()

f = open("512k_int.txt", "r")
file = f.readlines()
arr_rand_512k_int = [int(word[:-1]) for word in file]  # remove '\n' from each line
f.close()

f = open("1024k_int.txt", "r")
file = f.readlines()
arr_rand_1024k_int = [int(word[:-1]) for word in file]  # remove '\n' from each line
f.close()

f = open("2048k_int.txt", "r")
file = f.readlines()
arr_rand_2048k_int = [int(word[:-1]) for word in file]  # remove '\n' from each line
f.close()

f = open("4096k_int.txt", "r")
file = f.readlines()
arr_rand_4096k_int = [int(word[:-1]) for word in file]  # remove '\n' from each line
f.close()

