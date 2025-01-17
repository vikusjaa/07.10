import sqlite3
import tkinter as tk
from tkinter import messagebox

conn = sqlite3.connect('06.12_pd.db')
cursor = conn.cursor()

def pievienot_uznemumu():
    def saglabat_uznemumu():
        nosaukums = nosaukums_entry.get()
        adrese = adrese_entry.get()
        e_pasts = e_pasts_entry.get()
        tel_num = tel_num_entry.get()
        id_pilsetas = id_pilsetas_entry.get()
        id_logo = id_logo_entry.get()

        if nosaukums and id_pilsetas:
            cursor.execute(
                "INSERT INTO Uznemums (nosaukums, adrese, e_pasts, tel_num,id_pilsetas,id_logo) VALUES (?, ?, ?, ?, ?,?)",
                (nosaukums, adrese, e_pasts, tel_num,int(id_pilsetas),int(id_logo))
            )
            conn.commit()
            messagebox.showinfo("Veiksmīgi", "Uzņēmums pievienots!")
            logs.destroy()
        else:
            messagebox.showerror("Kļūda", "Lūdzu, aizpildiet visus laukus korekti!")

    logs = tk.Toplevel()
    logs.title("Pievienot uzņēmumu")
    logs.geometry("300x300")

    tk.Label(logs, text="Nosaukums:").pack()
    nosaukums_entry = tk.Entry(logs)
    nosaukums_entry.pack()

    tk.Label(logs, text="Adrese:").pack()
    adrese_entry = tk.Entry(logs)
    adrese_entry.pack()

    tk.Label(logs, text="E-pasts:").pack()
    e_pasts_entry = tk.Entry(logs)
    e_pasts_entry.pack()

    tk.Label(logs, text="Tālrunis:").pack()
    tel_num_entry = tk.Entry(logs)
    tel_num_entry.pack()

    tk.Label(logs, text="Pilsētas ID:").pack()
    id_pilsetas_entry = tk.Entry(logs)
    id_pilsetas_entry.pack()

    tk.Label(logs, text="Logo ID:").pack()
    id_logo_entry = tk.Entry(logs)
    id_logo_entry.pack()

    saglabat_btn = tk.Button(logs, text="Saglabāt", command=saglabat_uznemumu)
    saglabat_btn.pack(pady=10)

def meklēt_uznemumu():
    def atrast_uznemumu():
        nosaukums = nosaukums_entry.get()
        if nosaukums:
            cursor.execute("SELECT * FROM Uzņēmumi WHERE nosaukums LIKE ?", (f"%{nosaukums}%",))
            rezultati = cursor.fetchall()
            if rezultati:
                rezultati_str = ""
                for r in rezultati:
                    rezultati_str += f"{r[0]}: {r[1]} {r[2]}, {r[3]}, {r[4]}, {r[5]}, {r[6]}, {r[7]}\n"
            else:
                messagebox.showinfo("Rezultāti", "Netika atrasts neviens uzņēmums.")
        else:
            messagebox.showerror("Kļūda", "Lūdzu, ievadiet uzņēmuma nosaukumu!")

    logs = tk.Toplevel()
    logs.title("Meklēt uzņēmumu")
    logs.geometry("300x200")

    tk.Label(logs, text="Uzņēmuma nosaukums:").pack()
    nosaukums_entry = tk.Entry(logs)
    nosaukums_entry.pack()

    meklēt_btn = tk.Button(logs, text="Meklēt", command=atrast_uznemumu)
    meklēt_btn.pack(pady=10)


def dzēst_uznemumu():
    def dzēst_uznemumu_no_db():
        id_uznemuma = id_uznemuma_entry.get()
        if id_uznemuma.isdigit():
            cursor.execute("DELETE FROM Uzņēmumi WHERE id_uznemuma = ?", (id_uznemuma,))
            conn.commit()
            messagebox.showinfo("Veiksmīgi", f"Uzņēmums ar ID {id_uznemuma} tika izdzēsts!")
            logs.destroy()
        else:
            messagebox.showerror("Kļūda", "Lūdzu, ievadiet derīgu ID!")

    logs = tk.Toplevel()
    logs.title("Dzēst uzņēmumu")
    logs.geometry("300x150")

    tk.Label(logs, text="Uzņēmuma ID:").pack()
    id_uznemuma_entry = tk.Entry(logs)
    id_uznemuma_entry.pack()

    dzēst_btn = tk.Button(logs, text="Dzēst", command=dzēst_uznemumu_no_db)
    dzēst_btn.pack(pady=10)


def uznemumu_logs():
    uznemumi_logs = tk.Toplevel()
    uznemumi_logs.title("Uzņēmumu pārvaldība")
    uznemumi_logs.geometry("300x250")

    pievienot_btn = tk.Button(uznemumi_logs, text="Pievienot uzņēmumu", command=pievienot_uznemumu, width=25, height=2, bg="lightblue")
    pievienot_btn.pack(pady=10)

    meklēt_btn = tk.Button(uznemumi_logs, text="Meklēt uzņēmumu", command=meklēt_uznemumu, width=25, height=2, bg="lightgreen")
    meklēt_btn.pack(pady=10)

    dzēst_btn = tk.Button(uznemumi_logs, text="Dzēst uzņēmumu", command=dzēst_uznemumu, width=25, height=2, bg="lightyellow")
    dzēst_btn.pack(pady=10)

    iziet_btn = tk.Button(uznemumi_logs, text="Iziet", command=uznemumu_logs.destroy, width=25, height=2, bg="red", fg="white")
    iziet_btn.pack(pady=10)


