'''HOW TO USE
How to enter formulas:
*Use elements' abbreviations in all lowercase
*After every element, put a number, even if it's 1
*You can use parentheses (e.g. ca1(n1o3)2 for calcium nitrate)
*Put every formula in quotes
*Do not use spaces

How to use molar_mass:
*Enter print(molar_mass(formula)) at the bottom of the document

How to use percent_composition:
*Enter print(percent_composition(formula)) at the bottom of the document

How to use empirical_formula:
*Enter print(empirical_formula(masses)) at the bottom of the document
How to enter masses:
*Put every element or polyatomic ion in quotes immediately followed by its mass
*e.g. 'ca24.42(n1o3)75.58'

How to use redox:
*Enter print(redox(reactant1, reactantcharge1, reactant2, reactantcharge2, product1, productcharge1, product2, productcharge2))
'''
atwt={'h':1.01,'he':4,'li':6.94,'be':9.01,'b':10.81,'c':12.01,'n':14.01,'o':16,'f':19,'ne':20.18,'na':22.99,'mg':24.31,'al':26.98,'si':28.09,'p':30.97,'s':32.07,'cl':35.45,'ar':39.95,'k':39.1,'ca':40.08,'sc':44.96,'ti':47.9,'v':50.94, 'cr':52.00,'mn':54.94,'fe':55.85,'co':58.93,'ni':58.69,'cu':63.55,'zn':65.39,'se':78.96,'br':79.9,'kr':83.8,'sr':87.62,'ag':107.87,'sn':118.71,'i':126.9,'ba':137.33,'sm':150.36,'pb':207.2,'ra':226,'u':238}
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
def molar_mass(a):
    global atwt
    k=0
    a2=a.split(' ')
    print(a2)
    for i in a2:
        j=i.split('.')
        k+=atwt[j[0]]*int(j[1])
    return round(k,2)
def mm1(a,f=True):
    global atwt
    k=0
    if f:
        a2=p(a)
    else:
        a2=a
    if f:
        print(a2)
    for i in a2:
        k+=atwt[i[0]]*i[1]
    return round(k,2)
def empirical_formula(a):
    global atwt
    l,m,n,n1,n2,a5=0,-1,False,False,False,[]
    a2=[]
    if a[0]=='(':
        n1=True
    for i in a+'a':
        if n1:
            m+=1
            if i==')':
                m+=1
                a5.append(a[l+1:m-1])
                l=m
                m-=1
                n1=False
                n=True
                n2=True
            continue
        if i=='.':
            m+=1
            continue
        try:
            int(i)
            m+=1
            if not n:
                a2.append(a[l:m])
                l=m
                n=True
        except ValueError:
            m+=1
            if n:
                if n2:
                    a5.append(a[l:m])
                else:
                    a2.append(a[l:m])
                l=m
                n=False
                if i=='(':
                    n1=True
    print(a2+a5)
    a3=[]
    b3=[]
    for i in range(0,len(a2),2):
        a3.append(float(a2[i+1])/atwt[a2[i]])
        b3.append(a2[i])
    for i in range(0,len(a5),2):
        a3.append(float(a5[i+1])/mm1(a5[i]))
        b3.append(a5[i])
    a4,k=[],min(a3)
    for i in a3:
        a4.append(i/k)
    return a4
def percent_composition(a):
    global atwt
    k,k1='',0
    l,m,n=0,-1,False
    a2=p(a)
    print(a2)
    for i in a2:
        k1+=round(atwt[i[0]]*i[1],2)
    for i in a2:
        k+=i[0]+':'+str(round(atwt[i[0]]*i[1]/k1*100,2))+' '
    return k
def redox(a0,aa,b0,bb,c0,cc,d0,dd,t=False):
    def n(x):
        a=-1
        for i in x:
            if i[0]!='h' and i[0]!='o':
                if a!=-1:
                    raise ValueError("too many elements")
                a=i
        return a
    def m(x,f):
        return [f*i for i in x]
    def heq(x,aa,y,cc):
        a,c=p(x),p(y)
        a1,c1=n(a),n(c)
        if a1[0]!=c1[0]:
            if t:
                raise ValueError("Wrong order")
            return [1,rd(a0,aa,b0,bb,d0,dd,c0,cc,t=True)]
        d=gcd(a1[1],c1[1])
        def s1(l,h):
            for i in l:
                if i[0]==h:
                    return i[1]
            return 0
        a2=list(map(lambda x:x*c1[1]/d,[a1[1],s1(a,'h'),s1(a,'o'),aa]))
        c2=list(map(lambda x:x*a1[1]/d,[c1[1],s1(c,'h'),s1(c,'o'),cc]))
        d2=[c2[i]-a2[i] for i in range(1,4)]
        d2[0]-=2*d2[1]
        d2[2]=d2[0]-d2[2]
        return [0,d2+[c1[1]/d,a1[1]/d]]
    ax,bx=heq(a0,aa,c0,cc),heq(b0,bb,d0,dd)
    if ax[0]==1:
        return ax[1]
    a,b=ax[1],bx[1]
    d=gcd(abs(a[2]),abs(b[2]))
    a2,b2=m(a,abs(b[2]/d)),m(b,abs(a[2]/d))
    c1=[a2[i]+b2[i] for i in range(3)]
    if c1[2]!=0:
        raise ValueError('charges...')
    be,en='',''
    be+=str(int(a2[3]))+' '+a0+'('+str(aa)+')'+'+'+str(int(b2[3]))+' '+b0+'('+str(bb)+')'
    en+=str(int(a2[4]))+' '+c0+'('+str(cc)+')'+'+'+str(int(b2[4]))+' '+d0+'('+str(dd)+')'
    if c1[0]>0:
        be+='+'+str(int(c1[0]))+' h1(1)'
    elif c1[0]<0:
        be+='+'+str(int(-c1[0]))+' o1h1(-1)'
        c1[1]+=c1[0]
    if c1[1] > 0:
        be += '+' + str(int(c1[1])) + ' h2o1(0)'
    elif c1[1] < 0:
        en += '+' + str(-int(c1[1])) + ' h2o1(0)'
    return be+'-->'+en
def p(x):
    l,m,n,n1,n2=0,-1,False,False,0
    global atwt
    a2=[]
    for i in x+'a':
        try:
            int(i)
            m+=1
            if not n and not n1:
                a2.append(x[l:m])
                l=m
                n=True
        except ValueError:
            m+=1
            if n:
                a2.append(x[l:m])
                l=m
                n=False
            if not n1:
                if i=='(':
                    aa=l+x[l:].index(')')
                    n2=p(x[l+1:aa])
                    n3=mm1(n2,False)
                    atwt[x[l+1:aa]]=n3
                    n1=True
                    a2.append(x[l+1:aa])
            if n1 and i==')':
                n1=False
                n=True
                l=m+1
    a3=[]
    for i in range(0,len(a2),2):
        a3.append([a2[i],float(a2[i+1])])
    return a3
