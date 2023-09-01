import Reader
import tensorMaker as Te
#入力部分--------------------------------
cFile= Reader.handler.opener()
cFile = Reader.handler.intize(cFile)
MaxSize = cFile[0]
part1 = cFile[1]
part2= cFile[2]
part3 = cFile[3]
part4 = cFile[4]
part5 = cFile[5]
#入力部分-------------------------------   下の方にも入力部分あり↓↓
plist = []
Max_instance = Te.Tensor.Make(MaxSize)                          #3次元テンソルの作成

locationx = [0]*1                                     #開始点のx座標
locationy = [0]*1                                     #開始点のy座標
locationz = [0]*1                                     #開始点のz座標
location = [[0],[0],[0]]                              #開始点の座標
location_count =len(location[0])                                     #開始点の数
beginpointx = [] 
beginpointy = [] 
beginpointz = [] 

def location_decide(part ,name,plist):                             #どの開始点に部品を置くかを決定する
    which_location = 0
    for i in range(location_count):
        which_location = i
        OK = False
        for t in range(5):
            judge_go =rota(t,part,locationx[i],locationy[i],locationz[i])
            if judge_go[0] ==True:
                OK = True
                break
        if OK == True:
            break

    if OK == True:
        kiridashi(judge_go[1],locationx[i],locationy[i],locationz[i],which_location,name,plist)   
  
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
    locationx.append(x)          #奥左端
    location[0].append(x)
    locationy.append(y +part1[1])
    location[1].append(y)
    locationz.append(z) 
    location[2].append(z)

    locationx.append(x)          #上左端
    locationy.append(y)
    locationz.append(z +part1[2])  

    locationx.append(x +part1[0])        #手前右
    locationy.append(y)
    locationz.append(z) 

    beginpointx.append(x)
    beginpointy.append(y)
    beginpointz.append(z)

    del locationx[whichlocation]         #手前左を使ったので消去
    del locationy[whichlocation]         #部品の配置開始点の処理（新しくできた開始点を加えて、使用した開始点を消去）
    del locationz[whichlocation]   
    for ii in range(3):
        del(location[ii][whichlocation])   
   
 
    global location_count                     #これがないと上手く行かない（謎）
    location_count += 2                       #開始点の数を増やす（三つ増えて1つ減るので+2）
  

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



#入力部分ここから---------------------------------
location_decide(part1,1,plist)    #この部分を真似して必要な部品の数だけコードを書いて下さい
location_decide(part2,2,plist)
location_decide(part3,3,plist)
location_decide(part4,4,plist)
location_decide(part5,5,plist)
many = 5                  #必要な部品の数を入力
write2 = []
for ii in range(many):
    write = []
    write.append(beginpointx[ii])
    write.append(beginpointy[ii])
    write.append(beginpointz[ii])
    for jj in range(3):
        write.append(plist[ii][jj])
    write2.append(write)

Reader.handler.initializeCSV(MaxSize)
Reader.handler.writeCSV(write2)