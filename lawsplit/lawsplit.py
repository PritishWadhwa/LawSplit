import pysbd
import re


class split_data:
    def __init__(self):
        self.vDict = {}
        self.vnum = 0
        self.repDict = {}
        self.repNum = 0
        self.singleDict = {}
        self.singleNum = 0
        self.seg = pysbd.Segmenter(language="en", clean=False)
        self.sentList = []

    def regexCitation(self, data):
        while(True):
            occ = re.search(
                r"\d{1,4}\s((\s?(Dallam|Hosea\'s\sRep\.|Dudley\sRep\.|Or\.\sApp\.|F\.R\.D\.|Ga\.\sL\.\sRep\.|Greene|Serg\.\s&\sRawl\.|N\.J\.\s\(Manumission\)|Unrep\.\sTenn\.\sCas\.|Ohio\sSt\.|Ct\.\sCust\.|Okla\.\sCrim\.|Indian\sTerr\.|P\.R\.|Super\.\sCt\.\s\(R\.I\.\)|Yeates|Barb\.|Smith\s\(N\.\sH\.\)|Chand\.|Whart\.|Vaux|How\.\sPr\.\s\(n\.s\.\)|Howison|Tenn\.\sApp\.|Teiss\.|Ill\.|Del\.\sCh\.|Walker|Ohio\sApp\.\s3d|Cal\.\sRptr\.\s3d|Utah\s2d|App\.\sD\.C\.|Edw\.\sCh\.|Pennyp\.|N\.Y\.|N\.Y\.\sSuper\.\sCt\.|Pa\.\sJust\.\sL\.\sRep\.|D\.C\.|Cal\.\sUnrep\.|Jeff\.|N\.M\.\sApp\.|Tenn\.\sCh\.\sR\.|N\.M\.|Mart\.\s\(o\.s\.\)|Rawle|Cai\.\sCas\.|Cl\.\sCh\.|How\.\sPr\.|F\.\sSupp\.|F\.3d|Dem\.\sSur\.|Neb\.\sApp\.|Minn\.|Hay\.\s&\sHaz\.|White\s&\sW\.|Balt\.\sC\.\sRep\.|Ala\.|McCahon|Freem\.\sCh\.|Pen\.\s&\sW\.|V\.I\.|Pears\.|Md\.|Lock\.\sRev\.\sCas\.|Daly\s\(N\.Y\.\)|Posey|Misc\.2d|Am\.\sSamoa\s3d|La\.\sAnn\.|F\.\sApp\'x|N\.E\.2d|Parsons|Armstrong\.\sElection\sCases|N\.Y\.\s2d|Binn\.|Lans\.\sCh\.|Blume\sUnrep\.\sOp\.|Ohio\sN\.P\.\s\(n\.s\.\)|N\.Y\.\sSup\.\sCt\.|Johns\.\sCh\.|Tex\.\sCiv\.\sApp\.|Dakota|Mills\sSurr\.|Rob\.|Va\.\sDec\.|Hilt\.|T\.C\.|Ark\.\sTerr\.\sRep\.|Miles|Wright|Cal\.\sApp\.\s3d|Miss\.\s\(S\.\s&\sM\.\sCh\.\)|Doug\.|Cal\.\s5th|Ga\.|N\.Y\.\sCrim\.|Md\.\sApp\.|Ohio\sApp\.\sUnrep\.|Fla\.\sSupp\.|Mor\.\sSt\.\sCas\.|Barb\.\sCh\.|Wis\.|L\.\sEd\.\s2d|Minor|Abb\.\sPr\.|Cole\.\sCas\.|Sadler|Ohio\sL\.R\.|N\.Y\.3d|A\.D\.2d|Port\.|Bur\.|Ind\.\sL\.\sRep\.|P\.R\.\sSent\.|Ant\.\sN\.P\.\sCas\.|Shan\.\sCas\.|Cal\.\s3d|Wash\.\sApp\.|Paige\sCh\.|Wyo\.|Haw\.|Blackf\.|D\.\sChip\.|Rep\.\sCont\.\sElect\.\sCase\.|Del\.|Rec\.\sCo\.\sCt\.|Gill|Gibb\.\sSurr\.|C\.M\.A\.|Stew\.\s&\sP\.|Fla\.|S\.W\.3d|Johns\.|H\.\s&\sMcH\.|Miss\.|Robards|D\.C\.\s\(patent\)|Connoly\sSur\.\sRep\.|Colo\.|Hill\s&\sDen\.|Watts|N\.Y\.\sProc\.\sCt\.\sAss\.|Johns\.\sCas\.|Mich\.\sPr\.|Myrick|Redf\.|Ohio\sC\.A\.|Am\.\sTribal\sLaw|Pa\.\sFid\.|Conn\.|Va\.\sApp\.|Ohio\sCir\.\sDec\.|N\.J\.L\.|Disney\s\(Ohio\)|H\.\s&\sG\.|S\.W\.2d|Blume\sSup\.\sCt\.\sTrans\.|P\.2d|Seld\.\sNotes|A\.D\.3d|Ga\.\sApp\.|Brayt\.|Watts\s&\sSerg\.|Pelt\.|Pin\.|Ohio\sLaw\sAbs\.|Wend\.|Cole\.\s&\sCai\.\sCas\.|Mont\.|Va\.\sCol\.\sDec\.|N\.H\.|Va\.|Cal\.\sApp\.\s4th|S\.W\.|N\.\sChip\.|So\.3d|Ohio\sMisc\.|Pa\.\sD\.\s&\sC\.|Va\.\sCir\.|Brad\.|Mich\.|N\.\sMar\.\sI\.\sCommw\.|F\.\sSupp\.\s2d|N\.J\.\sEq\.|Walk\.\sCh\.|D\.\sHaw\.|Pa\.\sCommw\.|N\.Y\.\sSt\.\sRep\.|Mass\.\sL\.\sRptr\.|U\.S\.\sApp\.\sD\.C\.|Thomp\.\s&\sCook|Handy|A\.3d|Ohio\sC\.C\.\sDec\.|A\.D\.|Howell\sN\.P\.|Tex\.\sL\.\sR\.|G\.\s&\sJ\.|Ala\.\sApp\.|Mich\.\sN\.P\.\sR\.|Idaho|Super\.\sCt\.\sJud\.|Rec\.\sCo\.\sCh\.\s\(S\.C\.\)|Trans\.\sApp\.|Ohio\sN\.P\.|Fla\.\sSupp\.\s2d|Okla\.|Willson|Tenn\.\sCrim\.\sApp\.|Abb\.N\.\sCas\.|Cow\.|S\.C\.D\.C\.\s\(N\.S\.\)|Guam|N\.J\.\sSuper\.|Cal\.\sApp\.|Aik\.|Pa\.\s\(Admiralty\)|Vt\.|F\.2d|Cl\.\sCt\.|Ohio\sSt\.\s3d|S\.C\.\sEq\.|How\.\sApp\.\sCas\.|Kirby|N\.J\.\sMisc\.|Nev\.|Conn\.\sSupp\.|Hoff\.\sCh\.|Navajo\sRptr\.|Tuck\.\sSurr\.|Ohio|Hopk\.\sCh\.|Tapp\.\sRep\.|Pa\.\sSuper\.|Mart\.\s\(n\.s\.\)|Law\sTimes\s\(N\.S\.\)|McGrath|Brightly|Cal\.\s4th|Monaghan|S\.C\.L\.|Alaska\sFed\.|Ky\.\sOp\.|Sand\.\sCh\.|Kan\.|Abb\.\sPr\.\s\(n\.s\.\)|Neb\.|Mass\.\sSupp\.|Denio|Tenn\.|F\.\sCas\.|Wash\.|F\.|N\.C\.\sApp\.|Charlton\sRep\.|Abb\.\sCt\.\sApp\.|Misc\.|Fed\.\sCl\.|Alaska|Ohio\sCh\.|Conn\.\sCir\.\sCt\.|Mann\.\sUnrep\.\sCas\.|Ky\.|Ohio\sApp\.\s2d|Pa\.|Tex\.|Colo\.\sL\.\sRep\.|Colo\.\sN\.\sP\.|Mo\.|Silv\.\sSup\.|Haw\.\sApp\.|Morris|Md\.\sCh\.|Hill|P\.R\.\sFed\.|Kan\.\sApp\.|B\.R\.|R\.I\.|Miss\.\sDec\.|Ill\.\sApp\.\s2d|Ct\.\sCl\.|Mo\.\sApp\.|Ill\.\sCt\.\sCl\.|Misc\.3d|Ohio\sC\.C\.\s\(N\.S\.\)|Ariz\.|Rep\.\sCont\.\sEl\.|Va\.\s\(Patt\.\s&\sHeath\)|E\.D\.\sSmith|S\.\sCt\.|Mass\.\sApp\.\sCt\.|T\.C\.A\.|Tex\.\sCt\.\sApp\.|Day|Rec\.\sV\.A\.\sCt\.\s\(R\.I\.\)|N\.\sMar\.\sI\.|Ohio\sC\.C\.|N\.J\.\sTax|So\.|N\.E\.3d|La\.|Cal\.\sDist\.\sCt\.|Ark\.\sApp\.|S\.C\.|Am\.\sSamoa\s2d|Park\.\sCrim\.\sRep\.|Va\.\sCh\.\sDec\.|Iowa|McGl\.|Dall\.|Stew\.|Cal\.\sSuper\.\sCt\.|Silv\.\sCt\.\sApp\.|M\.J\.|La\.\sApp\.|Ark\.|Am\.\sSamoa|Pa\.\sD\.\s&\sC\.2d|Tex\.\sCrim\.|Harr\.\sCh\.|N\.Y\.S\.|E\.D\.\sPa\.|Wash\.\s2d|Bland|R\.I\.\sDec\.|P\.3d|Edm\.\sSel\.\sCas\.|N\.C\.|Ill\.\sCir\.\sCt\.\sRep\.|Cal\.|Foster|Or\.\sTax|Goebel|Keyes|Cal\.\sApp\.\s2d|Mass\.\sApp\.\sDiv\.|Ohio\sMisc\.\s2d|Root|Mass\.\sApp\.\sDec\.|Ariz\.\sApp\.|N\.D\.|Ill\.\sApp\.\s3d|N\.Y\.\sCity\sCt\.\sRep\.|A\.2d|Mass\.|Sarat\.\sCh\.\sSent\.|C\.C\.P\.A\.|Colo\.\sApp\.|S\.D\.|Kan\.\sApp\.\s2d|N\.J\.|Cai\.|Wis\.\s2d|Davis\sL\.\sCt\.\sCas\.|U\.S\.|Lans\.|Pa\.\sD\.\s&\sC\.4th|Vet\.\sApp\.|Liquor\sTax\sRep\.|Georgia\sDecisions|Del\.\sCas\.|Charlton|W\.\sVa\.|So\.2d|Ohio\sSt\.\s2d|Tyl\.|Wheel\.\sCr\.\sCas\.|Cin\.\sSup\.\sCt\.\sRep\.|H\.\s&\sJ\.|Cal\.\s2d|N\.W\.2d|Bradf\.|Gunby|Grant|Ill\.\s2d|Pa\.\sD\.\s&\sC\.3d|Cal\.\sApp\.\s5th|Ct\.\sInt\'l\sTrade|Mich\.\sApp\.|Conn\.\sApp\.|Ill\.\sApp\.|Wash\.\sTerr\.|Ind\.|F\.\sSupp\.\s3d|P\.R\.\sDec\.|Coffey|Or\.|Cust\.\sCt\.|Ohio\sApp\.|Pow\.\sSurr\.|Pa\.\sD\.\s&\sC\.5th|B\.T\.A\.|Utah|Wilson|Me\.|Ind\.\sApp\.|Add\.|Hawai\'i|Fed\.\s\(2d\))\s?|\s?[\w]+\.\s?|\s?\&\.?\s?|\s?(at)\s?)+\,?)+\s(\,?\s?\d{1,5}\,?\s?(\s?\(\d{1,4}\)\s?)?)[\,\.\;]?", data)
            if occ is None:
                break
            cite = occ.group(0)
            start = data.find(cite)
            end = start + len(cite)
            currSpan = '[CITATION_SPAN_' + str(self.repNum) + ']'
            data = data[:start] + currSpan + ' ' + data[end:]
            self.repDict[currSpan] = cite
            self.repNum += 1
        return data

    def replaceSingle(self, data):
        alpha = "qwertyuiopasdfghjklzxcvbnm"
        for i in alpha:
            reg = r'\s' + i + '(\.|\,)+\s'
            rep = ' ' + i + ' '
            while(True):
                occ = re.search(reg, data)
                if occ is None:
                    break
                repData = occ.group(0)
                start = data.find(repData)
                end = start + len(repData)
                currSpan = '[SINGLE_SPAN_' + str(self.singleNum) + ']'
                data = data[:start] + currSpan + ' ' + data[end:]
                self.singleDict[currSpan] = repData
                self.singleNum += 1
        return data

    def detectVersusCases(self, data):
        citation_list = []
        cite_dict = {}
        data = re.sub(r'\s(Inc)(\.|\,)+\s', ' Inc ', data)
        data = re.sub(r'\s(Co)(\.|\,)+\s', ' Co ', data)
        data = re.sub(r'\s(Ltd)(\.|\,)+\s', ' Ltd ', data)
        data = re.sub(r'\s(inc)(\.|\,)+\s', ' inc ', data)
        data = re.sub(r'\s(co)(\.|\,)+\s', ' co ', data)
        data = re.sub(r'\s(ltd)(\.|\,)+\s', ' ltd ', data)
        data = re.sub(r'\s(No)(\.|\,)+\s', ' Num ', data)
        data = re.sub(r'\s(no)(\.|\,)+\s', ' num ', data)
        data = re.sub(r'\s(Vol)(\.|\,)+\s', ' Vol ', data)
        data = re.sub(r'\s(vol)(\.|\,)+\s', ' vol ', data)
        data = re.sub(r'\s(Corp)(\.|\,)+\s', ' Corp ', data)
        data = re.sub(r'\s(corp)(\.|\,)+\s', ' corp ', data)
        data = re.sub(r'\s(viz)(\.|\,)+\s', ' viz ', data)
        data = re.sub(r'\s(Viz)(\.|\,)+\s', ' Viz ', data)
        data = re.sub(r'\s(corp)\s', ' corp ', data)
        data = re.sub(r'\s(Corp)\s', ' Corp ', data)
        data = re.sub(r'\s(Pvt)(\.|\,)+\s', ' Pvt ', data)
        data = re.sub(r'\s(pvt)(\.|\,)+\s', ' pvt ', data)
        data = re.sub(r'\s(mr)(\.|\,)+\s', ' mr ', data)
        data = re.sub(r'\s(ms)(\.|\,)+\s', ' ms ', data)
        data = re.sub(r'\s(Ms)(\.|\,)+\s', ' Ms ', data)
        data = re.sub(r'\s(Mr)(\.|\,)+\s', ' Mr ', data)
        data = re.sub(r'\s(Jr)(\.|\,)+\s', ' Jr ', data)
        data = re.sub(r'\s(jr)(\.|\,)+\s', ' jr ', data)
        data = re.sub(r'\s(Sr)(\.|\,)+\s', ' Sr ', data)
        data = re.sub(r'\s(sr)(\.|\,)+\s', ' sr ', data)
        data = re.sub(r'\s(Dr)(\.|\,)+\s', ' Dr ', data)
        data = re.sub(r'\s(dr)(\.|\,)+\s', ' dr ', data)
        data = re.sub(r'\s(al)(\.|\,)+\s', ' al ', data)
        data = re.sub(r'\s(Al)(\.|\,)+\s', ' Al ', data)
        data = re.sub(r'\s(A)(\.|\,)+\s', ' A ', data)
        data = re.sub(r'\s(Q)(\.|\,)+\s', ' Q ', data)
        data = re.sub(r'\s(cont)(\.|\,)+\s', ' cont ', data)
        data = re.sub(r'\s(Cont)(\.|\,)+\s', ' Cont ', data)
        data = re.sub(r'\s(aff)(\.|\,)+\s', ' aff ', data)
        data = re.sub(r'\s(Aff)(\.|\,)+\s', ' Aff ', data)
        data = re.sub(r'\s(cert)(\.|\,)+\s', ' cert ', data)
        data = re.sub(r'\s(Cert)(\.|\,)+\s', ' Cert ', data)
        data = re.sub(r'\s(Art)(\.|\,)+\s', ' Art ', data)
        data = re.sub(r'\s(art)(\.|\,)+\s', ' art ', data)
        data = re.sub(r'\s(Bros)(\.|\,)+\s', ' Bros ', data)
        data = re.sub(r'\s(bros)(\.|\,)+\s', ' bros ', data)
        data = re.sub(r'\s(Ref)(\.|\,)+\s', ' Ref ', data)
        data = re.sub(r'\s(ref)(\.|\,)+\s', ' ref ', data)
        data = re.sub(r'\s(ref\'d)\s', ' ref ', data)
        data = re.sub(r'\s(Mfg)(\.|\,)+\s', ' Mfg ', data)
        data = re.sub(r'\s(mfg)(\.|\,)+\s', ' mfg ', data)
        data = re.sub(r'\s(dist)(\.|\,)+\s', ' dist ', data)
        data = re.sub(r'\s(Dist)(\.|\,)+\s', ' Dist ', data)
        data = re.sub(r'\s(Commn)(\.|\,)+\s', ' Commn ', data)
        data = re.sub(r'\s(commn)(\.|\,)+\s', ' commn ', data)
        data = re.sub(r'\s(sec)(\.|\,)+\s', ' sec ', data)
        data = re.sub(r'\s(Sec)(\.|\,)+\s', ' Sec ', data)
        data = re.sub(r'\s(pet)(\.|\,)+\s', ' pet ', data)
        data = re.sub(r'\s(Pet)(\.|\,)+\s', ' Pet ', data)
        data = re.sub(r'\s(com)(\.|\,)+\s', ' com ', data)
        data = re.sub(r'\s(Com)(\.|\,)+\s', ' Com ', data)
        data = re.sub(r'\s(eq)(\.|\,)+\s', ' eq ', data)
        data = re.sub(r'\s(Eq)(\.|\,)+\s', ' Eq ', data)
        data = re.sub(r'\s(Doc)(\.|\,)+\s', ' Doc ', data)
        data = re.sub(r'\s(doc)(\.|\,)+\s', ' doc ', data)
        data = re.sub(r'\s(Mrs)(\.|\,)+\s', ' Mrs ', data)
        data = re.sub(r'\s(mrs)(\.|\,)+\s', ' mrs ', data)
        data = re.sub(r'\s(ed)(\.|\,)+\s', ' ed ', data)
        data = re.sub(r'\s(Ed)(\.|\,)+\s', ' Ed ', data)
        data = re.sub(r'\s(Nom)(\.|\,)+\s', ' Nom ', data)
        data = re.sub(r'\s(nom)(\.|\,)+\s', ' nom ', data)
        data = re.sub(r'\s(ch)(\.|\,)+\s', ' ch ', data)
        data = re.sub(r'\s(Ch)(\.|\,)+\s', ' Ch ', data)
        data = re.sub(r'\s(Eq)(\.|\,)+\s', ' Eq ', data)
        data = re.sub(r'\s(eq)(\.|\,)+\s', ' eq ', data)
        data = re.sub(r'(See)\,\s', 'See ', data)
        data = re.sub(r'(see)\,\s', 'see ', data)
        data = re.sub(r'\s(e\.g)\.\,?\s', ' eg ', data)
        data = re.sub(r'\s(i\.e)\.\,?\s', ' ie ', data)
        data = re.sub(r'\s(a\.m)\.\,?\s', ' am ', data)
        data = re.sub(r'\s(p\.m)\.\,?\s', ' pm ', data)
        data = re.sub(r'(D\.C\.)\s', 'DC ', data)
        data = re.sub(r'\s(ins)(\.|\,)+\s', ' ins ', data)
        data = re.sub(r'\s(Ins)(\.|\,)+\s', ' Ins ', data)
        data = re.sub(r'\s(ex)(\.|\,)+\s', ' ex ', data)
        data = re.sub(r'\s(Ex)(\.|\,)+\s', ' Ex ', data)
        data = re.sub(r'\s(cf)(\.|\,)+\s', ' cf ', data)
        data = re.sub(r'\s(Cf)(\.|\,)+\s', ' Cf ', data)
        data = re.sub(r'\s(civ)(\.|\,)+\s', ' civ ', data)
        data = re.sub(r'\s(Civ)(\.|\,)+\s', ' Civ ', data)
        data = re.sub(r'\s(mortg)(\.|\,)+\s', ' mortgage ', data)
        data = re.sub(r'\s(Mortg)(\.|\,)+\s', ' Mortgage ', data)
        data = re.sub(r'\.\.\.', ' ', data)
        deduce = 0
        cid3 = 20000000
        data_res = re.finditer(r"\sv(s)?\.?\s\w+", data, flags=re.I)
        datactr = 0
        for match in data_res:
            datactr += 1
            s = match.start()
            e = match.end()
            citation_list.append(data[s:e].strip())
        for i in range(len(citation_list)):
            postid = None
            preid = None
            vid = data.find(citation_list[i])
            startId = data.find(' ', vid)
            preCheck = data[max(0, vid-50):vid]
            postCheck = data[vid:vid+50]
            preCaps = re.finditer(
                r"([A-Z][A-Za-z-’]+|[A-Z]\.)(\s([A-Z]\.|of|and|&)|(?:\s[A-Z][A-Za-z-’]*))*", preCheck)
            postCaps = re.finditer(
                r"([A-Z][A-Za-z-’]+|[A-Z]\.)(\s([A-Z]\.|of|and|&)|(?:\s[A-Z][A-Za-z-’]*))*", postCheck)
            dctr = 0
            for match in preCaps:
                dctr += 1
                s = match.start()
                preid = s
            for match in postCaps:
                postid = match.end()
                break
            if preid == None or postid == None:
                deduce = 1
                continue
            cite_dict[cid3] = data[vid-(len(preCheck)-preid):vid+postid]
            currSpan = '[CITATION_SPAN_v' + str(self.vnum) + ']'
            self.vnum += 1
            self.vDict[currSpan] = cite_dict[cid3]
            data = data[:vid-(len(preCheck)-preid)] + \
                currSpan + data[vid+postid:]
            cid3 += 1
        return data

    def split_text(self, data, path=None):
        """
        path: path of the file to store the split data e.g. ~/file.txt
        """
        self.vDict = {}
        self.vnum = 0
        self.repDict = {}
        self.repNum = 0
        self.singleDict = {}
        self.singleNum = 0
        self.sentList = []
        fileData = self.regexCitation(data)
        fileData = self.detectVersusCases(fileData)
        fileData = self.replaceSingle(fileData)
        split = fileData.splitlines()
        for i in split:
            j = self.seg.segment(i)
            for k in j:
                if len(k) > 0:
                    if(k.find('[CITATION_SPAN') >= 0 or k.find('[SINGLE_SPAN') >= 0):
                        for cite in self.vDict:
                            if k.find(cite) != -1:
                                start = k.find(cite)
                                end = start + len(cite)
                                k = k[:start] + self.vDict[cite] + k[end:]
                        for cite in self.repDict:
                            if k.find(cite) != -1:
                                start = k.find(cite)
                                end = start + len(cite)
                                k = k[:start] + self.repDict[cite] + k[end:]
                        for cite in self.singleDict:
                            if k.find(cite) != -1:
                                start = k.find(cite)
                                end = start + len(cite)
                                k = k[:start] + self.singleDict[cite] + k[end:]
                    k = k.strip()
                    k = re.sub(' +', ' ', k)
                    self.sentList.append(k.strip())
        if path is not None:
            file = open(path, 'w')
            file.write('\n'.join(self.sentList))
            file.close()
        return self.sentList

    def split_file(self, file, path=None):
        """
        path: path of the file to store the split data e.g. ~/file.txt
        """
        self.vDict = {}
        self.vnum = 0
        self.repDict = {}
        self.repNum = 0
        self.singleDict = {}
        self.singleNum = 0
        self.sentList = []
        with open(file, 'r') as f:
            data = f.readlines()
        data = '\n'.join(i for i in data)
        fileData = self.regexCitation(data)
        fileData = self.detectVersusCases(fileData)
        fileData = self.replaceSingle(fileData)
        split = fileData.splitlines()
        for i in split:
            j = self.seg.segment(i)
            for k in j:
                if len(k) > 0:
                    if(k.find('[CITATION_SPAN') >= 0 or k.find('[SINGLE_SPAN') >= 0):
                        for cite in self.vDict:
                            if k.find(cite) != -1:
                                start = k.find(cite)
                                end = start + len(cite)
                                k = k[:start] + self.vDict[cite] + k[end:]
                        for cite in self.repDict:
                            if k.find(cite) != -1:
                                start = k.find(cite)
                                end = start + len(cite)
                                k = k[:start] + self.repDict[cite] + k[end:]
                        for cite in self.singleDict:
                            if k.find(cite) != -1:
                                start = k.find(cite)
                                end = start + len(cite)
                                k = k[:start] + self.singleDict[cite] + k[end:]
                    k = k.strip()
                    k = re.sub(' +', ' ', k)
                    self.sentList.append(k.strip())
        if path is not None:
            file = open(path, 'w')
            file.write('\n'.join(self.sentList))
            file.close()
        return self.sentList
