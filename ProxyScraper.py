__USER__: str  = "moonl1ght01"
__VERSION__: str = "0.1"
__DATE__: str = "27-07-2022"

from os import system
from os import mkdir

try:
    from colorama import Fore
    import requests
except ImportError:
    system('python -m pip install colorama, requests')  

class App:    
    def __init__(self) -> None:
        try: 
            print("Create PATH for Proxy List...")
            mkdir("ProxyLists")
            print("PATH CREATED SUCCESSFULLY!")
        except FileExistsError:
            print("PATH ALTREDY EXISTS")
        
        
        self.payload={}
        self.headers = {}     
        
        self.URLHTTP: str = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=10000&country=all&ssl=all&anonymity=all"
        self.URLSOCKS4: str = "https://api.proxyscrape.com/v2/?request=displayproxies&proxytype=socks4&timeout=10000&country=all&ssl=all&anonymity=all"
        self.URLSOCKS5: str = "https://api.proxyscrape.com/v2/?request=displayproxies&proxytype=socks5&timeout=10000&country=all&ssl=all&anonymity=all"
        
        print(self.GET_HTTPPROXY())
           
    def GET_HTTPPROXY(self) -> str:
        response = requests.request("GET", self.URLHTTP, headers=self.payload, data=self.payload)
        return response.text   
     
    def GET_SOCKS4PROXY(self) -> str:

        response = requests.request("GET", self.URLSOCKS4, headers=self.payload, data=self.payload)
        return response.text    
    
    def GET_SOCKS5PROXY(self) -> str:
        response = requests.request("GET", self.URLSOCKS5, headers=self.payload, data=self.payload)
        return response.text
    
    def GET_PROXYLIST(self) -> list:
        list: list = []
        list.append("HTTP PROXY:\n" + self.GET_HTTPPROXY() + "\n")
        list.append("SOCKS4 PROXY:\n" + self.GET_SOCKS5PROXY() + "\n")
        list.append("SOKS5 PROXY:\n" + self.GET_SOCKS5PROXY() + "\n")
        
        with open("ProxyLists/ProxyList.txt", "w") as file:
            file.writelines(list)    
        return list
    
if __name__ == '__main__':
    App()
