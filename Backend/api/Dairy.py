from fastapi import APIRouter
Router = APIRouter()

@Router.post ("/Diary")
def MembuatDiary (Tanggal:str,Judul:str,Isi:str):
    Diary = {
        "Tanggalnya":Tanggal,
        "Judulnya":Judul,
        "Isi":Isi
        }
    
    file=open("dairy.txt","a+")
    file.write(str(Diary)+"\n")
    file.close()
    return f"Diary berhasil ditambahkan."

@Router.get("/Diary")
def MembacaDiary ():
    global Diaries
    file=open("dairy.txt","a+")
    file.seek(0)
    Diaries=file.read().strip()
    Diaries =Diaries.split("\n")
    return Diaries

@Router.delete ("/Diary")
def MenghapusDiary (Urutan:int):
    Diaries[Urutan-1]
    del Diaries[Urutan-1]
    print("Dairies: ",Diaries )
    file=open("dairy.txt","a+")
    file.truncate(0)
    for diary in Diaries:
        file.write(str(diary)+"\n")
    file.close()
    return"Diary telah dihapuskan." 

@Router.put ("/Diary")
def MembenarkanDiary (Urutan:int,Pilihan:str,Mengganti:str):
    if Pilihan=="Tanggal":
        Diaries[Urutan-1]
        Diaries[Urutan-1]["Tanggalnya"]=Mengganti
        return"Diary berhasil di ubah"

    if Pilihan=="Judul":
        Diaries[Urutan-1]
        Diaries[Urutan-1]["Judulnya"]=Mengganti
        return"Diary berhasil di ubah"

    if Pilihan=="Isi":
        Diaries[Urutan-1]
        Diaries[Urutan-1]["Isinya"]=Mengganti
        return"Diary berhasil di ubah"    
