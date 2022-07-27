__USER__: str  = "moonl1ght01 AKA Py-Moon"
__VERSION__: str = "0.5"
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
        print(f"{Fore.RED}ProxyScraper v{__VERSION__} by {__USER__}")
        
        try: 
            print(f"{Fore.BLUE}Create PATH for Proxy List...")
            mkdir(r"ProxyLists/")
            mkdir(r"ProxyLists/SortedProxyLists/")
            print(f"{Fore.GREEN}PATH CREATED SUCCESSFULLY!")
        except FileExistsError:
            print(f"{Fore.GREEN}PATH ALTREDY EXISTS")
        
        
        self.payload={}
        self.headers = {}     
        
        self.URLHTTP: str = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"
        self.URLSOCKS5: str = "https://api.proxyscrape.com/v2/?request=displayproxies&proxytype=socks5&timeout=10000&country=all&ssl=all&anonymity=all"
        
        self.GET_PROXYLIST()
        print(f"{Fore.GREEN} PROXY LIST CREATED SUCCESSFULLY! ( AND SAVED IN FILE )")
        
        print(f"{Fore.LIGHTMAGENTA_EX} HTTP PROXY:\n {self.GET_HTTPPROXY()}")
        print(f"{Fore.LIGHTYELLOW_EX} SOCKS4/5 PROXY:\n {self.GET_SOCKS5PROXY()}")
        
        print(f"""
{Fore.LIGHTMAGENTA_EX}COLOR HTTP PROXY {Fore.LIGHTMAGENTA_EX}
{Fore.LIGHTYELLOW_EX}COLOR SOCKS 4/5 PROXY {Fore.LIGHTYELLOW_EX}
""")
        print(f"{Fore.RED}ProxyScraper v{__VERSION__} by {__USER__}")

    def GET_HTTPPROXY(self) -> str:
        response = requests.request("GET", self.URLHTTP, headers=self.payload, data=self.payload)
        return response.text   
    
    def GET_SOCKS5PROXY(self) -> str:
        response = requests.request("GET", self.URLSOCKS5, headers=self.payload, data=self.payload)
        return response.text
    
    def GET_PROXYLIST(self) -> list:
        list: list = []
        list.append(self.GET_HTTPPROXY())
        list.append(self.GET_SOCKS5PROXY())
        
        with open("ProxyLists/ProxyList.txt", "w") as file:
            file.writelines(list)
            file.close()

        with open(r"ProxyLists/SortedProxyLists/HTTP_PROXY.txt", "w") as file:
            file.write(self.GET_HTTPPROXY())
            file.close()
            
        with open(r"ProxyLists/SortedProxyLists/SOCKS4-5_PROXY.txt", "w") as file:
            file.write(self.GET_SOCKS5PROXY())
            file.close()
        return list
    
if __name__ == '__main__':
    App()
