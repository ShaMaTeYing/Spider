# -*- coding: utf-8 -*-
import requests
import re
import os
import sys
reload(sys)                      # reload 才能调用 setdefaultencoding 方法
sys.setdefaultencoding('utf-8')  # 设置 'utf-8'
#用正则表达式提取内容
def Query(ss,tt):
    ans=re.findall(ss,tt)[0]
    ans=ans.strip()
    return ans
#下载照片
def downPhoto(url,path,cook):
    photo_data=requests.get(url,cookies=cook)
    output = open(path, 'wb')
    output.write(photo_data.content)
    output.close()
#下载文本数据
def downText(data,path):
    output = open(path, 'wb')
    for each in data:
        output.write(each)
        output.write('\n')
    output.close()
#不足cnt位，补充前导0
def judgeDigital(num,cnt):
    ans=str(num)
    while len(ans)<cnt:
        ans='0'+ans
    return ans
#python的主函数
if __name__ == "__main__":
    new_url="http://jwc.jxnu.edu.cn/MyControl/All_Display.aspx?UserControl=All_StudentInfor.ascx&UserType=Student&UserNum="
	#cookies可能过期了，要自己去重新弄个cookies来程序才有用
	cookies='_ga=GA1.3.1162983937.1484892417; _gscu_1575220171=89667079izbk4n16; ASP.NET_SessionId=13gpfsylk4ez2iiwjgrzyhwr; JwOAUserSettingNew=UserNum=tsFcj7GNQ05f6R5Gozi94g==&UserName=fw7lKGxYVrM=&UserType=WmTb330+jk8=&UserLoginTime=2017/3/31 22:33:14'
    cook={"Cookie":cookies}

	#构造提取姓名，学号，班级，性别的正则匹配串,其实只要把想获取的内容用(.*?)替换就可以啦
    name_str='<span id="_ctl0_lblXM">(.*?)</span>'
    id_str='<span id="_ctl0_lblXH">(.*?)</span></td>'
    class_str='<span id="_ctl0_lblBJ">(.*?)</span></td>'
    sex_str='<span id="_ctl0_lblXB">(.*?)</span></td>'

    # test student_id:1308092060
    for grade in range(12,17):
        for class_id in range(1,1000000):
            print "now downloading "+str(class_id)
            for class_in_id in range(1,100):
                grade_str=judgeDigital(grade,2)#不足位数补齐前导零
                class_id_str=judgeDigital(class_id,6)
                class_in_id_str=judgeDigital(class_in_id,2)
                student_id=grade_str+class_id_str+class_in_id_str#构造学号
                down_url=new_url+student_id#构造信息页面的URL
                try:#有可能会出错，所以要用异常
                    obj=requests.get(down_url,cookies=cook)
                except:
                    print down_url+"error"
                name=Query(name_str,obj.text)#提取姓名
                id=Query(id_str,obj.text)
                class_name=Query(class_str,obj.text)
                sex=Query(sex_str,obj.text)
                if name=='Label' or name=="":#如果数据无效，跳出循环
                    break
                if os.path.exists(grade_str)==False:#判断文件夹是否存在，不存在则创建
                    os.mkdir(grade_str)
                class_id_path=grade_str+'/'+class_name
                if os.path.exists(class_id_path)==False:
                    os.mkdir(class_id_path)
                class_in_id_path=class_id_path+'/'+name
                if os.path.exists(class_in_id_path)==False:
                    os.mkdir(class_in_id_path)
                else :
                    continue

                photo_url='http://jwc.jxnu.edu.cn/StudentPhoto/'+student_id+'.jpg'#构造存储图片的URL
                photo_path=class_in_id_path+'/'+student_id+'.jpg'#构造存储图片的路径
                downPhoto(photo_url,photo_path,cook)#下载图片

                text_data=[name,id,class_name,sex]
                text_path=class_in_id_path+'/'+student_id+'.txt'#构造存储文本的路径
                downText(text_data,text_path)






