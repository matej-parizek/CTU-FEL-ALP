vstup = list(map(int,input().split()))
def soucet(k):
     s=0
     for i in range(len(k)):
          s+=k[i]
     return s
def check_sym(a):
     stav = None
     if len(a) % 2 ==0:
          mid= len(a)//2
     else:
          mid=len(a)//2 + 1
     start=-1
     end=len(a)
     while start<mid and mid<end:
          start += 1
          end -= 1
          if a[start]==a[end]:
               stav=True
          else:
               stav=False
               break
     return stav
def sym (x):
     soucet_k =0
     soucet_prev = 0
     len_x = 0
     y = 0
     index = 0
     for i in range(len(x)):
          for j in range(len(x)-1,i,-1):
               if i<j:
                    if x[i]==x[j]:
                         if check_sym(x[i:j+1]):
                              y = (len(x[i:j+1]))
                              soucet_k = soucet(x[i:j + 1])
                              if y > len_x or y==len_x and soucet_k > soucet_prev:
                                   len_x = y
                                   y = 0
                                   index = i
                                   soucet_prev = soucet_k
                                   soucet_k = 0

     if len_x==0 and y==0:
          index=x.index(max(x))
          len_x = 1
     print(index, len_x,)
sym(vstup)
