try:
    open('test-files/test1.txt', 'r')

except FileNotFoundError:
    print('Die Datei wurde nicht gefunden.')

else:
    with open('test-files/test1.txt', 'r') as file:
        filedata = file.read()

    print(filedata)

print('Ende')