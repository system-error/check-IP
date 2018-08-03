import re

ip_input = input("Hello, give me an ip please: ")
ip_input = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",ip_input)
if ip_input !=None:
    ip_group = ip_input.group()
    ip = list(map(int,ip_group.split(".")))
    for checking in ip:
        if checking <= 255:
            continue
        else:
            print("false")
    for i in ip:
        ip_to_string = ''.join(i)
    print(ip_to_string)
else:
    print("Somethnig went wrong with the IP. Please check the IP")    
        

    # if ip_check==True:
    #     print("match")
    # else:
    #     print("not match")    