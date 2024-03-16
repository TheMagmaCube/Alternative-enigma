# Skrypt na kodowanie alfabetu polskiego poprzez liczby trzycyfrowe.





#                0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38
zbiór_znaków = ['0','a','ą','b','c','ć','d','e','ę','f','g','h','i','j','k','l','ł','m','n','ń','o','ó','p','q','r','s','ś','t','u','v','w','x','y','z','ż','ź',' ',',','.']


#                      
zakodowany_zbiór_znaków = ['0','223','644','291','608','536','970','626','147','154','505','251','570','905','365','354','512','749','675','616','199','583','384','577','211','293','341','678','213','151','307','703','252','629','801','664','817','404','774']




while 1>0:
    slowa_input = []
    slowa_user_input =  str(input ('Wpisz tekst do zakodowania:'))
    for char in slowa_user_input:
        slowa_input.append(char)



    while 'a' in slowa_input:
        slowa_index_a = slowa_input.index('a')
        slowa_input[slowa_index_a] = zakodowany_zbiór_znaków[1]

    while 'ą' in slowa_input:
        slowa_index_ą = slowa_input.index('ą')
        slowa_input[slowa_index_ą] = zakodowany_zbiór_znaków[2]
    
    while 'b' in slowa_input:
        slowa_index_b = slowa_input.index('b')
        slowa_input[slowa_index_b] = zakodowany_zbiór_znaków[3]

    while 'c' in slowa_input:
        slowa_index_c = slowa_input.index('c')
        slowa_input[slowa_index_c] = zakodowany_zbiór_znaków[4]

    while 'ć' in slowa_input:
        slowa_index_ć = slowa_input.index('ć')
        slowa_input[slowa_index_ć] = zakodowany_zbiór_znaków[5]

    while 'd' in slowa_input:
        slowa_index_d = slowa_input.index('d')
        slowa_input[slowa_index_d] = zakodowany_zbiór_znaków[6]
    
    while 'e' in slowa_input:
        slowa_index_e = slowa_input.index('e')
        slowa_input[slowa_index_e] = zakodowany_zbiór_znaków[7]

    while 'ę' in slowa_input:
        slowa_index_ę = slowa_input.index('ę')
        slowa_input[slowa_index_ę] = zakodowany_zbiór_znaków[8]

    while 'f' in slowa_input:
        slowa_index_f = slowa_input.index('f')
        slowa_input[slowa_index_f] = zakodowany_zbiór_znaków[9]

    while 'g' in slowa_input:
        slowa_index_g = slowa_input.index('g')
        slowa_input[slowa_index_g] = zakodowany_zbiór_znaków[10]

    while 'h' in slowa_input:
        slowa_index_h = slowa_input.index('h')
        slowa_input[slowa_index_h] = zakodowany_zbiór_znaków[11]

    while 'i' in slowa_input:
        slowa_index_i = slowa_input.index('i')
        slowa_input[slowa_index_i] = zakodowany_zbiór_znaków[12]

    while 'j' in slowa_input:
        slowa_index_j = slowa_input.index('j')
        slowa_input[slowa_index_j] = zakodowany_zbiór_znaków[13]

    while 'k' in slowa_input:
        slowa_index_k = slowa_input.index('k')
        slowa_input[slowa_index_k] = zakodowany_zbiór_znaków[14]

    while 'l' in slowa_input:
        slowa_index_l = slowa_input.index('l')
        slowa_input[slowa_index_l] = zakodowany_zbiór_znaków[15]

    while 'ł' in slowa_input:
        slowa_index_ł = slowa_input.index('ł')
        slowa_input[slowa_index_ł] = zakodowany_zbiór_znaków[16]

    while 'm' in slowa_input:
        slowa_index_m = slowa_input.index('m')
        slowa_input[slowa_index_m] = zakodowany_zbiór_znaków[17]
    
    while 'n' in slowa_input:
        slowa_index_n = slowa_input.index('n')
        slowa_input[slowa_index_n] = zakodowany_zbiór_znaków[18]
    
    while 'ń' in slowa_input:
        slowa_index_ń = slowa_input.index('ń')
        slowa_input[slowa_index_ń] = zakodowany_zbiór_znaków[19]

    while 'o' in slowa_input:
        slowa_index_o = slowa_input.index('o')
        slowa_input[slowa_index_o] = zakodowany_zbiór_znaków[20]

    while 'ó' in slowa_input:
        slowa_index_ó = slowa_input.index('ó')
        slowa_input[slowa_index_ó] = zakodowany_zbiór_znaków[21]

    while 'p' in slowa_input:
        slowa_index_p = slowa_input.index('p')
        slowa_input[slowa_index_p] = zakodowany_zbiór_znaków[22]

    while 'q' in slowa_input:
        slowa_index_q = slowa_input.index('q')
        slowa_input[slowa_index_q] = zakodowany_zbiór_znaków[23]

    while 'r' in slowa_input:
        slowa_index_r = slowa_input.index('r')
        slowa_input[slowa_index_r] = zakodowany_zbiór_znaków[24]

    while 's' in slowa_input:
        slowa_index_s = slowa_input.index('s')
        slowa_input[slowa_index_s] = zakodowany_zbiór_znaków[25]

    while 'ś' in slowa_input:
        slowa_index_ś = slowa_input.index('ś')
        slowa_input[slowa_index_ś] = zakodowany_zbiór_znaków[26]
    
    while 't' in slowa_input:
        slowa_index_t = slowa_input.index('t')
        slowa_input[slowa_index_t] = zakodowany_zbiór_znaków[27]

    while 'u' in slowa_input:
        slowa_index_u = slowa_input.index('u')
        slowa_input[slowa_index_u] = zakodowany_zbiór_znaków[28]

    while 'v' in slowa_input:
        slowa_index_v = slowa_input.index('v')
        slowa_input[slowa_index_v] = zakodowany_zbiór_znaków[29]

    while 'w' in slowa_input:
        slowa_index_w = slowa_input.index('w')
        slowa_input[slowa_index_w] = zakodowany_zbiór_znaków[30]

    while 'x' in slowa_input:
        slowa_index_x = slowa_input.index('x')
        slowa_input[slowa_index_x] = zakodowany_zbiór_znaków[31]

    while 'y' in slowa_input:
        slowa_index_y = slowa_input.index('y')
        slowa_input[slowa_index_y] = zakodowany_zbiór_znaków[32]

    while 'z' in slowa_input:
        slowa_index_z = slowa_input.index('z')
        slowa_input[slowa_index_z] = zakodowany_zbiór_znaków[33]

    while 'ż' in slowa_input:
        slowa_index_ż = slowa_input.index('ż')
        slowa_input[slowa_index_ż] = zakodowany_zbiór_znaków[34]

    while 'ź' in slowa_input:
        slowa_index_ź = slowa_input.index('ź')
        slowa_input[slowa_index_ź] = zakodowany_zbiór_znaków[35]

    while ' ' in slowa_input:
        slowa_index__ = slowa_input.index(' ')
        slowa_input[slowa_index__] = zakodowany_zbiór_znaków[36]
    
    while ',' in slowa_input:
        slowa_index_1 = slowa_input.index(',')
        slowa_input[slowa_index_1] = zakodowany_zbiór_znaków[37]

    while '.' in slowa_input:
        slowa_index_dot = slowa_input.index('.')
        slowa_input[slowa_index_dot] = zakodowany_zbiór_znaków[38]

    while 'A' in slowa_input:
        slowa_index_A = slowa_input.index('A')
        slowa_input[slowa_index_A] = zakodowany_zbiór_znaków[1]
    
    while 'Ą' in slowa_input:
        slowa_index_Ą = slowa_input.index('Ą')
        slowa_input[slowa_index_Ą] = zakodowany_zbiór_znaków[2]
    
    while 'B' in slowa_input:
        slowa_index_B = slowa_input.index('B')
        slowa_input[slowa_index_B] = zakodowany_zbiór_znaków[3]
    
    while 'C' in slowa_input:
        slowa_index_C = slowa_input.index('C')
        slowa_input[slowa_index_C] = zakodowany_zbiór_znaków[4]

    while 'Ć' in slowa_input:
        slowa_index_Ć = slowa_input.index('Ć')
        slowa_input[slowa_index_Ć] = zakodowany_zbiór_znaków[5]
    
    while 'D' in slowa_input:
        slowa_index_D = slowa_input.index('D')
        slowa_input[slowa_index_D] = zakodowany_zbiór_znaków[6]
    
    while 'E' in slowa_input:
        slowa_index_E = slowa_input.index('E')
        slowa_input[slowa_index_E] = zakodowany_zbiór_znaków[7]

    while 'Ę' in slowa_input:
        slowa_index_Ę = slowa_input.index('Ę')
        slowa_input[slowa_index_Ę] = zakodowany_zbiór_znaków[8]

    while 'F' in slowa_input:
        slowa_index_F = slowa_input.index('F')
        slowa_input[slowa_index_F] = zakodowany_zbiór_znaków[9]
    
    while 'G' in slowa_input:
        slowa_index_G = slowa_input.index('G')
        slowa_input[slowa_index_G] = zakodowany_zbiór_znaków[10]

    while 'H' in slowa_input:
        slowa_index_H = slowa_input.index('H')
        slowa_input[slowa_index_H] = zakodowany_zbiór_znaków[11]

    while 'I' in slowa_input:
        slowa_index_I = slowa_input.index('I')
        slowa_input[slowa_index_I] = zakodowany_zbiór_znaków[12]

    while 'J' in slowa_input:
        slowa_index_J = slowa_input.index('J')
        slowa_input[slowa_index_J] = zakodowany_zbiór_znaków[13]

    while 'K' in slowa_input:
        slowa_index_K = slowa_input.index('K')
        slowa_input[slowa_index_K] = zakodowany_zbiór_znaków[14]

    while 'L' in slowa_input:
        slowa_index_L = slowa_input.index('L')
        slowa_input[slowa_index_L] = zakodowany_zbiór_znaków[15]

    while 'Ł' in slowa_input:
        slowa_index_Ł = slowa_input.index('Ł')
        slowa_input[slowa_index_Ł] = zakodowany_zbiór_znaków[16]

    while 'M' in slowa_input:
        slowa_index_M = slowa_input.index('M')
        slowa_input[slowa_index_M] = zakodowany_zbiór_znaków[17]

    while 'N' in slowa_input:
        slowa_index_N = slowa_input.index('N')
        slowa_input[slowa_index_N] = zakodowany_zbiór_znaków[18]

    while 'Ń' in slowa_input:
        slowa_index_Ń = slowa_input.index('Ń')
        slowa_input[slowa_index_Ń] = zakodowany_zbiór_znaków[19]

    while 'O' in slowa_input:
        slowa_index_O = slowa_input.index('O')
        slowa_input[slowa_index_O] = zakodowany_zbiór_znaków[20]

    while 'Ó' in slowa_input:
        slowa_index_Ó = slowa_input.index('Ó')
        slowa_input[slowa_index_Ó] = zakodowany_zbiór_znaków[21]

    while 'P' in slowa_input:
        slowa_index_P = slowa_input.index('P')
        slowa_input[slowa_index_P] = zakodowany_zbiór_znaków[22]

    while 'Q' in slowa_input:
        slowa_index_Q = slowa_input.index('Q')
        slowa_input[slowa_index_Q] = zakodowany_zbiór_znaków[23]

    while 'R' in slowa_input:
        slowa_index_R = slowa_input.index('R')
        slowa_input[slowa_index_R] = zakodowany_zbiór_znaków[24]

    while 'S' in slowa_input:
        slowa_index_S = slowa_input.index('S')
        slowa_input[slowa_index_S] = zakodowany_zbiór_znaków[25]

    while 'Ś' in slowa_input:
        slowa_index_Ś = slowa_input.index('Ś')
        slowa_input[slowa_index_Ś] = zakodowany_zbiór_znaków[26]

    while 'T' in slowa_input:
        slowa_index_T = slowa_input.index('T')
        slowa_input[slowa_index_T] = zakodowany_zbiór_znaków[27]

    while 'U' in slowa_input:
        slowa_index_U = slowa_input.index('U')
        slowa_input[slowa_index_U] = zakodowany_zbiór_znaków[28]

    while 'V' in slowa_input:
        slowa_index_V = slowa_input.index('V')
        slowa_input[slowa_index_V] = zakodowany_zbiór_znaków[29]

    while 'W' in slowa_input:
        slowa_index_W = slowa_input.index('W')
        slowa_input[slowa_index_W] = zakodowany_zbiór_znaków[30]

    while 'X' in slowa_input:
        slowa_index_X = slowa_input.index('X')
        slowa_input[slowa_index_X] = zakodowany_zbiór_znaków[31]

    while 'Y' in slowa_input:
        slowa_index_Y = slowa_input.index('Y')
        slowa_input[slowa_index_Y] = zakodowany_zbiór_znaków[32]

    while 'Z' in slowa_input:
        slowa_index_Z = slowa_input.index('Z')
        slowa_input[slowa_index_Z] = zakodowany_zbiór_znaków[33]

    while 'Ż' in slowa_input:
        slowa_index_Ż = slowa_input.index('Ż')
        slowa_input[slowa_index_Ż] = zakodowany_zbiór_znaków[34]

    while 'Ź' in slowa_input:
        slowa_index_Ź = slowa_input.index('Ź')
        slowa_input[slowa_index_Ź] = zakodowany_zbiór_znaków[35]
    output = ''
    for char in slowa_input:
        output += char
    print (output)
