verbs = {}
verbs ["fiilA1sgFut"]=[]
verbs ["fiilA2sgFut"]=[]
verbs ["fiilA3sgFut"]=[]
verbs ["fiilA1sgPast"]=[]
verbs ["fiilA2sgPast"]=[]
verbs ["fiilA3sgPast"]=[]
verbs ["fiilA1plFut"]=[]
verbs ["fiilA2plFut"]=[]
verbs ["fiilA3plFut"]=[]
verbs ["fiilA1plPast"]=[]
verbs ["fiilA2plPast"]=[]
verbs ["fiilA3plPast"]=[]
verbs ["fiilA1sgElse"]=[]
verbs ["fiilA2sgElse"]=[]
verbs ["fiilA3sgElse"]=[]
verbs ["fiilA1sgElse"]=[]
verbs ["fiilA2sgElse"]=[]
verbs ["fiilA3sgElse"]=[]

verbs ["isimA1sgFut"]=[]
verbs ["isimA2sgFut"]=[]
verbs ["isimA3sgFut"]=[]
verbs ["isimA1sgPast"]=[]
verbs ["isimA2sgPast"]=[]
verbs ["isimA3sgPast"]=[]
verbs ["isimA1plFut"]=[]
verbs ["isimA2plFut"]=[]
verbs ["isimA3plFut"]=[]
verbs ["isimA1plPast"]=[]
verbs ["isimA2plPast"]=[]
verbs ["isimA3plPast"]=[]
verbs ["isimA1sgElse"]=[]
verbs ["isimA2sgElse"]=[]
verbs ["isimA3sgElse"]=[]
verbs ["isimA1sgElse"]=[]
verbs ["isimA2sgElse"]=[]
verbs ["isimA3sgElse"]=[]

adv = []
conj = []
adj = []
ques = []
det = []
postp=[]
noun={}
noun["no suffix"]=[]
noun["a|e"]=[]
noun["i"]=[]
noun["le|la"]=[]
noun["ler|lar"]=[]
noun["in"]=[]
noun["im"]=[]
noun["imiz"]=[]
noun["iniz"]=[]
noun["de|da"]=[]
noun["den|dan"]=[]
pron={}
pron["no suffix 1"]=[]
pron["no suffix 2"]=[]
pron["no suffix 3"]=[]
pron["no suffix 4"]=[]
pron["no suffix 5"]=[]
pron["no suffix 6"]=[]
pron["in"]=[]
pron["im"]=[]
pron["un"]=[]
pron["ce|ca"]=[]

