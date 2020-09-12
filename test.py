f = open('input.txt')
lines2 = f.readlines() # 1行毎にファイル終端まで全て読む(改行文字も含まれる)
f.close()
# lines2: リスト。要素は1行の文字列データ
anslist=[]
for line in lines2:
    a=line.split(':')
    if int(lines2[-1])%int(a[0])==0 and len(a)==2:
        anslist.append((int(a[0]),a[1]))
if len(anslist)!=0:
    anslist.sort()
    ans=''
    for i in range(len(anslist)):
        ans+=anslist[i][1][:-1]
    print(ans)
else:
    print(lines2[-1])
