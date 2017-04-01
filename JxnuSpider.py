# -*- coding: utf-8 -*-
import requests
import re
import os
import sys
reload(sys)                      # reload 才能调用 setdefaultencoding 方法
sys.setdefaultencoding('utf-8')  # 设置 'utf-8'
def Query(ss,tt):
    ans=re.findall(ss,tt)[0]
    ans=ans.strip()
    return ans
def downPhoto(url,path,cook):
    photo_data=requests.get(url,cookies=cook)
    output = open(path, 'wb')
    output.write(photo_data.content)
    output.close()
def downText(data,path):
    output = open(path, 'wb')
    for each in data:
        output.write(each)
        output.write('\n')
    output.close()
def judgeDigital(num,cnt):
    ans=str(num)
    while len(ans)<cnt:
        ans='0'+ans
    return ans
if __name__ == "__main__":
    new_url="http://jwc.jxnu.edu.cn/MyControl/All_Display.aspx?UserControl=All_StudentInfor.ascx&UserType=Student&UserNum="
    cookies='_ga=GA1.3.1162983937.1484892417; _gscu_1575220171=89667079izbk4n16; ASP.NET_SessionId=13gpfsylk4ez2iiwjgrzyhwr; JwOAUserSettingNew=UserNum=tsFcj7GNQ05f6R5Gozi94g==&UserName=fw7lKGxYVrM=&UserType=WmTb330+jk8=&UserLoginTime=2017/3/31 22:33:14'
    cook={"Cookie":cookies}


    name_str='<span id="_ctl0_lblXM">(.*?)</span>'
    id_str='<span id="_ctl0_lblXH">(.*?)</span></td>'
    class_str='<span id="_ctl0_lblBJ">(.*?)</span></td>'
    sex_str='<span id="_ctl0_lblXB">(.*?)</span></td>'

    # test student_id:1308092060
    for grade in range(12,17):
        for class_id in range(1342,1000000):
            print "now downloading "+str(class_id)
            for class_in_id in range(1,100):
                grade_str=judgeDigital(grade,2)
                class_id_str=judgeDigital(class_id,6)
                class_in_id_str=judgeDigital(class_in_id,2)
                student_id=grade_str+class_id_str+class_in_id_str
                down_url=new_url+student_id
                try:
                    obj=requests.get(down_url,cookies=cook)
                except:
                    print down_url+"error"
                name=Query(name_str,obj.text)
                id=Query(id_str,obj.text)
                class_name=Query(class_str,obj.text)
                sex=Query(sex_str,obj.text)
                if name=='Label' or name=="":
                    break
                if os.path.exists(grade_str)==False:
                    os.mkdir(grade_str)
                class_id_path=grade_str+'/'+class_name
                if os.path.exists(class_id_path)==False:
                    os.mkdir(class_id_path)
                class_in_id_path=class_id_path+'/'+name
                if os.path.exists(class_in_id_path)==False:
                    os.mkdir(class_in_id_path)
                else :
                    continue

                photo_url='http://jwc.jxnu.edu.cn/StudentPhoto/'+student_id+'.jpg'
                photo_path=class_in_id_path+'/'+student_id+'.jpg'
                downPhoto(photo_url,photo_path,cook)

                text_data=[name,id,class_name,sex]
                text_path=class_in_id_path+'/'+student_id+'.txt'
                downText(text_data,text_path)






