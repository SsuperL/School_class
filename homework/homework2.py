import pickle,json
class School(object):
    def __init__(self,school_name,addr):
        self.addr=addr
        self.school_name=school_name
        self.grade={}
        self.course={}
        self.stu=[]
        self.teacher_class={}
    def create_class(self,class_obj,teacher_obj,coursename):
        '''创建班级'''
        self.grade.update({
            '%s'%class_obj.grade_name:{
            '讲师':'%s'%teacher_obj.teacher_name,
            '课程':'%s'%coursename,
            '学员':[]
            }
        })
        grade=[]
        grade.append(class_obj.grade_name)
        self.teacher_class .update({'%s'%teacher_obj.teacher_name:grade})

    def create_course(self,course_obj):
        '''创建课程'''
        self.course.update({
            '%s'%course_obj.course_name:{
                '周期':'%s'%course_obj.period,
                '价格':'%s'%course_obj.price
            }

        })
    def hire_teacher(self,teacher_obj):
        '''招聘讲师'''
        for i in self.grade.keys():
            if self.grade[i]['课程']==teacher_obj.course:
                if self.grade[i]['讲师']=='':
                    self.grade[i]['讲师'] =teacher_obj.teacher_name
    def enroll(self,choose,grade,stu_obj):
        '''学生注册'''
        self.stu.append(stu_obj.stu_name)
        self.grade['%s'%grade]['学员']=self.stu
        print(self.grade)
        with open('student','r',encoding='utf-8')as f:
            a=f.read()
            stu_dict=json.loads(a)
        with open('student','w',encoding='utf-8')as f:
            stu_dict['%s'%choose]['%s'%grade]['学员']=self.stu
            # stu_dict.update({
            #    '%s'%choose:{ '%s'%grade:self.stu}
            # })
            f.write(json.dumps(stu_dict))



class Grade(School):
    def __init__(self,grade_name,):
        self.grade_name=grade_name




class Course():
    def __init__(self,course_name,period,price):
        self.course_name=course_name
        self.period=period
        self.price=price



class Teacher(School):
    def __init__(self,teacher_name,course):
        self.teacher_name=teacher_name
        self.course=course
    def info(self):
        print('''
        -----Teacher %s info----
        name:    %s
        course:  %s
        
        '''%(self.teacher_name,self.course))
    def teach(self):
        print('%s is teaching %s in %s'%())

class Student():
    def __init__(self,stu_name,age):
        self.stu_name=stu_name
        self.age=age


school1 = School('北京', '北京市')
school2 = School('上海', '上海市')
# pickle.dump(school1)
# pickle.dump(school2)
Linux = Course('Linux', '24周', 5800)
Python = Course('Python', '32周', 7800)
Go = Course('Go', '25周', 6000)
teacher1=Teacher('Alex','Linux')
teacher2=Teacher('April','Python')
teacher3=Teacher('Peter','Go')
class1=Grade('class1')
school1.create_class(class1,teacher1,'Linux')
class2=Grade('class2')
school1.create_class(class2,teacher2,'Python')
class3=Grade('class3')
school2.create_class(class3,teacher3,'Go')
x=school1.create_course(Linux)
y=school1.create_course(Python)
z=school2.create_course(Go)
# print(school1.grade)
# print(school1.teacher_class)
def main():
    x='''
    1     学员
    2     讲师
    3     管理
    4     退出
    '''
    print(x)
    choice=input('请输入选择>>')
    if choice=='1':
        Stu()
    if choice=='2':
        Teach()

def Stu():
    name = input('姓名：')
    age = input('年龄：')
    # print('''
    # 1       注册
    # 2       查看个人信息
    # ''')
    school_dict={
        '北京':school1,
        '上海':school2
    }
    # x=pickle.loads(x1)
    # y=pickle.loads(y1)
    # z=pickle.loads(z1)
    student=Student(name,age)
    print('【学校】%s' % school1.school_name, '【地址】%s' % school1.addr)
    print('【学校】%s' % school2.school_name, '【地址】%s' % school2.addr)
    choose = input('请输入要报名的学校>>')
    if choose in school_dict:
        print('课程:')
        for i, item in enumerate(school_dict[choose].course.keys()):
            print(item, '【周期】%s' % school_dict[choose].course[item]['周期'], '【价格】%s' % school_dict[choose].course[item]['价格'])
        choose2 = input('请输入要报名的课程：')
        print('%s的班级有：'%choose2)
        for i in school_dict[choose].grade:
            if choose2==school_dict[choose].grade[i]['课程']:
                print(i,'\t\t【讲师】%s'%school_dict[choose].grade[i]['讲师'])
        choose3=input('请选择班级：')
        print('你报名的课程价格为：%s'%school_dict[choose].course[choose2]['价格'])
        while True:
            monney=int(input('请交清学费，否则无法注册>>'))
            if monney<int(school_dict[choose].course[choose2]['价格']):
                print('缴费失败，学费不足!')
            else:
                print('注册成功!')
                school_dict[choose].enroll(choose,choose3,student)
                exit()



def Teach():
    name=input('Teacher_name>>')
    course=input('your course>>')
    with open('teacher','r')as f:
        f.read()
    if name in f:
        teacher=Teacher(name,course)
    x=input('学校:')
    school_dict = {
        '北京': school1,
        '上海': school2
    }
    print('''
    1       个人信息
    2       查看管理的班级
    ''')
    choose=input('your choice>>')
    if choose=='1':
        teacher.info()
    if choose=='2':
        print('所管理的班级有:')
       # for
        print('''
        1       选择一个班级上课
        2       查看班级学员列表
        ''')
        choose2=input('choice>>')
        if choose2=='1':
            choose3=input('choose a class to teach>>')

main()