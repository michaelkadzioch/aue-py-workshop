try:
    file = open('test-files/test1.txt', 'r')


except FileNotFoundError:
    print('Die Datei wurde nicht gefunden.')

else:
    filedata = file.read()
    print(filedata)
    file.close()