def pievienot_pilsetu():
    def saglabat_pilsetu():
        pilsetas_nos = pilsetas_nos_entry.get()
        pilsetas_uzn_sk =pilsetas_uzn_sk_entry.get()

        if pilsetas_nos :
            cursor.execute(
                "INSERT INTO Pilsetas (pilsetas_nos, pilsetas_uzn_sk) VALUES (?, ?)",
                (pilsetas_nos, pilsetas_uzn_sk)
            )
            conn.commit()
            messagebox.showinfo("Veiksmīgi", "Pilsēta pievienota!")
            logs.destroy()
        else:
            messagebox.showerror("Kļūda", "Lūdzu, aizpildiet visus laukus korekti!")

    logs = tk.Toplevel()
    logs.title("Pievienot pilsētu")
    logs.geometry("300x300")

    tk.Label(logs, text="Pilsēta:").pack()
    pilsetas_nos_entry = tk.Entry(logs)
    pilsetas_nos_entry.pack()

    tk.Label(logs, text="Uzņēmumu skaits pilsētā:").pack()
    pilsetas_uzn_sk_entry = tk.Entry(logs)
    pilsetas_uzn_sk_entry.pack()

    saglabat_btn = tk.Button(logs, text="Saglabāt", command=saglabat_pilsetu)
    saglabat_btn.pack(pady=10)


def meklēt_pilsetu():
    def atrast_pilsetu():
        pilsetas_nos = pilsetas_nos_entry.get()
        if pilsetas_nos:
            cursor.execute("SELECT * FROM  Pilsetas WHERE pilsetas_nos LIKE ?", (f"%{pilsetas_nos}%",))
            rezultati = cursor.fetchall()
            if rezultati:
                rezultati_str = ""
                for r in rezultati:
                    rezultati_str += f"{r[0]}: {r[1]}, {r[2]}\n"
            else:
                messagebox.showinfo("Rezultāti", "Netika atrasts neviens treneris.")
        else:
            messagebox.showerror("Kļūda", "Lūdzu, ievadiet trenera vārdu!")

    logs = tk.Toplevel()
    logs.title("Meklēt pilsētu")
    logs.geometry("300x200")

    tk.Label(logs, text="Pilsēta:").pack()
    pilsetas_nos_entry = tk.Entry(logs)
    pilsetas_nos_entry.pack()

    meklēt_btn = tk.Button(logs, text="Meklēt", command=atrast_pilsetu)
    meklēt_btn.pack(pady=10)


def dzēst_pilsetu():
    def dzēst_pilsetu_no_db():
        id_pilsetas = id_pilsetas_entry.get()
        if id_pilsetas.isdigit():
            cursor.execute("DELETE FROM Pilsetas WHERE id_pilsetas = ?", (id_pilsetas))
            conn.commit()
            messagebox.showinfo("Veiksmīgi", f"Pilsēta ar ID {id_pilsetas} tika izdzēsta!")
            logs.destroy()
        else:
            messagebox.showerror("Kļūda", "Lūdzu, ievadiet derīgu ID!")

    logs = tk.Toplevel()
    logs.title("Dzēst pilsētu")
    logs.geometry("300x150")

    tk.Label(logs, text="Pilsētas ID:").pack()
    id_pilsetas_entry = tk.Entry(logs)
    id_pilsetas_entry.pack()

    dzēst_btn = tk.Button(logs, text="Dzēst", command=dzēst_pilsetu_no_db)
    dzēst_btn.pack(pady=10)


def pilsetu_logs():
    pilsētas_logs = tk.Toplevel()
    pilsētas_logs.title("Pilsētu pārvaldība")
    pilsētas_logs.geometry("300x250")

    pievienot_btn = tk.Button(pilsētas_logs, text="Pievienot pilsētu", command=pievienot_pilsetu, width=25, height=2, bg="lightblue")
    pievienot_btn.pack(pady=10)

    meklēt_btn = tk.Button(pilsētas_logs, text="Meklēt pilsētu", command=meklēt_pilsetu, width=25, height=2, bg="lightgreen")
    meklēt_btn.pack(pady=10)

    dzēst_btn = tk.Button(pilsētas_logs, text="Dzēst pilsētu", command=dzēst_pilsetu, width=25, height=2, bg="lightyellow")
    dzēst_btn.pack(pady=10)

    iziet_btn = tk.Button(pilsētas_logs, text="Iziet", command=pilsetu_logs.destroy, width=25, height=2, bg="red", fg="white")
    iziet_btn.pack(pady=10)


def izveidot_galveno_logu():
    def uznemumi_poga():
        pievienot_uznemumu()
        uznemumu_logs()
        #messagebox.showinfo("Uzņēmums", "Atvērta uzņēmumu pārvaldība.")

    def pilsetas_poga():
        pievienot_pilsetu()
        pilsetu_logs()
        #messagebox.showinfo("Pilsētas", "Atvērta pilsētu pārvaldība.")


    logs = tk.Tk()
    logs.title("Suši bāru pārvaldība")
    logs.geometry("300x200")

    uznemumi_btn = tk.Button(logs, text="Uzņēmumi", command=uznemumi_poga, width=20, height=2, bg="lightblue")
    uznemumi_btn.pack(pady=20)

    pilsetas_btn = tk.Button(logs, text="Pilsētas", command=pilsetas_poga, width=20, height=2, bg="lightgreen")
    pilsetas_btn.pack(pady=20)

    logs.mainloop()

if __name__ == "__main__":
    izveidot_galveno_logu()

    