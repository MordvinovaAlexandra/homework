# 1 способ:
# with open('text1.txt',encoding = 'utf-8') as f1:
#     with open('text2.txt',encoding = 'utf-8') as f2:
#         f1_lines = f1.readlines()
#         f2_lines = f2.readlines()

#         for i in range(len(f1_lines)):
#             if f1_lines[i] != f2_lines[i]:
#                 print("Line " + str(i+1) + " doesn't match.")
#                 print("------------------------")
#                 print("File1: " + f1_lines[i])
#                 print("File2: " + f2_lines[i])

#         f1.close()
#         f2.close()

# 2 способ:

import difflib
with open('text1.txt',encoding = 'utf-8') as f1:
    f1_contents = f1.readlines()
with open('text2.txt',encoding = 'utf-8') as f2:
    f2_contents = f2.readlines()

diff = difflib.unified_diff(
    f1_contents, f2_contents, fromfile="text1.txt",
    tofile="text2.txt", lineterm='')

for line in diff:
    print(line)
