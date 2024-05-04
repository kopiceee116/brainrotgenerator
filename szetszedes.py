def szetszed(text :str) -> str:
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
            if wordpositions[i] > lenline*0.75:
                wordpositions[i] == 0
        returnline += f"{line[0:max(wordpositions)]}\n"
        returnline += f"{line[max(wordpositions):]}"
        return returnline

def removeSmallRow(text):
    splittext = [text.split("\n")]
    for line in range(len(splittext)):
        if len(splittext[line])< 3:
            splittext[line-1] += splittext[line]
            splittext[line] == 0
    bigtext = ""
    for i in splittext[0]:
        print(i)
        if len(i) > 1:
            bigtext += i
            bigtext += "\n"
    return bigtext

    
szoveg = """Bida wenn ich auf meine Pause bestehe?Hey, ich hab folgendes Thema und dazu die Frage Bida?Ich arbeite seit einer Zeit in einem großen Unternehmen. Die Nachtschicht Pause wird durchbezahlt, deswegen beschwer ich mich nicht, wenn ich meine Pause unterbrechen muss oder sonst was. Während der Früh oder Spätschicht in normalerweise noch jemand in der Tag Schicht da, der die Pausen der beiden Schichten übernimmt.Das funktioniert nur solange bis jemand krank ist oder im Urlaub ist. Dann muss ich jemanden suchen der meine Pause übernimmt. Dann hat mal die erste Person viel zutun und kann nicht, die zweite evtl auch und dann geht's hin und her bis jemand dann doch Zeit hat zum übernehmen.Das geht dann jeden Tag so, das ich hin und her laufe und aktiv suchen muss wer mich solange vertritt. Wenn ich niemanden Frage, kann ich auch keine Pause machen, da die Maschinellen Abläufe hier auf mein handeln angewiesen sind. Mir kommt es vor als würde ich denjenigen auf den Sack gehen mit meiner Pause. Alle machen ihre Pause und müssen niemanden dafür einspringen lassen, bei mir geht es nicht anders. Bida wenn ich jeden Tag auf meine Pause bestehe?"""
with open("temp.txt","w",encoding="utf-8") as fajl:
    print(szetszed(szoveg),file=fajl)
