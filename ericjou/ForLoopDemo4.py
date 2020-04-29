e1 = {'name': 'John', 'salary': 50000, 'program ' : ['Jave', 'Python']}
e2 = {'name': 'Mary', 'salary': 60000,'program ' : ['VB', 'Python']}
e3 = {'name': 'Bob', 'salary': 70000,'program ' : ['Python']}
emps = [e1, e2, e3]
# 求會 Python 的人名
names=[]
lan
 for emp in emps:
      for p in emp['program']:
         names.append(emp['name'])

print(names)