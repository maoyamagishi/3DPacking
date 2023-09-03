import Reader
import tensorMaker as Te


cFile= Reader.handler.opener()
cFile = Reader.handler.intize(cFile)
MaxSize = cFile[0]

plist = []
Max_instance = Te.Tensor.Make(MaxSize)                          #3次元テンソルの作成
location = [[0],[0],[0]]                              #開始点の座標
beginpoints = [[],[],[]]
parts = []
for ii in range(len(cFile) -1):
    parts.append(cFile[ii +1])

def DecidingHandler(part ,name,plist):                             #どの開始点に部品を置くかを決定する
    which_location = 0
    for i in range(len(location[0])):
        which_location = i
        OK = False
        for t in range(5):
            judge_go =rota(t,part,location[0][i],location[1][i],location[2][i])
            if judge_go[0] ==True:
                OK = True
                break
        if OK == True:
            break

    if OK == True:
        kiridashi(judge_go[1],location[0][i],location[1][i],location[2][i],which_location,name,plist)   
  
    else:
        shippai(part)
        
 
       


def kiridashi(part1 ,x ,y ,z ,whichlocation,name,plist):                 #実際に切り出す
    s = part1[0]
    t = part1[1]
    u = part1[2]
    for l in range(s):
        for m in range(t):
            for n in range(u):
                Max_instance[x +l][y +m][z +n] =1
    plist.append([s,t,u])
    location[0].append(x)          #奥左端
    location[1].append(y +part1[1])
    location[2].append(z)

    location[0].append(x)          #上左端
    location[1].append(y)
    location[2].append(z +part1[2])  

    location[0].append(x +part1[0])        #手前右
    location[1].append(y)
    location[2].append(z) 

    beginpoints[0].append(x)
    beginpoints[1].append(y)
    beginpoints[2].append(z)
                                   
    #部品の配置開始点の処理（新しくできた開始点を加えて、使用した開始点を消去）
  
    for ii in range(3):     #手前左を使ったので消去
        del(location[ii][whichlocation])   
   
  

def check(part1rpy,x,y,z):             #部品が切り出せるか判定する
    interact = False
    if MaxSize[0] < x + part1rpy[0]:
        interact = True
    if MaxSize[1] < y + part1rpy[1]:
        interact = True
    if MaxSize[2] < z + part1rpy[2]:
        interact = True
    
    if interact == False:
        for l in range(part1rpy[0]-1):
            for m in range(part1rpy[1]-1):
                for n in range(part1rpy[2]-1):
                   if Max_instance[l +x][m +y][n +z] ==1:
                      interact = True

    if interact == True:
        return(False)
    else:
        return(True)





def rota(t ,part,x,y,z):              #部品を回転させる
    rota_part = part
    rota_desk = 0
    if t > 0:

        if t %2==1:
          rota_desk = part[2]
          rota_part[2] = rota_part[1]
          rota_part[1] = rota_desk
        else:
           rota_desk = part[1]
           rota_part[1] = rota_part[0]
           rota_part[0] = rota_desk 

    if check(rota_part,x,y,z) ==True:
        return True,rota_part
    else:
        return False,rota_part


def shippai(part):
    print(f'{part}は入りません')


for ii in range(len(parts)):
    DecidingHandler(parts[ii],ii ,plist)


write2 = []
for ii in range(len(parts)):
    write = []
    write.append(beginpoints[0][ii])
    write.append(beginpoints[1][ii])
    write.append(beginpoints[2][ii])
    for jj in range(3):
        write.append(plist[ii][jj])
    write2.append(write)

Reader.handler.initializeCSV(MaxSize)
Reader.handler.writeCSV(write2)