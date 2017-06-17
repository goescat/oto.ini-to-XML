# coding=UTF-8
otofile = open("oto.ini", "r")
xmlfile = open("oto.xml", "w")

#xml 開始
xmlfile.write("<VoiceDictionary version=\"0.1\">\n")
#Syllables 開始
xmlfile.write("<Syllables>\n")


for line in otofile.readlines():
    #拿掉 ";" 開頭的註解
    ch = line[0]
    if ch == ";":
        pass
    else:
        #非空行
        if line.split():
            line = line.replace("=",",")
            line.rstrip()
            xmlfile = open("oto.xml", "a")
            #xmlfile.write(line)
            phonemes = line.split(",")[0].split(".")
            xmlfile.write("<Syllable alias=\""+line.split(",")[1]+"\">\n")
            xmlfile.write("<Phonemes>"+phonemes[0].lower()+"</Phonemes>\n</Syllable>\n")
        else:
            pass

xmlfile.close
otofile.close

xmlfile = open("oto.xml", "a")

#Syllables 結束，Fragments 開始
xmlfile.write("</Syllables>\n<Fragments>\n")
xmlfile.close

otofile = open("oto.ini", "r")

for line in otofile.readlines():
    ch = line[0]
    if ch == ";":
        pass
    else:
        if line.split():
            line = line.replace("=",",")
            line.rstrip()
            xmlfile = open("oto.xml", "a")
            phonemes = line.split(",")[0].split(".")
            xmlfile.write("<Fragment phonemes=\""+phonemes[0].lower()+"\" pitch=\"F4\">\n")
            xmlfile.write("<FileName>"+line.split(",")[0]+"</FileName>\n")
            xmlfile.write("<Length>"+line.split(",")[2]+"</Length>\n")
            xmlfile.write("<StartTime>"+line.split(",")[3]+"</StartTime>\n")
            xmlfile.write("<FixedRange>\n<Length>"+line.split(",")[4]+"</Length>\n")
            xmlfile.write("<Overlap>"+line.split(",")[6].rstrip()+"</Overlap>\n")
            xmlfile.write("<Preceding>"+line.split(",")[5]+"</Preceding>\n</FixedRange>\n</Fragment>\n")
        else:
            pass

otofile.close()
xmlfile.close()

#xml 結束
xmlfile = open("oto.xml", "a")
xmlfile.write("</Fragments>\n")
xmlfile.write("</VoiceDictionary>")
xmlfile.close()
