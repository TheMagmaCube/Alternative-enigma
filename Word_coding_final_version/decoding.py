# Skrypt na odkodowywanie liczb trzy cyfrowych.



#                0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38
zbiór_znaków = ['0','a','ą','b','c','ć','d','e','ę','f','g','h','i','j','k','l','ł','m','n','ń','o','ó','p','q','r','s','ś','t','u','v','w','x','y','z','ż','ź',' ',',','.']


#                      
zakodowany_zbiór_znaków = ['0','223','644','291','608','536','970','626','147','154','505','251','570','905','365','354','512','749','675','616','199','583','384','577','211','293','341','678','213','151','307','703','252','629','801','664','817','404','774']



while 1>0:
    operator = ''
    slowa_input = []
    slowa_input_a = []
    slowa_user_input = str(input ('Wpisz kod do odkodowania:'))
    for char in slowa_user_input:
            slowa_input_a.append(char)
            while len(slowa_input_a) == 3:
                operator += slowa_input_a[0]
                operator += slowa_input_a[1]
                operator += slowa_input_a[2]
                slowa_input_a = []
                slowa_input.append(operator)
                operator = ''

    

    while '223' in slowa_input:
        slowa_index_a = slowa_input.index('223')
        slowa_input[slowa_index_a] = zbiór_znaków[1]

    while '644' in slowa_input:
        slowa_index_ą = slowa_input.index('644')
        slowa_input[slowa_index_ą] = zbiór_znaków[2]
    
    while '291' in slowa_input:
        slowa_index_b = slowa_input.index('291')
        slowa_input[slowa_index_b] = zbiór_znaków[3]

    while '608' in slowa_input:
        slowa_index_c = slowa_input.index('608')
        slowa_input[slowa_index_c] = zbiór_znaków[4]

    while '536' in slowa_input:
        slowa_index_ć = slowa_input.index('536')
        slowa_input[slowa_index_ć] = zbiór_znaków[5]

    while '970' in slowa_input:
        slowa_index_d = slowa_input.index('970')
        slowa_input[slowa_index_d] = zbiór_znaków[6]
    
    while '626' in slowa_input:
        slowa_index_e = slowa_input.index('626')
        slowa_input[slowa_index_e] = zbiór_znaków[7]

    while '147' in slowa_input:
        slowa_index_ę = slowa_input.index('147')
        slowa_input[slowa_index_ę] = zbiór_znaków[8]

    while '154' in slowa_input:
        slowa_index_f = slowa_input.index('154')
        slowa_input[slowa_index_f] = zbiór_znaków[9]

    while '505' in slowa_input:
        slowa_index_g = slowa_input.index('505')
        slowa_input[slowa_index_g] = zbiór_znaków[10]

    while '251' in slowa_input:
        slowa_index_h = slowa_input.index('251')
        slowa_input[slowa_index_h] = zbiór_znaków[11]

    while '570' in slowa_input:
        slowa_index_i = slowa_input.index('570')
        slowa_input[slowa_index_i] = zbiór_znaków[12]

    while '905' in slowa_input:
        slowa_index_j = slowa_input.index('905')
        slowa_input[slowa_index_j] = zbiór_znaków[13]

    while '365' in slowa_input:
        slowa_index_k = slowa_input.index('365')
        slowa_input[slowa_index_k] = zbiór_znaków[14]

    while '354' in slowa_input:
        slowa_index_l = slowa_input.index('354')
        slowa_input[slowa_index_l] = zbiór_znaków[15]

    while '512' in slowa_input:
        slowa_index_ł = slowa_input.index('512')
        slowa_input[slowa_index_ł] = zbiór_znaków[16]

    while '749' in slowa_input:
        slowa_index_m = slowa_input.index('749')
        slowa_input[slowa_index_m] = zbiór_znaków[17]
    
    while '675' in slowa_input:
        slowa_index_n = slowa_input.index('675')
        slowa_input[slowa_index_n] = zbiór_znaków[18]
    
    while '616' in slowa_input:
        slowa_index_ń = slowa_input.index('616')
        slowa_input[slowa_index_ń] = zbiór_znaków[19]

    while '199' in slowa_input:
        slowa_index_o = slowa_input.index('199')
        slowa_input[slowa_index_o] = zbiór_znaków[20]

    while '583' in slowa_input:
        slowa_index_ó = slowa_input.index('583')
        slowa_input[slowa_index_ó] = zbiór_znaków[21]

    while '384' in slowa_input:
        slowa_index_p = slowa_input.index('384')
        slowa_input[slowa_index_p] = zbiór_znaków[22]

    while '577' in slowa_input:
        slowa_index_q = slowa_input.index('577')
        slowa_input[slowa_index_q] = zbiór_znaków[23]

    while '211' in slowa_input:
        slowa_index_r = slowa_input.index('211')
        slowa_input[slowa_index_r] = zbiór_znaków[24]

    while '293' in slowa_input:
        slowa_index_s = slowa_input.index('293')
        slowa_input[slowa_index_s] = zbiór_znaków[25]

    while '341' in slowa_input:
        slowa_index_ś = slowa_input.index('341')
        slowa_input[slowa_index_ś] = zbiór_znaków[26]
    
    while '678' in slowa_input:
        slowa_index_t = slowa_input.index('678')
        slowa_input[slowa_index_t] = zbiór_znaków[27]

    while '213' in slowa_input:
        slowa_index_u = slowa_input.index('213')
        slowa_input[slowa_index_u] = zbiór_znaków[28]

    while '151' in slowa_input:
        slowa_index_v = slowa_input.index('151')
        slowa_input[slowa_index_v] = zbiór_znaków[29]

    while '307' in slowa_input:
        slowa_index_w = slowa_input.index('307')
        slowa_input[slowa_index_w] = zbiór_znaków[30]

    while '703' in slowa_input:
        slowa_index_x = slowa_input.index('703')
        slowa_input[slowa_index_x] = zbiór_znaków[31]

    while '252' in slowa_input:
        slowa_index_y = slowa_input.index('252')
        slowa_input[slowa_index_y] = zbiór_znaków[32]

    while '629' in slowa_input:
        slowa_index_z = slowa_input.index('629')
        slowa_input[slowa_index_z] = zbiór_znaków[33]

    while '801' in slowa_input:
        slowa_index_ż = slowa_input.index('801')
        slowa_input[slowa_index_ż] = zbiór_znaków[34]

    while '664' in slowa_input:
        slowa_index_ź = slowa_input.index('664')
        slowa_input[slowa_index_ź] = zbiór_znaków[35]

    while '817' in slowa_input:
        slowa_index__ = slowa_input.index('817')
        slowa_input[slowa_index__] = zbiór_znaków[36]
    
    while '404' in slowa_input:
        slowa_index_1 = slowa_input.index('404')
        slowa_input[slowa_index_1] = zbiór_znaków[37]

    while '774' in slowa_input:
        slowa_index_dot = slowa_input.index('774')
        slowa_input[slowa_index_dot] = zbiór_znaków[38]

    while '223' in slowa_input:
        slowa_index_A = slowa_input.index('223')
        slowa_input[slowa_index_A] = zbiór_znaków[1]
    
    while '644' in slowa_input:
        slowa_index_Ą = slowa_input.index('644')
        slowa_input[slowa_index_Ą] = zbiór_znaków[2]
    
    while '291' in slowa_input:
        slowa_index_B = slowa_input.index('291')
        slowa_input[slowa_index_B] = zbiór_znaków[3]
    
    while '608' in slowa_input:
        slowa_index_C = slowa_input.index('608')
        slowa_input[slowa_index_C] = zbiór_znaków[4]

    while '536' in slowa_input:
        slowa_index_Ć = slowa_input.index('536')
        slowa_input[slowa_index_Ć] = zbiór_znaków[5]
    
    while '970' in slowa_input:
        slowa_index_D = slowa_input.index('970')
        slowa_input[slowa_index_D] = zbiór_znaków[6]
    
    while '626' in slowa_input:
        slowa_index_E = slowa_input.index('626')
        slowa_input[slowa_index_E] = zbiór_znaków[7]

    while '147' in slowa_input:
        slowa_index_Ę = slowa_input.index('147')
        slowa_input[slowa_index_Ę] = zbiór_znaków[8]

    while '154' in slowa_input:
        slowa_index_F = slowa_input.index('154')
        slowa_input[slowa_index_F] = zbiór_znaków[9]
    
    while '505' in slowa_input:
        slowa_index_G = slowa_input.index('505')
        slowa_input[slowa_index_G] = zbiór_znaków[10]

    while '251' in slowa_input:
        slowa_index_H = slowa_input.index('251')
        slowa_input[slowa_index_H] = zbiór_znaków[11]

    while '570' in slowa_input:
        slowa_index_I = slowa_input.index('570')
        slowa_input[slowa_index_I] = zbiór_znaków[12]

    while '905' in slowa_input:
        slowa_index_J = slowa_input.index('905')
        slowa_input[slowa_index_J] = zbiór_znaków[13]

    while '365' in slowa_input:
        slowa_index_K = slowa_input.index('365')
        slowa_input[slowa_index_K] = zbiór_znaków[14]

    while '354' in slowa_input:
        slowa_index_L = slowa_input.index('354')
        slowa_input[slowa_index_L] = zbiór_znaków[15]

    while '512' in slowa_input:
        slowa_index_Ł = slowa_input.index('512')
        slowa_input[slowa_index_Ł] = zbiór_znaków[16]

    while '749' in slowa_input:
        slowa_index_M = slowa_input.index('749')
        slowa_input[slowa_index_M] = zbiór_znaków[17]

    while '675' in slowa_input:
        slowa_index_N = slowa_input.index('675')
        slowa_input[slowa_index_N] = zbiór_znaków[18]

    while '616' in slowa_input:
        slowa_index_Ń = slowa_input.index('616')
        slowa_input[slowa_index_Ń] = zbiór_znaków[19]

    while '199' in slowa_input:
        slowa_index_O = slowa_input.index('199')
        slowa_input[slowa_index_O] = zbiór_znaków[20]

    while '583' in slowa_input:
        slowa_index_Ó = slowa_input.index('583')
        slowa_input[slowa_index_Ó] = zbiór_znaków[21]

    while '384' in slowa_input:
        slowa_index_P = slowa_input.index('384')
        slowa_input[slowa_index_P] = zbiór_znaków[22]

    while '577' in slowa_input:
        slowa_index_Q = slowa_input.index('577')
        slowa_input[slowa_index_Q] = zbiór_znaków[23]

    while '211' in slowa_input:
        slowa_index_R = slowa_input.index('211')
        slowa_input[slowa_index_R] = zbiór_znaków[24]

    while '293' in slowa_input:
        slowa_index_S = slowa_input.index('293')
        slowa_input[slowa_index_S] = zbiór_znaków[25]

    while '341' in slowa_input:
        slowa_index_Ś = slowa_input.index('341')
        slowa_input[slowa_index_Ś] = zbiór_znaków[26]

    while '678' in slowa_input:
        slowa_index_T = slowa_input.index('678')
        slowa_input[slowa_index_T] = zbiór_znaków[27]

    while '213' in slowa_input:
        slowa_index_U = slowa_input.index('213')
        slowa_input[slowa_index_U] = zbiór_znaków[28]

    while '151' in slowa_input:
        slowa_index_V = slowa_input.index('151')
        slowa_input[slowa_index_V] = zbiór_znaków[29]

    while '307' in slowa_input:
        slowa_index_W = slowa_input.index('307')
        slowa_input[slowa_index_W] = zbiór_znaków[30]

    while '703' in slowa_input:
        slowa_index_X = slowa_input.index('703')
        slowa_input[slowa_index_X] = zbiór_znaków[31]

    while '252' in slowa_input:
        slowa_index_Y = slowa_input.index('252')
        slowa_input[slowa_index_Y] = zbiór_znaków[32]

    while '629' in slowa_input:
        slowa_index_Z = slowa_input.index('629')
        slowa_input[slowa_index_Z] = zbiór_znaków[33]

    while '801' in slowa_input:
        slowa_index_Ż = slowa_input.index('801')
        slowa_input[slowa_index_Ż] = zbiór_znaków[34]

    while '664' in slowa_input:
        slowa_index_Ź = slowa_input.index('664')
        slowa_input[slowa_index_Ź] = zbiór_znaków[35]

    output = ''
    for char in slowa_input:
        output += char
    print (output)