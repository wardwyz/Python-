import shutil

with open('E:/sample.txt','r+') as f1:
    f1.write('abcd\n1234')
    f1.flush()
    with open('E:/copy.txt','w+') as f2:
        shutil.copyfileobj(f1,f2)