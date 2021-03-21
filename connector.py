i = 0
while True:
    i = int(i)
    data = open('javascript.js','w')
    i = i+1
    i = str(i)
    data.write('document.getElementById('+'"speed"'+').value ='+i+'\n')
    data.write('document.getElementById('+'"weight"'+').value ='+i )
    data.close()
    print('succesfull ' + i )

