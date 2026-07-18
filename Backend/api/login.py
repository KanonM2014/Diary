from fastapi import APIRouter

from database.db import get_connection
Router = APIRouter()

@Router.get("/login")
def login(Username, Password):
    with get_connection() as conn:    
        cursor = conn.cursor()
        cursor.execute ('SELECT username, password FROM login WHERE username=?', (Username,))
        row = cursor.fetchone()
    
    
    if row is None:
        return "Login failed"
    
    or_username=row[0]
    or_password=row[1]
    if Username == or_username and Password == or_password:
        return "Login successful"
    else:
        return "Login failed"

    
@Router.post("/Sign Up")
def sign_up(Username:str, Password:str,Nama_Lengkap:str,Umur:int,Cita_cita:str):
    if (type(Username)==int or type (Username)==float) or (type (Password)==int or type (Password)==float)or(type (Nama_Lengkap)==int or type (Nama_Lengkap)==float)or(type(Umur)==str or type(Umur)==float)or(type (Cita_cita)==int or type (Cita_cita)==float):
        return"Tidak bisa Sign Up."
    elif Username=="" or Password=="" or Nama_Lengkap=="" or Umur=="" or Cita_cita=="":
        return "Tidak bisa Sign Up."
    else:
        with get_connection() as conn :
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
        
        return f"Sign Up berhasil."

@Router.delete("/Hapus Akun")
def hapus_akun(Username):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(f'DELETE FROM login WHERE username="{Username}"')

    return f"Akun {Username} berhasil dihapus."

@Router.put("/Ganti Password")
def ganti_password(Username,Password_Lama,Password_Baru):
    with get_connection() as conn:
        cursor=conn.cursor()
        cursor.execute(f'SELECT username,password FROM login WHERE username=?',(Username,))
        row= cursor.fetchone()
    
        if row is None:
            
            return "Username tidak ditemukan"
        
        or_username=row[0]
        or_password=row[1]

        if Username==or_username and Password_Lama==or_password:
            
            cursor.execute('UPDATE login SET password = ? WHERE username=?',(Password_Baru,Username))
            return "Password berhasil diganti."
        
        else:
            return"Password tidak berhasil diubah."
    
@Router.put("/Update Profil")
def update_profil(Username,Nama_Lengkap,Umur,Cita_cita):
    with get_connection() as conn :
        cursor=conn.cursor()
        cursor.execute('UPDATE login SET nama_lengkap=?,umur=?,cita_cita=? WHERE username=?',(Nama_Lengkap,Umur,Cita_cita,Username))

    return "Profil berhasil diperbarui."
