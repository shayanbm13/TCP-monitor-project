import subprocess
import socket
import re
from server_tcp import get_local_IP  



def get_default_gateway_windows():
   
    gateway_list=[]
    try:
        output = subprocess.check_output("ipconfig", shell=True).decode("utf-8")
        for line in output.splitlines():
            if "Default Gateway" in line:
                
                gateway = line.split(":")[1].strip()
                if gateway.startswith("192.168") :
                    gateway_list.append(gateway)
                
                
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        return None
    return gateway_list




def find_ethernet_name():
        
    command_output = subprocess.run(['netsh', 'interface', 'ipv4', 'show', 'interfaces'], capture_output=True, text=True)
    output_lines = command_output.stdout.splitlines()

    ethernet_names = []
    # ethernet_names = re.findall(r'\bEthernet\b.*$', output, flags=re.MULTILINE)

    for line in output_lines:

        if 'Ethernet' in line:
            print("111")
            # جستجوی نام اترنت با استفاده از regex
            match = re.search(r'(\d+)\s+disconnected\s+(Ethernet(?: \d*)?)', line)
            if match:
                ethernet_names.append(match.group(2).strip())  # افزودن نام به لیست

    return ethernet_names



def set_static_ip():
    current_ip= get_local_IP()
    net_name=find_ethernet_name()
    my_gateway= get_default_gateway_windows()[0]
    my_gateway_parts= str(my_gateway).split(".")
    
    if int(my_gateway_parts[3]) < 254 :
        current_static_ip = my_gateway_parts[0]+"."+my_gateway_parts[1]+"."+my_gateway_parts[2]+"."+str(int(my_gateway_parts[3])+1)
    elif int(my_gateway_parts[3]) >= 254 :
        current_static_ip = my_gateway_parts[0]+"."+my_gateway_parts[1]+"."+my_gateway_parts[2]+"."+str(int(my_gateway_parts[3])-1)
    print(current_static_ip)
    for ethernet in net_name :
        
        print(current_ip , ethernet,get_default_gateway_windows()[0])
        # netsh interface ipv4 set address name=Ethernet source=static address=192.168.1.5 mask=255.255.255.0 gateway=192.168.2.1
        command = f'netsh interface ipv4 set address name={ethernet} source=static address={current_static_ip} mask=255.255.255.0 gateway={get_default_gateway_windows()[0]}'

        # اجرای دستور
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()

        # چاپ خروجی و خطا اگر وجود داشته باشد
        if output:
            print(f"log: {output.decode('utf-8')}")
        if error:
            print(f"log: {error.decode('utf-8')}")


