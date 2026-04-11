from fastapi import APIRouter
import ast
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
    # Parse string menjadi dict
    diary_dict = ast.literal_eval(Diaries[Urutan-1])

    if Pilihan=="Tanggal":
        diary_dict["Tanggalnya"]=Mengganti
    elif Pilihan=="Judul":
        diary_dict["Judulnya"]=Mengganti
    elif Pilihan=="Isi":
        diary_dict["Isi"]=Mengganti
    else:
        return "Pilihan tidak valid"

    Diaries[Urutan-1] = str(diary_dict)

    # Tulis kembali ke file
    file=open("dairy.txt","w")
    for diary in Diaries:
        file.write(str(diary)+"\n")
    file.close()
    return"Diary berhasil di ubah"
