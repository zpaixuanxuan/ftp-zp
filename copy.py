import os

size=os.path.getsize('clock_process.py')
pid=os.fork()
if pid<0:
    print("不想动")
#子进程拷贝前半部分
elif pid==0:
    n=size//2
    fw=open('child','w')
    with open('clock_process.py','r') as f:
        while True:
            if n<64:
                data=f.read(n)
                fw.write(data)
                break
            data=f.read(64)
            fw.write(data)
            n-=64
    fw.close()
    
#父进程拷贝后半部分
else:
    fw=open('parent','w')
    with open('clock_process.py') as f:
        f.seek(size//2,0)
        while True:
            data=f.read(64)
            if not data:
                break
            fw.write(data)
        fw.close()