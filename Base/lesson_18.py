# Выполнение команд в консольной строке
import subprocess
import io
print('-------------------------------')
sp1 = subprocess.Popen(['DATE'], stdout=subprocess.PIPE, shell=True)
print(sp1)
out1 = io.TextIOWrapper(sp1.stdout, encoding='cp866')
s1 = ' '
while s1:
    s1 = out1.readline()
    print(s1)

# print('-------------------------------')
# sp = subprocess.Popen(['dir'], stdout=subprocess.PIPE, shell=True)
# print(sp)
# out = io.TextIOWrapper(sp.stdout, encoding='cp866')
# s = ' '
# while s:
#     s = out.readline()
#     print(s)
