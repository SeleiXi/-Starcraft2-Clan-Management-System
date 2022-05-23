import pymysql
import random
import time

# 自行链接SQL数据库
db = pymysql.connect(host='',
                     user='',
                     password='',
                     database ='')
cursor = db.cursor()
cursor.execute("create table KPGMSP1(QBID varchar(30),name varchar(15),race varchar(30),server varchar(2),premission int(1),PW char(30),Message int(255),MSGContent char(255),NMSG int(10),NMC char(255))")
# 已有则注释掉

number = 0
number1 = 0
number2 = 0
message1 = 0
CountMB=0

# 此处可优化
while True:
    while True:
        cursor.execute("select * from KPGMSP1")
        data = cursor.fetchall()
        while True:

            try:
                data[CountMB]
                CountMB=CountMB+1
            except:
                break        
        try:
            Start = int(input("请选择 登入(1) | 注册(2) | 疑难疑问查询/举报/功能建议及其他反馈(3) | 入队申请(4) | 公告栏(5) | 找回账号/密码(6) | 商业合作(7) | 退出登入界面(8) | ："))
        except ValueError:
            print("请输入操作所对应的操作编号")

            continue

# 测试人员快捷通道
        if Start ==111 or 1123:
            memberno = 0
            signupN='SeleiXi'
            break

#退出系统(登入界面)  
        if Start == 8:
            print("已退出登入界面")
            break
# 登入
        elif Start == 1:
            memberno=0
            signupN = input("请输入您已登记的QQ/战网ID（带#和数字）(退出登入模式请输入88)：")
            while True:   
                if memberno < CountMB:
                    if data[memberno][0] == signupN:
                        break
                    if signupN == "88":
                        break
                    memberno= memberno+1
                else :
                    print("成员不存在")
                    signupN = "88"
                    break
            if signupN == "88":
                    continue

                
                    
            
            password = input("请输入密码:")
            if password == data[memberno][5]:
                break
            else:
                print("输入错误")
                password = input("请重新输入密码:")
                if password == data[memberno][5]:
                    print("登入成功")
                    break
                else:
                    print("输入错误")
                password = input("请重新输入密码:")
                if password == data[memberno][5]:
                    print("登入成功")
                    break
                else:
                    print("输入错误")
                password = input("请重新输入密码:")
                if password == data[memberno][5]:
                    print("登入成功")
                    break
                else:
                    print("输入错误")
                print("尝试过多,请重新再来")
                continue

# 新建成员信息
        elif Start == 2: 

            while True:
                print  ("QQ号及战网ID二选一填,Q号请确保已在战队内部群，战网ID带#和数字,请确保登记ID已挂[KPG]或分队战队队标，此栏将会作为日后账号的登入账号") 
                QBID = input("请输入 Q号 | 战网ID：")
                CN = input("请输入游戏ID(退出新建模式请输入88)：")
                if CN == "88" :
                    break

                while True:
                    CR = input("请输入游戏主族：").upper().strip()
                    if  CR == "P":
                        break
                    elif  CR == "T":
                        break
                    elif  CR == "Z":
                        break
                    elif  CR == "R":
                        break
                    else:
                         print("请输入 P | T | Z | R 其一作为游戏主族")
                while True:
                    Server = input("请输入常驻服务器：").upper().strip()
                    if  Server == "CN":
                        Server1 = 1
                        break
                    elif  Server == "KR":
                        Server1 = 1
                        break
                    elif  Server == "EU":
                        Server1 = 1
                        break
                    elif  Server == "US":
                        Server1 = 1
                        break
                    else:
                        print("请输入 CN | KR | EU | US 其一作为常驻服务器")
                        print("Please choose the server that you mostly played: CN | KR | EU | US")

                CP = input("请输入密码：")
                while CP =="88":
                    print("密码不能为88")
                    CP = input("请输入密码：")

                if Server1 == 1:
                    cursor.execute("INSERT INTO KPGMSP1(QBID,name, race, server, premission,PW,Message,NMSG)   VALUES ('%s', '%s',  '%s',  '%s',  %s ,'%s',%s,%s)" % (QBID, CN, CR, Server, 0,CP,0,0))
                    # cursor.execute("INSERT INTO KPGMSP1(QBID,name, race, server, premission,PW,Message,NMSG)   VALUES (QBID, CN, CR, Server, 0,CP,0,0)")
                    db.commit()
                    break
