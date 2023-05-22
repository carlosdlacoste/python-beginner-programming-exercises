import random

def get_color(color_number=4):
    # making sure is a number and not a string
    color_number = int(color_number)

    switcher={
                  0:'red',
                  1:'yellow',
                  2:'blue',
                  3:'green',
                  4:'black'
              }
    return switcher.get(color_number,"Invalid Color Number")


def get_allStudentColors():
    example_color = get_color(1)
    students_array = []
    #your loop here
    for i in range(10):
        students_array.append(i)
        num_random = random.randint(0, 3)
        color = get_color(num_random)
        print("El color asignado al estudiante "+ str(students_array[i]) + " es: "+ color)

get_allStudentColors()