with open("source.txt","r", encoding="utf-8") as file:
    for line in file:
        if "#text = " not in line:
            pair = line.strip().split("\t")
            pos = pair[0]
            word = pair[1]
            analysis = pair[2]
            if pos == "Conj":
                conj.append(word)
            elif pos == "Det":
                det.append(word)
            elif pos == "Adj" or pos == "Num":
                adj.append(word)
            elif pos == "Adv":
                adv.append(word)
            elif pos == "Verb":
                if "Zero→Verb" in analysis:
                    if "A1sg" in analysis and "Past" in analysis:
                        verbs["isimA1sgPast"].append(word)
                    elif "A2sg" in analysis and "Past" in analysis:
                        verbs["isimA2sgPast"].append(word)
                    elif "A3sg" in analysis and "Past" in analysis:
                        verbs["isimA3sgPast"].append(word)
                    elif "A1sg" in analysis and "Fut" in analysis:
                        verbs["isimA1sgFut"].append(word)
                    elif "A2sg" in analysis and "Fut" in analysis:
                        verbs["isimA2sgFut"].append(word)
                    elif "A3sg" in analysis and "Fut" in analysis:
                        verbs["isimA3sgFut"].append(word)
                    elif "A1pl" in analysis and "Past" in analysis:
                        verbs["isimA1plPast"].append(word)
                    elif "A2pl" in analysis and "Past" in analysis:
                        verbs["isimA2plPast"].append(word)
                    elif "A3pl" in analysis and "Past" in analysis:
                        verbs["isimA3plPast"].append(word)
                    elif "A1pl" in analysis and "Fut" in analysis:
                        verbs["isimA1plFut"].append(word)
                    elif "A2pl" in analysis and "Fut" in analysis:
                        verbs["isimA2plFut"].append(word)
                    elif "A3pl" in analysis and "Fut" in analysis:
                        verbs["isimA3plFut"].append(word)
                    elif "A1sg" in analysis:
                        verbs["isimA1sgElse"].append(word)
                    elif "A2sg" in analysis:
                        verbs["isimA2sgElse"].append(word)
                    elif "A3sg" in analysis:
                        verbs["isimA3sgElse"].append(word)
                    elif "A1pl" in analysis:
                        verbs["isimA1plElse"].append(word)
                    elif "A2pl" in analysis:
                        verbs["isimA2plElse"].append(word)
                    elif "A3pl" in analysis:
                        verbs["isimA3plElse"].append(word)
                else:
                    if "A1sg" in analysis and "Past" in analysis:
                        verbs["fiilA1sgPast"].append(word)
                    elif "A2sg" in analysis and "Past" in analysis:
                        verbs["fiilA2sgPast"].append(word)
                    elif "A3sg" in analysis and "Past" in analysis:
                        verbs["fiilA3sgPast"].append(word)
                    elif "A1sg" in analysis and "Fut" in analysis:
                        verbs["fiilA1sgFut"].append(word)
                    elif "A2sg" in analysis and "Fut" in analysis:
                        verbs["fiilA2sgFut"].append(word)
                    elif "A3sg" in analysis and "Fut" in analysis:
                        verbs["fiilA3sgFut"].append(word)
                    elif "A1pl" in analysis and "Past" in analysis:
                        verbs["fiilA1plPast"].append(word)
                    elif "A2pl" in analysis and "Past" in analysis:
                        verbs["fiilA2plPast"].append(word)
                    elif "A3pl" in analysis and "Past" in analysis:
                        verbs["fiilA3plPast"].append(word)
                    elif "A1pl" in analysis and "Fut" in analysis:
                        verbs["fiilA1plFut"].append(word)
                    elif "A2pl" in analysis and "Fut" in analysis:
                        verbs["fiilA2plFut"].append(word)
                    elif "A3pl" in analysis and "Fut" in analysis:
                        verbs["fiilA3plFut"].append(word)
                    elif "A1sg" in analysis:
                        verbs["fiilA1sgElse"].append(word)
                    elif "A2sg" in analysis:
                        verbs["fiilA2sgElse"].append(word)
                    elif "A3sg" in analysis:
                        verbs["fiilA3sgElse"].append(word)
                    elif "A1pl" in analysis:
                        verbs["fiilA1plElse"].append(word)
                    elif "A2pl" in analysis:
                        verbs["fiilA2plElse"].append(word)
                    elif "A3pl" in analysis:
                        verbs["fiilA3plElse"].append(word)
            elif pos == "Ques":
                ques.append(word)

            elif pos == "Postp":
                postp.append(word)

            elif pos == "Pron":
                if analysis.endswith("Pron+A1sg"):
                    pron["no suffix 1"].append(word)
                elif analysis.endswith("Pron+A2sg"):
                    pron["no suffix 2"].append(word)
                elif analysis.endswith("Pron+A3sg"):
                    pron["no suffix 3"].append(word)
                elif analysis.endswith("Pron+A1pl"):
                    pron["no suffix 4"].append(word)
                elif analysis.endswith("Pron+A2pl"):
                    pron["no suffix 5"].append(word)
                elif analysis.endswith("Pron+A3pl"):
                    pron["no suffix 6"].append(word)
                elif analysis.endswith("im:Gen"):
                    pron["im"].append(word)
                elif analysis.endswith("in:Gen"):
                    pron["in"].append(word)
                elif analysis.endswith("un:Gen"):
                    pron["un"].append(word)
                elif analysis.endswith("ce:Equ") or analysis.endswith("c:Equ"):
                    pron["ce|ca"].append(word)

            elif pos == "Noun":

                if analysis.endswith("Noun+A3sg"):
                    noun["no suffix"].append(word)

                elif analysis.endswith("Noun+lar:A3pl") or analysis.endswith("Noun+ler:A3pl"):
                    noun["ler|lar"].append(word)

                elif analysis.endswith("Acc") or analysis.endswith("P3sg"):
                    noun["i"].append(word)

                elif analysis.endswith("in:Gen") or analysis.endswith("ın:Gen") or analysis.endswith("un:Gen") or analysis.endswith("ün:Gen"):
                    noun["in"].append(word)

                elif analysis.endswith("im:Gen") or analysis.endswith("ım:Gen") or analysis.endswith("um:Gen") or analysis.endswith("üm:Gen"):
                    noun["im"].append(word)

                elif analysis.endswith("P2pl"):
                    noun["iniz"].append(word)

                elif analysis.endswith("P1pl"):
                    noun["imiz"].append(word)

                elif analysis.endswith("Dat"):
                    noun["a|e"].append(word)

                elif analysis.endswith("Ins"):
                    noun["le|la"].append(word)

                elif analysis.endswith("Abl"):
                    noun["den|dan"].append(word)

                elif analysis.endswith("Loc"):
                    noun["de|da"].append(word)




"""print(noun)
print(pron)
print(verbs)
print(list(set(adv)))
print(list(set(conj)))
print(list(set(adj)))
print(list(set(ques)))"""
yazil = []
for ix, val in enumerate(noun.keys()):
    if noun[val] != []:
        for elem in noun[val]:
            line = "N"+str(ix)+" -> "+ "'"+elem+ "'"
            yazil.append(line)

for ix, val in enumerate(pron.keys()):
    if pron[val] != []:
        for elem in pron[val]:
            line = "PRON"+str(ix)+" -> '"+elem+ "'"
            yazil.append(line)


for ix, val in enumerate(verbs.keys()):
    if verbs[val] != []:
        for elem in verbs[val]:
            line = "V"+str(ix)+" -> '"+elem+ "'"
            yazil.append(line)

for val in list(set(adv)):
    line = "ADV"+" -> '"+val+ "'"
    yazil.append(line)

for val in list(set(adj)):
    line = "ADJ"+" -> '"+val+ "'"
    yazil.append(line)

for val in list(set(conj)):
    line = "CONJ"+" -> '"+val+ "'"
    yazil.append(line)

for val in list(set(ques)):
    line = "QUES"+" -> '"+val+ "'"
    yazil.append(line)

for val in list(set(postp)):
    line = "POSTP"+" -> '"+val+ "'"
    yazil.append(line)

for val in list(set(det)):
    line = "DET"+" -> '"+val+ "'"
    yazil.append(line)

textfile = open("grammar_v3.txt", "w", encoding="utf-8")

"""for element in yazil:

    textfile.write(element + "\n")

textfile.close()"""

print(verbs.keys())
