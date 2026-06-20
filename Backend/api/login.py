import sqlite3

from fastapi import APIRouter
Router = APIRouter()

@Router.get("/login")
def login(Username, Password):
    conn = sqlite3.connect(r"D:\Kanon\Diary\database\Diary.db")  
    cursor = conn.cursor()
    cursor.execute ('SELECT username, password FROM login WHERE username=?', (Username,))
    row = cursor.fetchone()
    conn.close()
    
    or_username=row[0]
    or_password=row[1]
    if Username == or_username and Password == or_password:
        return "Login successful"
    else:
        return "Login failed"

    
@Router.post("/Sign Up")
def sign_up(Username, Password,Nama_Lengkap,Umur,Cita_cita):
    conn = sqlite3.connect(r"D:\Kanon\Diary\database\Diary.db")  
    cursor = conn.cursor()
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS login(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            nama_lengkap TEXT NOT NULL,
            umur INTEGER NOT NULL,
            cita_cita TEXT NOT NULL
        )
        '''
    )       
    cursor.execute(
       'INSERT INTO login (username, password,nama_lengkap,umur,cita_cita) VALUES (?, ?, ?, ?, ?)', 
       (Username, Password,Nama_Lengkap,Umur,Cita_cita)
    )
    conn.commit()
    return f"Sign Up berhasil."

@Router.delete("/Hapus Akun")
def hapus_akun(Username):
    conn = sqlite3.connect(r"D:\Kanon\Diary\database\Diary.db")
    cursor = conn.cursor()
    cursor.execute(f'DELETE FROM login WHERE username="{Username}"')
    conn.commit()
    conn.close()
    return f"Akun {Username} berhasil dihapus."

@Router.put("/Ganti Password")
def ganti_password(Username,Password_Lama,Password_Baru):
    conn=sqlite3.connect(r"D:\Kanon\Diary\database\Diary.db")
    cursor=conn.cursor()
    cursor.execute(f'SELECT username,password FROM login WHERE username=?',(Username,))
    row= cursor.fetchone()
    
    or_username=row[0]
    or_password=row[1]

    if Username==or_username and Password_Lama==or_password:
        
        cursor.execute('UPDATE login SET password = ? WHERE username=?',(Password_Baru,Username))
        conn.commit()
        conn.close()
        return "Password berhasil diganti."
    
    else: 
        return"Password tidak berhasil diubah."
    
@Router.put("/Update Profil")
def update_profil(Username,Nama_Lengkap,Umur,Cita_cita):
    conn=sqlite3.connect(r"D:\Kanon\Diary\database\Diary.db")
    cursor=conn.cursor()
    cursor.execute('UPDATE login SET nama_lengkap=?,umur=?,cita_cita=? WHERE username=?',(Nama_Lengkap,Umur,Cita_cita,Username))
    conn.commit()
    conn.close()
    return "Profil berhasil diperbarui."
