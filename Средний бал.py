
ListOfStudents = { 'Имя ученика' : "средний бал ученика"}

print(' вводите оценки через пробел, когда закончите нажмите "Enter"  ')
while 1 != 0:
    StrName = input('Имя ученика:')
    StrGrades=input('Его оценки:')
    Grades=list(map(int , StrGrades[0::2]))
    #print(Grades)
    AveregeScore = sum(Grades) /  len(Grades)
    ListOfStudents [StrName] =  AveregeScore
    StrName = input('Enter для продолжения, введите 0 если вы закончили ')
    if  '0' in StrName:
        break
print(ListOfStudents)
#Kos = 1 #попытался укусить больше чем могу сейчас
#Grades = [5,4,5,5]
# = ()
#print('Еще? 1- да / 2 нет')
#ListOfStudents = { 'Student1' : [2,4,3,3,3]}
#ListOfStudents = { 'Student2' : [2,2,2,3]}
#ListOfStudents = { 'Student3' : [5,3,4,5]}
#AveregeScore = sum(Grades[0]) /  len(Grades[1])
#подсчитываем средний бал
#input('''Привет, выбери что ты хочешь сделать:
 #   0 - Добавить учеников и оценки
 #   1 - вывести список учеников и их оценки
 #   2 - Показать список учиников и их средний бал
 #   3 - Добавить учиника
 #   4 - Добавить оценки ученику
#    5 - Посмотреть оценки конкретного учиника
 #   (нажми Enter, для продолжения)''')
#Ans_= input()
#if int(Ans_) == 1: #вывести список учеников и их оценки
#   print(ListOfStudents.keys())
#elif int(Ans_) == 2:#вывести список учеников и средний бал
 #   print(AveregeScore)
#elif int(Ans_) == 3:#добавить ученика и его оценки если есть
  #  print(ListOfStudents)
#elif int(Ans_) == 4:#добавить заданному ученику новые оценки
#    NameOfStud = input('Как зовут ученика? ' )
 #   NewScore = input( ' Через запятую введите оценки ученика :')
  #  print(NewScore)
#elif int(Ans_) == 0:#Добавить учеников и оценки

#else: print('введенна неверная цифра')
