import requests
from bs4 import BeautifulSoup
def szeddkiaszoveget(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    div_element = soup.find('div', class_='md max-h-[253px] overflow-hidden s:max-h-[318px] m:max-h-[337px] l:max-h-[352px] xl:max-h-[452px] text-14')
    h1_element = soup.find('h1')

    if h1_element and div_element:
        div_contents = div_element.text.strip()
        h1_contents = h1_element.text.strip()
        with open("saved.txt","w",encoding="utf-8") as fajl:
            fajl.write(f"{h1_contents} ")
            fajl.write(div_contents.replace("\n",""))
        return "siker"
    else:
        return "gatya"

szeddkiaszoveget("https://www.reddit.com/r/BinIchDasArschloch/comments/1cj2xa4/bida_wenn_ich_auf_meine_pause_bestehe/")