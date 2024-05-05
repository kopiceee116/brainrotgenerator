def darabol(text :str) -> str:
    characters = ["?","!",".",",",";",":","-"]
    text = makeNewLines(text,characters)
    textv2 = ""
    for line in text.split("\n"):
        new_line = f"{breakLongLine(line)}\n"
        if new_line:
            if new_line[0] == " ":
                new_line = new_line[1:]
                textv2 += (new_line)
        
    return removeSmallRow(textv2)

def makeNewLines(text: str, characterstoreplace :list) -> str:
    for character in characterstoreplace:
        text = text.replace(character,f"{character}\n")
    return text

def breakLongLine(line: str) -> str:
    words = ["und", "sondern", "oder", "dann", "aber", "trotzdem", "weil", "ob", "obwohl", "denn", "dass"]
    lenline = len(line)
    wordpositions = []
    if line.count(" ") < 10:
        return line
    else:
        returnline = ""
        for word in words:
            if line.find(word):
                wordpositions.append(line.find(word))
            else:
                wordpositions.append(0)
        for i in range(len(wordpositions)):
            if wordpositions[i] > lenline*0.75 or wordpositions[i] < lenline*0.25:
                wordpositions[i] == 0
        returnline += f"{line[0:max(wordpositions)]}\n"
        returnline += f"{line[max(wordpositions):]}"
        return returnline

def removeSmallRow(text :str) -> str:
    splittext = text.split("\n")
    for line in range(len(splittext)):
        if len(splittext[line])< 3:
            splittext[line-1] += splittext[line]
            splittext[line] == 0
    bigtext = ""
    for i in splittext:
        print(i)
        if len(i) > 1:
            bigtext += i
            bigtext += "\n"
    return bigtext

def kiszedafajlbol(nev :str) -> str:
    with open(nev,"r",encoding="utf-8") as kiszed:
        return kiszed.read()


def szetszedes(nev) -> str:
    szoveg = kiszedafajlbol(nev)
    keszFajlNev = "split.txt"
    print(szoveg)
    with open(keszFajlNev,"w",encoding="utf-8") as fajl:
        print(darabol(szoveg),file=fajl)
    return keszFajlNev

