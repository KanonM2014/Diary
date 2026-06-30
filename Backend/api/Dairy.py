from fastapi import APIRouter

from database.db import get_connection
Router = APIRouter()

@Router.post ("/Diary")
def MembuatDiary (tanggal:str,judul:str,isi:str):
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

    return f"Diary berhasil ditambahkan."

@Router.get("/Diary")
def MembacaDiary ():
    with get_connection() as conn :
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM diary')
        diaries = cursor.fetchall()
    return diaries

@Router.delete ("/Diary")
def MenghapusDiary (Urutan:int):
    with get_connection() as conn :
        cursor = conn.cursor()
        cursor.execute(f'DELETE FROM diary WHERE id={Urutan}')

    return f"Diary berhasil dihapus."
@Router.put ("/Diary")
def MembenarkanDiary (Urutan:int,Pilihan:str,Mengganti:str):
    with get_connection() as conn :
        cursor = conn.cursor()
        cursor.execute(
        'UPDATE diary SET {} = ? WHERE id = ?'.format(Pilihan),
        (Mengganti, Urutan)
    )

    return f"Diary berhasil diganti."