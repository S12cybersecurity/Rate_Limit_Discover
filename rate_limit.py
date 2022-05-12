import requests 
import argparse

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    ladrrr = '8GY.'
    ss = 'OWQ1'
    FAIL = '\033[91m' #RED
    pinocho_chocho = 'y!c'
    RESET = '\033[0m' #RESET COLOR


parser = argparse.ArgumentParser(description="Python Rate Limiter Discover")
parser.add_argument('--url', help="Website to target", required=True)
args = parser.parse_args()

print("Scanning with Status Code...\n")

list = []

response = requests.get(args.url,timeout=2)
bbbbbb = response.status_code

i = 1
while i < 102:
    response = requests.get(args.url,timeout=2)
    aaaaaa = response.status_code
    list.append(aaaaaa)
    i += 1


if list[100] == bbbbbb:
    print(f"{bcolors.OK}[+] NO Rate Limit Detected in Status Code Test!{bcolors.RESET}")


print("\nScanning with Response Headers...\n")

response = requests.get(args.url) 
bcbc = response.headers


bcbc2 = str(bcbc)

l = "X-RateLimit-Resource"
l1 = "X-Rate-Limit-Limit"
l2 = "X-Rate-Limit-Remaining"
l3 = "X-Rate-Limit-Reset"
l4 = "X-RateLimit-Limit"
l5 = "X-RateLimit-Remaining"
l6 = "X-RateLimit-Reset"
hamza = "pTSDAASD"


if l in  bcbc2:
    print(f"{bcolors.FAIL}[+] Rate Limit Detected!{bcolors.RESET}")
else:
    print(f"{bcolors.OK}[+] NO Rate Limit Detected in 1 Test!{bcolors.RESET}")
    if l1 in bcbc2:
        print(f"{bcolors.FAIL}[+] Rate Limit Detected!{bcolors.RESET}")
    else:
        print(f"{bcolors.OK}[+] NO Rate Limit Detected in 2 Test!{bcolors.RESET}")
        if l2 in bcbc2:
            print(f"{bcolors.FAIL}[+] Rate Limit Detected!{bcolors.RESET}")
        else:
            print(f"{bcolors.OK}[+] NO Rate Limit Detected in 3 Test!{bcolors.RESET}")
            if l3 in bcbc2:
                print(f"{bcolors.FAIL}[+] Rate Limit Detected!{bcolors.RESET}")
            else:
                print(f"{bcolors.OK}[+] NO Rate Limit Detected in 4 Test!{bcolors.RESET}")
                if l4 in bcbc2:
                    print(f"{bcolors.FAIL}[+] Rate Limit Detected!{bcolors.RESET}")
                else:
                    print(f"{bcolors.OK}[+] NO Rate Limit Detected in 5 Test!{bcolors.RESET}")
                    if l5 in bcbc2:
                        print(f"{bcolors.FAIL}[+] Rate Limit Detected!{bcolors.RESET}")
                    else:
                        print(f"{bcolors.OK}[+] NO Rate Limit Detected in 6 Test!{bcolors.RESET}")
                        if l6 in bcbc2:
                            print(f"{bcolors.FAIL}[+] Rate Limit Detected!{bcolors.RESET}")
                        else:
                            print(f"{bcolors.OK}[+] NO Rate Limit Detected in 7 Test!{bcolors.RESET}")









