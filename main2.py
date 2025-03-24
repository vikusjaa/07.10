import itertools
import sqlite3

conn=sqlite3.connect('06.12_pd.db')
cursor=conn.cursor()

class Uznemums:
    Uznemuma_nosaukums=""
    Uznemuma_adrese=""
    Uznemuma_e_pasts=""
    Uznemuma_tel_num=0
    Pilsetas_id=0
    Logo_id=0

    id_iter=itertools.count()

    def __init__(self,uzn_id,uzn_nos=None,uzn_adr=None,uzn_e_pasts=None,uzn_tel_num=0,pils_id=0,logo_id=0):
        #self.Uzņēmuma_id = next(self.id_iter) + 1
        self.Uznemuma_id= uzn_id
        self.Uznemuma_nosaukums= uzn_nos
        self.Uznemuma_adrese = uzn_adr
        self.Uznemuma_e_pasts = uzn_e_pasts
        self.Uznemuma_tel_num = uzn_tel_num
        self.Pilsetas_id = pils_id
        self.Logo_id = logo_id
    def info():
        uzn_id=int(input("Ievadi uzņēmuma ID:"))
        uzn_nos=input("Ievadi uzņēmuma nosaukumu:")
        uzn_adr=input("Ievadi uzņēmuma adresi:")
        uzn_e_pasts=input("Ievadi uzņēmuma e-pastu:")
        uzn_tel_num=int(input("Ievadi uzņēmuma telefona numuru:"))
        pils_id=int(input("Ievadi pilsētas ID:"))
        logo_id=int(input("Ievadi logo ID:"))

        cursor.execute('''INSERT INTO Uznemums (id_uznemuma,nosaukums,adrese,e_pasts,tel_num,id_pilsetas,id_logo)VALUES (?,?,?,?,?,?,?)''',
                       (uzn_id,uzn_nos, uzn_adr,uzn_e_pasts,uzn_tel_num,pils_id,logo_id))
        print("Uzņēmums pievienots!")
        conn.commit()

    def Uznemuma_info(self):
        return[
            self.Uznemuma_nosaukums,self.Uznemuma_adrese,self.Uznemuma_e_pasts , self.Uznemuma_tel_num 
        ]
    def Uznemuma_info_print(self):
        print("Uzņēmuma nosaukums:"+ str(self.Uznemuma_nosaukums))
        print("Uzņēmuma adrese:"+ str(self.Uznemuma_adrese))
        print("Uzņēmuma e-pasta adrese:"+ str(self.Uznemuma_e_pasts))
        print("Uzņēmuma telefona numurs:"+ str(self.Uznemuma_tel_num))
    
    def find_organisation_by_id():
        e=input('Ievadi uzņēmuma ID,kuru ir jāsameklē:')
        cursor.execute(f"""SELECT * FROM Uznemums WHERE id_uznemuma ={e}""")
        conn.commit()
        organisation=cursor.fetchall()
        for organisations in organisation:
            print(organisations)
        v=input('Vai gribat atjaunot uzņēmuma telefona numuru?(jā/nē) ')
        if v=='jā':
            x=input('Ievadi jaunu telefona numuru:')
            cursor.execute(f"""UPDATE Uznemums set tel_num=? WHERE id_uznemuma=?""",(x,e))
            conn.commit()
        else:
            pass
        
    def delete_organisation_by_id():  
        d=int(input('Ievadi uzņēmuma ID,kuru ir jāisdzēš:'))
        cursor.execute(f"""DELETE FROM Uznemums WHERE id_uznemuma ={d}""")
        conn.commit()
       
   
class Pilseta:
    Pilsetas_nosaukums=""
    Pilsetas_uzn_skaits=0
    
    id_iter_kl=itertools.count()
    
    def __init__(self,pils_nos=None,pils_uzn_sk=0):
        self.Pilsetas_id=next(self.id_iter_kl)+1
        self.Pilsetas_nosaukums= pils_nos
        self.Pilsetas_uzn_skaits= pils_uzn_sk
        
    def Pilsetas_info(self):
        return[
            self.Pilsetas_nosaukums, self.Pilsetas_uzn_skaits
        ]

    def Pilsetas_info_print(self):
        print('Pilsētas nosaukums:',self.Pilsetas_nosaukums)
        print('Cik suši iestādes ir pilsētā? :',self.Pilsetas_uzn_skaits)


def main():
    #load_data()
    #find_organization_by_id()
    while (True):
        response=input('(1) Add organization (2) Delete organizations (3) Find organisation (4) Exit ')
        if response=='1':
           Uznemums.info()
        elif response=='2':
           Uznemums.delete_organisation_by_id()
        elif response=='3':
           Uznemums.find_organisation_by_id()
        elif response=='4':
            #save_data()
            pass
            print('Bye bue!')
            exit()
        else:
            print('Chose a number between 1 and 3')
            continue

main()


