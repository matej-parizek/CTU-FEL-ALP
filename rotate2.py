vst1= list(map(int,input().split()))
vst2 =list(map(int,input().split()))

class Rotate:
    def __init__(self,val1,val2):
        self.val1=val1
        self.val2=val2
    def otoceniminus(self,rotate):
        vm1=self.val1
        vm2=self.val2
        a=[]
        b=vm2[:]
        for i in range(1,len(vm1)):
            a.append(vm1[i])
        a.append(vm1[0])
        b[0], b[2] = a[0], a[2]
        if rotate==0:
            return a, b
        if rotate==1:
            return b,a
    def otoceniplus(self,rotate):
        a=[]
        vp1=self.val1
        vp2=self.val2
        b=vp2[:]
        a.append(vp1[len(vp1)-1])
        for i in range(len(vp1)):
            if i <len(vp1)-1:
                a.append(vp1[i])
        b[0],b[2]=a[0],a[2]
        if rotate == 0:
            return a, b
        if rotate == 1:
            return b, a
class TreeNode:
    def __init__(self, data):
        self.data=data
        self.children=[]
        self.parent=None
    def add_child(self,child):
        self.child = child
        child.parent = self
        self.children.append(child)
    def get_level(self):
        level = 0
        p = self.parent
        while p :
            p = p.parent
            level += 1
        return level
    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
def conrol(otoceni):
    if otoceni[0][0]==1 and otoceni[0][2]== 0 and otoceni[1].count(0)==1 and otoceni[0].count(1)==1:
        return True
    else:
        return False
skate=[]
ind=[]
def parent(tree,n,a,s):
    if n >1:
        if a:
            s.append(a)
        if tree.parent:
            s.append(tree.data)
        parent(tree.parent,n-1,"",s)
    return s

def zk(n,strom,rt):
    rotate1,rotate2,rotate3,rotate4= Rotate(rt[0],rt[1]),Rotate(rt[0],rt[1]),Rotate(rt[1],rt[0]),Rotate(rt[1],rt[0])
    otoceni1, otoceni2,otoceni3, otoceni4=rotate1.otoceniplus(0),rotate2.otoceniminus(0),rotate3.otoceniplus(1),rotate4. otoceniminus(1)
    a,b,c,d= TreeNode("(0,p)"),TreeNode("(0,m)"),TreeNode("(1,p)"),TreeNode("(1,m)")
    if n<7:
        if conrol(otoceni1):
            strom.add_child(a)
            skate.append(parent(strom, n +2, "(0,p)",[]))
            ind.append(len((parent(strom, n+2 , "(0,p)",[]))))
        if conrol(otoceni2):
            strom.add_child(b)
            skate.append(parent(strom, n +2, "(0,m)",[]))
            ind.append(len(parent(strom,n+2,"(0,m)",[])))
        if conrol(otoceni3):
            strom.add_child(c)
            skate.append(parent(strom, n +2, "(1,p)",[]))
            ind.append(len(parent(strom, n +2, "(1,p)",[])))
        if conrol(otoceni4):
            strom.add_child(d)
            skate.append(parent(strom, n +2, "(1,m)",[]))
            ind.append(len(parent(strom, n+2, "(1,m)",[])))

        for i in range(4):
            if i == 0:
                strom.add_child(a)
            if i == 1:
                strom.add_child(b)
            if i == 2:
                strom.add_child(c)
            if i == 3 :
                strom.add_child(d)
        zk(n + 1, d, otoceni4)
        zk(n + 1, c, otoceni3)
        zk(n + 1, b, otoceni2)
        zk(n + 1, a, otoceni1)


    return strom
rot1=(vst1,vst2)
tree=TreeNode(str(rot1))
zk(0,tree,rot1)
tisk=(skate[(ind.index(min(ind)))])[::-1]
for i in tisk:
    print(i,end="")