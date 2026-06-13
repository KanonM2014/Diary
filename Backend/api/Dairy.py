import sqlite3

from fastapi import APIRouter

Router = APIRouter()


@Router.post ("/Diary")
def MembuatDiary (tanggal:str,judul:str,isi:str):
    conn = sqlite3.connect(r"D:\Kanon\Diary\database\Diary.db")
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
    conn.commit()
    conn.close()
    return f"Diary berhasil ditambahkan."

@Router.get("/Diary")
def MembacaDiary ():
    conn = sqlite3.connect(r"D:\Kanon\Diary\database\Diary.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM diary')
    diaries = cursor.fetchall()
    conn.close()
    return diaries

@Router.delete ("/Diary")
def MenghapusDiary (Urutan:int):
    conn = sqlite3.connect(r"D:\Kanon\Diary\database\Diary.db")
    cursor = conn.cursor()
    cursor.execute(f'DELETE FROM diary WHERE id={Urutan}')
    conn.commit()
    conn.close()
    return f"Diary berhasil dihapus."
@Router.put ("/Diary")
def MembenarkanDiary (Urutan:int,Pilihan:str,Mengganti:str):
    conn = sqlite3.connect(r"D:\Kanon\Diary\database\Diary.db")
    cursor = conn.cursor()
    cursor.execute(
    'UPDATE diary SET {} = ? WHERE id = ?'.format(Pilihan),
    (Mengganti, Urutan)
)
    conn.commit()       
    conn.close()
    return f"Diary berhasil diganti."