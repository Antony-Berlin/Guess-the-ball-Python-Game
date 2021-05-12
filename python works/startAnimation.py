import time,sys,os

def starting_animation():

    load_str = 'starting your "guess the ball" game... '
    ls_len =len(load_str)

    animation ="|/-\\"
    frame_count = 0

    count_time = 0
    i = 0
    while(count_time!=100):
        
        load_str_list = list(load_str)

        x = load_str_list[i]
        y = 0

        if x!="." and x!='"':
            if x.islower():
                y = x.upper()
            else:
                y = x.lower()
            load_str_list[i] = y
        
        res = ""
        for j in range(ls_len):
            res = res + load_str_list[j]
        
        sys.stdout.write("\r"+res+animation[frame_count])
        time.sleep(0.08)
        sys.stdout.flush()

        load_str = res
        frame_count = (frame_count+1) % 4
        i = (i+1) % ls_len
        count_time += 1
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")