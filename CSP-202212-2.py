# CSP 202212-2 训练计划

def _input():
    return list(map(int,input().split(" ")))

class Prj:
    def __init__(self,time):
        self.time=time
        self._depend=None
        self._depended=list()
        
    def depend(self,prj):
        self._depend=prj
        
    def depended(self,prj):
        self._depended.append(prj)
    
    def before(self):
        if(self._depend==None):
            return 0
        else:
            return self._depend.before()+self._depend.time
    def after(self):
        _time=0
        for d in self._depended:
            _time = max(d.after()+d.time,_time)
        return _time

def create_projects(p:list,t:list):
    prjs=list()
    for i in range(len(p)):
        prj=Prj(t[i])
        if p[i]!=0:
            #print(prjs[p[i]-1])
            prj.depend(prjs[p[i]-1])
            prjs[p[i]-1].depended(prj)
        prjs.append(prj)
    return prjs

def earliest(prj):
    return 1+prj.before()

def latest(prj,n):
    return n+1-prj.time-prj.after()

def main():
    (n,m)=_input()
    p=_input()
    t=_input()
    prjs=create_projects(p,t)
    r1=list()
    r2=list()
    for prj in prjs:
        r1.append(earliest(prj))
        r2.append(latest(prj,n))
    print(*r1,sep=' ')
    if not(min(r2)<1):
        print(*r2,sep=' ')

main()