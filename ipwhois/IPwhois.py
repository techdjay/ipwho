import sys
import json
from requests import get
from json import dumps

def ipwhois(ip4:str) -> str:
    url = "https://ipwhois.app/json/%s" % (ip4)
    try:
        req = get(url).json()
        parsed_data = {
            "IP": req["ip"],
            "Organization": req["org"],
            "ISP": req["isp"]
        }
        formatted_output = "\n".join([f"{key}: {value}" for key, value in parsed_data.items()])
        return formatted_output
    except:
        return "Check your internet connection!"

def main():
    if len(sys.argv) > 1:
        ip_address = sys.argv[1]
        print(ipwhois(ip_address))
    else:
        while True:
            print("type quit/exit to exit the program\n")
            data = input("ip4 > ")
            if not data:
                print(ipwhois("0"))
            elif data in ["quit", "exit"]:
                print("user quit :)")
                break
            else:
                print(ipwhois(data))
