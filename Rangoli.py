def rangoli(size):
    
    alpha_list = list(map(chr,range(97,123)))
    mid_element = alpha_list[size-1::-1] + alpha_list[1:size]
    final_mid_element = "-".join(mid_element)
    width = len(final_mid_element)
    row_length = (size*2)-1
    flag = 0
    flag_l = 2
    for i in range(1,row_length+1):
        if(i==1 or i==row_length):
            print(alpha_list[size-1].center(width,"-"))
        elif(i==(row_length//2)+1):
            print(final_mid_element)
        elif(i<(row_length//2)+1):
            times = flag*1+2
            final = alpha_list[size-1:size-times:-1] + alpha_list[size-i:size]
            print('-'.join(final).center(width,"-"))
            flag += 1
        else:
            final = alpha_list[size-1:i-size-1:-1] + alpha_list[i-size+1:size]
            print('-'.join(final).center(width,"-"))
            
if __name__ == "__main__":
    n = int(input())
    rangoli(n)