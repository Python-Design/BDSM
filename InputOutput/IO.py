'''
    Библотека BoriStyleGuide
IO - InputOutput

'''

''' Input '''


#value - обрабатываемое значене
#needtype - нужный тип
#showmessage - вывод сообщения
def check(value, needtype, showmessage=''):
    ourtype = type(value)  #получение типа данных
    if ourtype == needtype:  #сравнение с нужным типом
        return True
    elif ourtype == str:
        try:
            return check(int(value), needtype, showmessage)
        except ValueError:
            pass
        try:
            return check(float(value), needtype, showmessage)
        except ValueError:
            pass
        if ourtype == needtype:
            return check(str(value), needtype, showmessage)
        else:
            if showmessage:
                print("Введено некорректное значение")
            #return False
    else:
        if showmessage:
            print("Введено некорректное значение")
        #return False


# input_massage - приглашение на ввод, vtype - тип необходимой переменой
def binput(vtype, input_massage=''):
    value = input(input_massage)
    if check(value, vtype, False):
        return value
    else:
        return check(value, vtype, True)


''' Output '''
# Make title
# manual will be added for user align like '{:9s}'.format()
def title(title_text, align='mid', style='', manual=False):  # example: style='+' result: + title_text +
    title_text = str(str(style) + title_text + str(style))
    if not manual:
        if align == 'mid':
            print('\t\t', title_text)
        elif align == 'left':
            print('\t', title_text)
        elif align == 'right':
            print('\t\t\t', title_text)
    else:
        print(' '*align, title_text)


# Makes table
# column_titles can be array of names like ['A1','A2']
# data is like array of columns, ex: [x1,x2]
def table_one_type(column_names=1, column_names_align=3, left_column_names_align=3, data=[], datatype=str, tail=None, align=3):
    amount_of_columns = 0
    vertical_length = len(data[0])

    # aligns
    if datatype == int:
        align = '{:'+ str(align) + 'd}'
    elif datatype == float:
        align = '{:'+ str(align) + '.' + str(tail) + 'f}'
    elif datatype == str:
        align = '{:'+ str(align) + 's}'

    # column names align
    column_names_align = '{:'+ str(column_names_align) + 's}'
    left_column_names_align = '{:'+ str(left_column_names_align) + 's}'

    # getting amount of columns
    if check(column_names,int):
        amount_of_columns = column_names
        column_names = [str(i+1) for i in range(column_names)]

    else:
        amount_of_columns = len(column_names)

    # checking if
    if amount_of_columns == len(data):
        if not check(column_names,int):
            # print of column names
            print(left_column_names_align.format(''), end='')  # required for align of column names
            for i in range(amount_of_columns):
                print(column_names_align.format(column_names[i]), end='')
            print()
            # print of data
            for i in range(vertical_length):
                for j in range(amount_of_columns):
                    value = data[j][i]
                    print(align.format(value), end='')
                print()
    else:
        print('Кол-во навзаний столбцов не равно кол-ву столбцов')


# much more simpler table but supporting multitype
def table(data=[], data_types=[], column_names=[]):
    amount_of_columns = 0
    # getting amount of columns
    if check(column_names,int):
        amount_of_columns = column_names
        column_names = [str(i+1) for i in range(column_names)]
    else:
        amount_of_columns = len(column_names)
    if amount_of_columns == len(data):

        # finding longest massive
        vertical_length = 0
        for i in data:
            if len(i) > vertical_length:
                vertical_length = len(i)

        # data preprocessing
        x_data = []
        for i in range(len(data)):
            x_data.append([column_names[i],])
            for j in range(vertical_length):
                if j >= len(data[i]):
                    x_data[i].append(None)
                else:
                    if data_types[i] == float:
                        x_data[i].append(float(data[i][j]))
                    else:
                        x_data[i].append(data[i][j])

        # printing table
        for j in range(len(x_data[i])):
            for i in range(amount_of_columns):
                if data_types[i] == str:
                    value = str(x_data[i][j])
                    print('\t','{:9s}'.format(value), end='')
                elif data_types[i] == int:
                    value = str(x_data[i][j])
                    print('\t','{:9s}'.format(value), end='')
                elif data_types[i] == float:
                    if check(x_data[i][j],float) != None:
                        print('\t','{:9.4f}'.format(float(x_data[i][j])), end='')
                    else:
                        value = str(x_data[i][j])
                        print('\t','{:9s}'.format(value), end='')
            print()
    else:
        print('Кол-во навзаний столбцов не равно кол-ву столбцов')


# bprint is like orignial print(), but with customizable tail and integer part for float + ending
def bprint(*args, integer=3 ,tail=7, ending=' '):
    if len(args) == 0:
        print()
    else:
        for i in args:
            if check(i, float):
                size = '{:'+str(integer)+'.'+str(tail)+'f}'
                print(size.format(i), end=ending)
            else:
                print(i, end=ending)