#疑难疑问查询/举报/功能建议及其他反馈 
        elif Start == 3:
            pass

# 入队申请
        elif Start ==4:
            pass
# 退出登入界面
    if Start ==8:
        break
    
    
    
    
# 加载内部系统
    while not Start==8:
        cursor.execute("select * from KPGMSP1")
        data = cursor.fetchall()
        try:

           print("\n欢迎使用【KPG战队管理系统】V1.1")
           y = int(input("请输入操作编号选择要进行的操作(打开操作菜单请输入0):"))	
        except ValueError:
           print("请重新输入正确的指令")
           continue

            
        
        if y == 0:
            print(
                 f"""
---------------------------------------------------------------------------------
1. 退出系统
2. 查询/修改/删除 个人资料
3. 消息（{data[memberno][6]}条）
4. 战队公告栏
5. 即时通讯系统【功能尚未推出】
6. 报名SATL战队联赛（4500分以上）
7. 报名内阁
8. 报名SNL战队联赛 （4200分以下）【功能尚未推出】
9. 战队相关信息【功能尚未推出】

666. 战队管理【该功能仅提供于管理员】 
---------------------------------------------------------------------------------""")
            continue
            
        

        # 查询/修改/删除个人资料
        elif y == 2:
            ChoIns = input("请选择  查询(1) | 修改(2) | 删除(3)  个人信息 ：")
            if ChoIns == "1":
                    PMS = data[memberno][4]
                    if PMS==0:
                        identity = "普通成员"
                    elif PMS==1:
                        identity = "管理员"
                    elif PMS==3:
                        identity = "战队队长"
                    print("游戏名称：",end="")
                    print(data[memberno][1],end="  游戏主族：")
                    print(data[memberno][2],end="  游戏常驻服务器：")
                    print(data[memberno][3],end="  战队身份：")
                    print(identity,end= " QQ/暴雪战网ID：")
                    print(data[memberno][0])

            # 修改名单指令
            elif ChoIns == '2': 
                QBID = data[memberno][0]
                name = data[memberno][1]
                race = data[memberno][2]
                server = data[memberno][3]
                premission = data[memberno][4]
                PW = data[memberno][5]
                MessageC = data[memberno][6]
                MSGContent = data[memberno][7]
                NMSG = data[memberno][8]
                if MSGContent == 'None':
                    MSGContent = ""
                while True:
                        Confirm = input("请输入密码以确认身份（退出修改模式请输入88）：")
                        if Confirm == "88":
                            break
                        elif Confirm == data[memberno][5]:
                            break
                        else:
                            print("输入错误")
                if Confirm == "88":
                    continue
                SelectChange = input("请选择要更改的内容( QQ/战网ID(1) | 游戏ID(2) | 游戏种族(3) | 常驻服务器(4) | 密码(5) | 退出模式(88) )：")
                SelectChange.strip

                if SelectChange == "1":
                    QBID = input("请输入新QQ/战网ID：")
                    cursor.execute(f"DELETE FROM KPGMSP1 Where QBID = '{data[memberno][0]}'")
                    cursor.execute(f"INSERT INTO KPGMSP1(QBID,name, race, server, premission,PW,Message,MSGContent,NMSG)   VALUES ('{QBID}','{name}', '{race}', '{server}',{premission},'{PW}',{MessageC},'{MSGContent}',{NMSG})")
                    db.commit()

                elif SelectChange == "2":
                    name = input("请输入新游戏ID：")
                    cursor.execute(f"DELETE FROM KPGMSP1 Where QBID = '{data[memberno][0]}'")
                    cursor.execute(f"INSERT INTO KPGMSP1(QBID,name, race, server, premission,PW,Message,MSGContent,NMSG)   VALUES ('{QBID}','{name}', '{race}', '{server}',{premission},'{PW}',{MessageC},'{MSGContent}',{NMSG})")
                    db.commit()


                elif SelectChange == "3":
                    while True:
                        race = input("请输入新游戏主族：").upper().strip()
                        if  race == "P":
                            break
                        elif  race == "T":
                            break
                        elif  race == "Z":
                            break
                        elif  race == "R":
                            break
                        else:
                             print("请输入 P | T | Z | R 其一作为游戏主族")
                    cursor.execute(f"DELETE FROM KPGMSP1 Where QBID = '{data[memberno][0]}'")
                    cursor.execute(f"INSERT INTO KPGMSP1(QBID,name, race, server, premission,PW,Message,MSGContent,NMSG)   VALUES ('{QBID}','{name}', '{race}', '{server}',{premission},'{PW}',{MessageC},'{MSGContent}',{NMSG})")
                    db.commit()


                elif SelectChange == "4":
                    while True:
                        Server = input("请输入常驻服务器：").upper().strip()
                        if  Server == "CN":
                            Server1 = 1
                            break
                        elif  Server == "KR":
                            Server1 = 1
                            break
                        elif  Server == "EU":
                            Server1 = 1
                            break
                        elif  Server == "US":
                            Server1 = 1
                            break
                        else:
                            print("请输入 CN | KR | EU | US 其一作为常驻服务器")
                            print("Please choose the server that you mostly played: CN | KR | EU | US")
                    cursor.execute(f"DELETE FROM KPGMSP1 Where QBID = '{data[memberno][0]}'")
                    cursor.execute(f"INSERT INTO KPGMSP1(QBID,name, race, server, premission,PW,Message,MSGContent,NMSG)   VALUES ('{QBID}','{name}', '{race}', '{server}',{premission},'{PW}',{MessageC},'{MSGContent}',{NMSG})")
                    db.commit()


                elif SelectChange ==5:
                    PW = input("请输入新密码")
                    cursor.execute(f"DELETE FROM KPGMSP1 Where QBID = '{data[memberno][0]}'")
                    cursor.execute(f"INSERT INTO KPGMSP1(QBID,name, race, server, premission,PW,Message,MSGContent,NMSG)   VALUES ('{QBID}','{name}', '{race}', '{server}',{premission},'{PW}',{MessageC},'{MSGContent}',{NMSG})")
                    db.commit()
   

                elif SelectChange == "88":
                    pass
                else:
                    print("指令不在范围内")
            # 删除人员指令
            elif ChoIns == "3":

                while True:
                    QBID=data[memberno][0]
                    Confirm = input("请输入密码以确认身份（退出删除模式请输入88）：")
                    if Confirm == 88:
                        break
                    elif Confirm == data[memberno][5]:
                        cursor.execute(f"DELETE FROM KPGMSP1 where QBID='{QBID}'")
                        db.commit()
                        break
                    else:
                        print("输入错误")

                break

        # 消息栏
        elif y == 3:
            if data[memberno][6]>=1:
                cursor.execute(f"UPDATE kpgmsp1 SET Message = 0 where QBID = '{data[memberno][0]}'")
            print(data[memberno][7])
        # 公告栏
        elif y == 4:
            cursor.execute("select * from announcement")
            dataA = cursor.fetchall()
            AnnoucementNo = 0
            while True:
            
                try:
                    print(f'''公告{AnnoucementNo+1}(发布者：{dataA[AnnoucementNo][2]} 发布于：{dataA[AnnoucementNo][1]})：
{dataA[AnnoucementNo][0]}''')
                    AnnoucementNo=AnnoucementNo+1
                    print("\n")
                except:
                    if AnnoucementNo ==0:
                        print("暂无公告")
                    break
        # 退出系统指令
        elif y == 1:
           print("已退出【KPG战队管理系统】")
           break         

        # 即时通讯系统
        elif y == 5:
            number = 1
            x=0
            while x < CountMB:
                # 必须是对应编号 假如说有5个人 这里就得是CountMB 因为后续没有memberno=memberno-1,纯考虑字典的显示{所有人}代码
                PMS = data[x][4]
                if PMS==0:
                    identity = "普通成员"
                elif PMS==1:
                    identity = "管理员"
                elif PMS==3:
                    identity = "战队队长"
                
                
                print('{0}.{1} 种族：{2} 常驻服务器：{3} 战队身份：{4}'.format(number,data[x][1],data[x][2],data[x][3],identity))
                x = x+1
                number = number +1

        # 报名SATL战队联赛
        elif y == 6:
            # 导入到excel文件（分一队二队）
            # 修改资料指令
            # 删除资料指令
            # 删去输入的空格 自动大写种族 邮箱格式 战网格式 比赛种族只能选指定的4个,QQ输入            
            #  (附SATL规则,rep)
            if number1 >= 8:
                print("一队报名已满")
            if number2 >= 8:
                print("二队报名已满")
            try:
                MMR = int(input("请输入目前所在的MMR(退出报名模式请在此处输入88):"))	
            except ValueError:
                print("请重新输入正确的指令(MMR请输入纯数字)")
                continue
            if MMR == 88:
                print("成功退出报名模式")
                continue
            if MMR > 6500:
                print("爬")
                continue
            if MMR < 5000:
                print("分数尚未达一队主力标准")
                if MMR < 4800:
                    print("分数尚未达到一队替补/二队主力标准")
                    if MMR < 4500:
                        print("分数尚未达到二队替补标准")
                        continue
                    else:
                        print("分数已达到二队替补标准")
                        Cteam = 2              
                else:
                    print("分数已达到一队替补/二队主力标准")
                    Cteam = int(input("请选择报名分队:（1 | 2）"))
    
            else:
                
                print("分数达到一队主力标准")
                Cteam = int(input("请选择报名分队:（1 | 2）"))
    
            if Cteam == 1 :
                while not number1 >=8:
                    break
                else:
                    print("一队报名已满,请另选分队（如未满）")
                    continue
                
            elif Cteam == 2:
                while not number2 >=8:
                    
                    break
                else:
                    print("二队报名已满,请另选分队（如未满）")
                    continue
                
                
            mail = input("请输入游戏战网邮箱：")
            Srace = input("请输入比赛报名种族：")
            BlzID = input("请输入暴雪战网id（包括数字）:")
            Gname = input("请输入游戏内ID（不用输入队标,若在比赛期间更改,届时请即刻用下方修改功能重新输入新ID）：")
            while True:
                try:
                    QQ = int(input("请输入QQ："))
                    break
                except:
                    continue
    
            if Cteam == 1:
                number1=number1+1
                CteamN = f"一队（B级）,{number1}号选手"           
            elif Cteam == 2:
                number2=number2+1
                CteamN = f"二队（C级）,{number2}号选手"
                
    
            print(
            f"""
报名参赛分队+选手序号：{CteamN}
战网邮箱：{mail}
战网ID（带数字):{BlzID}
游戏ID：KPG.{Gname}
报名种族：{Srace}
现MMR：{MMR}
QQ：{QQ}
            """)
                
                
    
    

           


