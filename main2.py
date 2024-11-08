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
        

class Pilseeta:
    Pilseetas_nosaukums=""
    Pilseetas_uzn_skaits=0
    
    id_iter_kl=itertools.count()
    
    def __init__(self,pils_nos=None,pils_uzn_sk=0):
        self.Pilseetas_id=next(self.id_iter_kl)+1
        self.Pilseetas_nosaukums= pils_nos
        self.Pilseetas_uzn_skaits= pils_uzn_sk
        
       

    def Pilseetas_info(self):
        return[
            self.Pilseetas_nosaukums, self.Pilseetas_uzn_skaits
        ]

    def Pilseetas_info_print(self):
        print('Pilsētas nosaukums:',self.Pilseetas_nosaukums)
        print('Cik suši iestādes ir pilsētā? :',self.Pilseetas_uzn_skaits)



uzņ1=Uzņēmums("UNAGI sushi shop","Atbrīvošanas aleja 111,Rēzekne","unagisushi@inbox.lv",28689903) 
uzņ2=Uzņēmums("Sushi Li","Atbrīvošanas aleja 81,Rēzekne","sushililatvija@gmail.com",25744425)

print(uzņ1.Uzņēmuma_id)
uzņ1.Uzņēmuma_info()
uzņ1.Uzņēmuma_info_print()
print(uzņ2.Uzņēmuma_id)
uzņ2.Uzņēmuma_info()
uzņ2.Uzņēmuma_info_print()


pak1=Pilseeta('Rīga',20)
pak2=Pilseeta('Daugavpils',4)
pak3=Pilseeta('Jelgava',6)

print(pak1.Pilseetas_id)
pak1.Pilseetas_info()
pak1.Pilseetas_info_print()
print(pak2.Pilseetas_id)
pak2.Pilseetas_info()
pak2.Pilseetas_info_print()
print(pak3.Pilseetas_id)
pak3.Pilseetas_info()
pak3.Pilseetas_info_print()