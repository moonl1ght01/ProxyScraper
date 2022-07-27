__USER__: str  = "moonl1ght01"
__VERSION__: str = "0.1"
__DATE__: str = "27-07-2022"

from os import system
from os import mkdir

try:
    from colorama import Fore, init
    import requests
except ImportError:
    system('python -m pip install colorama, requests')  
init(autoreset=True)
class App:    
    def __init__(self) -> None:
        print(f"{Fore.LIGHTGREEN_EX}ProxyScraper v{__VERSION__} by {__USER__}")
        
        try: 
            print(f"{Fore.BLUE}Create PATH for Proxy List...")
            mkdir("ProxyLists")
            print(f"{Fore.GREEN}PATH CREATED SUCCESSFULLY!")
        except FileExistsError:
            print(f"{Fore.GREEN}PATH ALTREDY EXISTS")
        
        
        self.payload={}
        self.headers = {}     
        
        self.URLHTTP: str = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all&timeout=10000&country=all&ssl=all&anonymity=all"
        self.URLSOCKS4: str = "https://api.proxyscrape.com/v2/?request=displayproxies&proxytype=socks4&timeout=10000&country=all&ssl=all&anonymity=all"
        self.URLSOCKS5: str = "https://api.proxyscrape.com/v2/?request=displayproxies&proxytype=socks5&timeout=10000&country=all&ssl=all&anonymity=all"
        
        self.GET_PROXYLIST()
        print(f"{Fore.GREEN} PROXY LIST CREATED SUCCESSFULLY! ( AND SAVED IN FILE )")
        
        print(f"{Fore.LIGHTMAGENTA_EX} HTTP PROXY:\n {self.GET_HTTPPROXY()}")
        print(f"{Fore.LIGHTYELLOW_EX} SOCKS4 PROXY:\n {self.GET_SOCKS4PROXY()}")
        print(f"{Fore.LIGHTCYAN_EX} SOKS5 PROXY:\n {self.GET_SOCKS5PROXY()}")
        
        print(f"""
{Fore.LIGHTMAGENTA_EX}COLOR HTTP PROXY: {Fore.LIGHTMAGENTA_EX}
{Fore.LIGHTYELLOW_EX}COLOR SOCKS4 PROXY: {Fore.LIGHTYELLOW_EX}
{Fore.LIGHTCYAN_EX}COLOR SOCKS5 PROXY: {Fore.LIGHTCYAN_EX}
""")
        print(f"{Fore.LIGHTGREEN_EX}ProxyScraper v{__VERSION__} by {__USER__}")

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
        list.append(f"{Fore.LIGHTMAGENTA_EX}HTTP PROXY:\n" + self.GET_HTTPPROXY() + "\n")
        list.append(f"{Fore.LIGHTYELLOW_EX}SOCKS4 PROXY:\n" + self.GET_SOCKS5PROXY() + "\n")
        list.append(f"{Fore.LIGHTCYAN_EX}SOKS5 PROXY:\n" + self.GET_SOCKS5PROXY() + "\n")
        
        with open("ProxyLists/ProxyList.txt", "w") as file:
            file.writelines(list)    
        return list
    
if __name__ == '__main__':
    App()
