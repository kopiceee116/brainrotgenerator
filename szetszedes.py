def darabol(text: str, words: list) -> str:
    characters = ["?", "!", ".", ",", ";", ":", "-"]
    text = makeNewLines(text, characters)
    textv2 = ""
    first_line_processed = False  # track first line
    for line in text.split("\n"):
        new_line = f"{breakLongLine(line, words)}\n"
        if new_line:
            if not first_line_processed:
                if new_line.count(" ") > 7:
                    middleLine = line[(len(line)//5)*2:(len(line)//5)*4]
                    whereToPutNewLine = middleLine.find(" ")+((len(line)//5)*2)
                    textv2 += line[:whereToPutNewLine] + "\n"
                    textv2 += line[whereToPutNewLine:] + "\n"
                else:
                    textv2 += line + "\n"  # Add the original first line
                first_line_processed = True
            else:
                textv2 += new_line
        
    return removeSmallRow(textv2)


def makeNewLines(text: str, characterstoreplace :list) -> str:
    for character in characterstoreplace:
        text = text.replace(character,f"{character}\n")
    return text

def breakLongLine(line: str,words :list) -> str:
    lenline = len(line)
    wordpositions = []
    if line.count(" ") < 7:
        return line
    else:
        middleLine = line[(lenline//5)*2:(lenline//5)*4]
        whereToPutNewLine = middleLine.find(" ")+((lenline//5)*2)
        returnline = ""
        for character in range(lenline):
            if character == whereToPutNewLine:
                returnline += "\n"
            returnline+= line[character]
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


def szetszedes(nev,words) -> str:
    szoveg = kiszedafajlbol(nev)
    keszFajlNev = "split.txt"
    print(szoveg)
    with open(keszFajlNev,"w",encoding="utf-8") as fajl:
        print(darabol(szoveg,words),file=fajl)
    return keszFajlNev