# 报名内阁
        elif y ==7:
            # 先try load之前的问题（因为不限时 所以将会加载先前的问题）
            cmembernoinetqs=[
"写出兼队的利与弊（75字+）",
"如果队员发生游戏上的矛盾，列出解决方法（100字+）",
"如果有队员在天梯上骂人并被举报，最好的解决方法是（75字+）",
"如何让新成员融入队内（100字+）",
"如何让队员自发地组织练习（75字+）",
"如何让队内氛围更加活跃（150字+）"
]
# 6条
            print("""
e.g.
为什么内阁问题要设置字数?
即便表达能力优秀至能将内容极度精简化，但能把观点解释完整，也具有着一条字数准线。
同时介于题目的局限性较小，亦没有标准答案，答者也可以从一个观点的多方面回答以及设立多个观点。除去考验管理者管理能力之外，
字数同时也是一个确认答者入阁态度的考验，若是无法完成如此工作量，怕是难以承担入阁后组织活动的工作量。
并且考虑到答者可能存在的个人原因而不限时,但这也给予了更多机会于答者完善自己的回答。
回答没有标准答案，无论是否,只要合理以及观点解释完整就都可以接受,最终给分将会综合多位1给予的分数。

Example2(参考答案自1Misaka):
战队是否应该让Q群群昵称后带mmr?试解释。
不需要。mmr作为实力表现的一方面，对于有一定实力的队员是不在意，但考虑到为了吸纳新人，列出mmr对新人会有一定的打击或者害怕mmr低被人嘲笑，
认为做出一点挽留保护个人的实力是有必要的，对于实力可以直接上线拉克希尔了解。相对于展示mmr则是为了避免低分段逆天发言，但从长远考虑意义不大，对于新人的保护比这一点更为重要
(150字)

（内容在提交后三天内会给予分数及相应点评,分数高于80即为通过,若是二次考核内阁会与第一次的问题不一样）



""")
            # CmembernoEXAM = CmembernoEXAM+1 
            # if cmembernoexam==2
            # print+break
            # if==1 
            # print(cmembernoinetqs[L1[6]])
            # 
            L1 = random.sample(range(0, 5), 5)
            L2 = [75,100,75,100,75,150]
            print("问题一：")
            print(cmembernoinetqs[L1[0]])
            ans = input("请输入回答：")
            ansL = L2[L1[0]]-len(ans)
            while ansL >=0:
                print(f'尚欠{ansL}字')
                ans = input("请输入回答：")
                ansL = L2[L1[0]]-len(ans)
            print("问题二：")
            print(cmembernoinetqs[L1[1]])
            while True:
                
                ans2 = input("请输入回答：")
                ansL2 = L2[L1[1]]-len(ans2)
                if ansL2 <=0:
                    break
                else:
                    print(f'尚欠{ansL2}字')
                    continue
            print("问题三：")
            print(cmembernoinetqs[L1[2]])
            while True:
                ans3 = input("请输入回答：")
                ansL3 = L2[L1[2]]-len(ans3)
                if ansL3 <=0:
                    break
                else:
                    print(f'尚欠{ansL3}字')
                    continue
            print("问题四：")
            print(cmembernoinetqs[L1[3]])
            while True:
                
                ans4 = input("请输入回答：")
                ansL4 = L2[L1[3]]-len(ans4)
                if ansL4 <=0:
                    break
                else:
                    print(f'尚欠{ansL4}字')
                    continue
            print("问题五：")
            print(cmembernoinetqs[L1[4]])
            while True:
                ans5 = input("请输入回答：")
                ansL5 = L2[L1[4]]-len(ans5)
                if ansL5 <=0:
                    break
                else:
                    print(f'尚欠{ansL5}字')
                    continue
            # if cmembernoexam ==0
            ansdict ={
            'Ans' : ans,
            'Ans2' : ans2,
            'Ans3' : ans3,
            'Ans4' : ans4,
            'Ans5' : ans5,
            }

        elif y == 666:
            while True:
                if data[memberno][4]>1:
                    print("\n欢迎来到管理员模式")
                    Manage = input("请输入要进行的操作(输入0打开菜单)")
                else:
                    print("暂无管理员权限")
                    Manage = "1"
                    break
                if Manage == "0":
                
                    print("""


1. 退出管理模式
2. 疑难疑问回馈【尚未推出】
3. 发布公告
4. 暂时禁言【尚未推出】
5. 内阁笔试打分【尚未推出】

            
            """)


            # 发布公告
                elif Manage == "1":
                    break
                elif Manage == "3":
                        PublishContent = input("请输入要发布的内容：")
                        annoucementTIME=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                        str(annoucementTIME)
                        cursor.execute(f"INSERT INTO Announcement (announcement,Time,发布者) Values ('{PublishContent}','{annoucementTIME}','{data[memberno][1]}')")
                        cursor.execute("UPDATE kpgmsp1  SET Message = Message+1") 
                        ANC = 0 
                        if data[ANC][7] == None:
                            cursor.execute("""UPDATE kpgmsp1  SET MSGContent = '【系统公告】您收到了一条新的战队公告'""") 
                            ANC = ANC+1
                        elif data[ANC][7]:
                            cursor.execute("""UPDATE kpgmsp1  SET MSGContent =CONCAT(MSGContent,'
【系统公告】您收到了一条新的战队公告')""") 
                            ANC = ANC+1
                        db.commit() 
                        




                        ACount = 0
                        ACount =ACount+1
                            

                    # 4可用把promission改为0（即游客临时账号），在部分功能中加入if promission=0, print（暂无权限， break
                elif Manage =="4":
                        pass
                    



                
            if Manage =="1":
                continue









db.commit() 
db.close()
