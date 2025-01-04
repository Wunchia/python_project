# Author Wunchia
# 2025年01月04日22时28分23秒
# wunchia@outlook.com

#sort 改变原列表顺序
#sorted 不改变原列表顺序 返回一个有序的新列表

my_list='This is a test string of sort and sorted from A'.split()
print(my_list)

def change_lower(str_name:str):
    return str_name.lower()

print(sorted(my_list,key=change_lower)) #key可以传递一个比较规则函数
print(my_list) #此时还未改变

my_list.sort(key=change_lower)
print(my_list) #发生改变

print('-'*50)

student_tuples=[
    ('John', 'F',15),
    ('Jack', 'K',12),
    ('Amy', 'K',11),
]

print(sorted(student_tuples,key=lambda x: (x[1],x[2]))) #lambda表达式

print('-'*50)
class Student:
    def __init__(self,name:str,grade:int,age:int):
        self.name=name
        self.grade=grade
        self.age=age

    # def __str__(self):
    #     return f'{self.name} {self.grade} {self.age}'
    def __repr__(self): #相对于str 可以返回多种类型 而str必须是string
        return repr((self.name,self.grade,self.age))

student1=Student('Micheal',23,18)
print(student1)