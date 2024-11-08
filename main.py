import itertools

class Uzņēmums:

    Uzņēmuma_nosaukums=""
    Uzņēmuma_adrese=""
    Uzņēmuma_e_pasts=""
    Uzņēmuma_tel_num=0

    id_iter=itertools.count()

    def __init__(self,uzņ_nos=None,uzņ_adr=None,uzņ_e_pasts=None,uzņ_tel_num=0):
        self.Uzņēmuma_id = next(self.id_iter) + 1
        self.Uzņēmuma_nosaukums= uzņ_nos
        self.Uzņēmuma_adrese = uzņ_adr
        self.Uzņēmuma_e_pasts = uzņ_e_pasts
        self.Uzņēmuma_tel_num = uzņ_tel_num

    def Uzņēmuma_info(self):
        return[
            self.Uzņēmuma_nosaukums,self.Uzņēmuma_adrese,self.Uzņēmuma_e_pasts , self.Uzņēmuma_tel_num 
        ]
    def Uzņēmuma_info_print(self):
        print("Uzņēmuma nosaukums:"+ str(self.Uzņēmuma_nosaukums))
        print("Uzņēmuma adrese:"+ str(self.Uzņēmuma_adrese))
        print("Uzņēmuma e-pasta adrese:"+ str(self.Uzņēmuma_e_pasts))
        print("Uzņēmuma telefona numurs:"+ str(self.Uzņēmuma_tel_num))


uzņ1=Uzņēmums("TERADA","Atbrīvošanas aleja 90","info@terada.lv",26265971) 
uzņ2=Uzņēmums("Zeize","Dārzu iela 30","info@zeize.lv",27889947)
uzņ3=Uzņēmums("Poligrāfserviss","Viļakas 4","poligrafserviss@inbox.lv",64622748)

print(uzņ1.Uzņēmuma_id)
uzņ1.Uzņēmuma_info()
uzņ1.Uzņēmuma_info_print()
print(uzņ2.Uzņēmuma_id)
uzņ2.Uzņēmuma_info()
uzņ2.Uzņēmuma_info_print()
print(uzņ3.Uzņēmuma_id)
uzņ3.Uzņēmuma_info()
uzņ3.Uzņēmuma_info_print()


class Pakalpojums:
    Pakalpojuma_uzņēmums=""
    Pakalpojumu_veidi=""

    id_iter_kl=itertools.count()
    
    def __init__(self,pak_uzņ=None,pak_veid=None):
        self.Pakalpojuma_id=next(self.id_iter_kl)+1
        self.Pakalpojuma_uzņēmums= pak_uzņ
        self.Pakalpojumu_veidi= pak_veid
       

    def Pakalpojuma_info(self):
        return[
            self.Pakalpojuma_uzņēmums, self.Pakalpojumu_veidi
        ]

    def Pakalpojuma_info_print(self):
        print('Uzņēmums,kurā tiek piedāvāts pakalpojums:'+self.Pakalpojuma_uzņēmums)
        print('Pakalpojumu veidi:'+self.Pakalpojumu_veidi)


pak1=Pakalpojums('TERADA','Biznesa sistēmas,Mājas lapas,Grafiskais dizains,SEO optimizācija,Sociālie tīkli')
pak2=Pakalpojums('Zeize','Zīmogu izgatavošana,Poligrāfijas pakalpojumi,Kopēšana,Gravēšana,Apdruka,Balvu pagatavošana,Uzlīmes,Vizuālā reklāma,Kabinetu norāžu sistēmas,Dizaina izstrāde')
pak3=Pakalpojums('Poligrāfserviss','Zīmogi,Iepakojums,Iesiešana,Vizuālā reklāma,Ofsetdruka,Lielformāta druka,Reprezentācijas materiāli')

print(pak1.Pakalpojuma_id)
pak1.Pakalpojuma_info()
pak1.Pakalpojuma_info_print()
print(pak2.Pakalpojuma_id)
pak2.Pakalpojuma_info()
pak2.Pakalpojuma_info_print()
print(pak3.Pakalpojuma_id)
pak3.Pakalpojuma_info()
pak3.Pakalpojuma_info_print()