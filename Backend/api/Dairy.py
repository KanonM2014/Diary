from fastapi import APIRouter

from database.db import get_connection
Router = APIRouter()

@Router.post ("/Diary")
def MembuatDiary (tanggal:str,judul:str,isi:str):
    if tanggal== "" or judul=="" or isi=="":
        return "Diary tidak berhasil ditambahkan."
    else:
        with get_connection() as conn :
            cursor = conn.cursor()
            cursor.execute(
                '''CREATE TABLE IF NOT EXISTS diary(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    Tanggal TEXT NOT NULL,
                    Judul TEXT NOT NULL,
                    Isi TEXT NOT NULL
                )
                '''
            )       
            cursor.execute(
            'INSERT INTO diary (Tanggal, Judul, Isi) VALUES (?, ?, ?)', 
            (tanggal, judul, isi)
            )
        return "Diary berhasil ditambahkan." 
     
@Router.get("/Diary")
def MembacaDiary ():
    with get_connection() as conn :
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM diary')
        diaries = cursor.fetchall()
    return diaries

@Router.delete ("/Diary")
def MenghapusDiary (Urutan:int):

    if (type(Urutan) == str or type(Urutan) == float):
        return "Diary tidak berhasil dihapus."
    else:
        with get_connection() as conn :
            cursor = conn.cursor()
            cursor.execute(f'SELECT * FROM diary WHERE id =?',(Urutan,))
            Bebas=cursor.fetchall()
            if len(Bebas)== 0:
                return"Data tidak ada."
            cursor.execute(f'DELETE FROM diary WHERE id=?',(Urutan,))

        return f"Diary berhasil dihapus."
@Router.put ("/Diary")
def MembenarkanDiary (Urutan:int,Pilihan:str,Mengganti:str):
    if (type (Urutan)==str or type(Urutan)==float) or (type (Pilihan)==int or type(Pilihan)==float) or (type (Mengganti)==int or type (Mengganti)==float):
        return"Diary tidak berhasil diubah."
    elif Urutan=="" or Pilihan=="" or Mengganti=="":
        return"Diary tidak berhasil diubah."
    else:
        with get_connection() as conn :
            cursor = conn.cursor()
            cursor.execute(
            'UPDATE diary SET {} = ? WHERE id = ?'.format(Pilihan),
            (Mengganti, Urutan)
        )

        return f"Diary berhasil diganti."