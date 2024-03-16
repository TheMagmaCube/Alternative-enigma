while 1>0:
    operator = ''
    slowa_input = []
    slowa_input_a = []
    slowa_user_input = str(input ('Wpisz tekst.'))
    for char in slowa_user_input:
            slowa_input_a.append(char)
            while len(slowa_input_a) == 3:
                operator += slowa_input_a[0]
                operator += slowa_input_a[1]
                operator += slowa_input_a[2]
                slowa_input_a = []
                slowa_input.append(operator)
                operator = ''
    print(slowa_input)