import pytest
from Backend.api.login import login
from Backend.api.login import sign_up
from Backend.api.login import hapus_akun
from Backend.api.login import ganti_password
from Backend.api.login import update_profil
def test_signup ():
    #String , string , string , integer , string .
    assert sign_up(4,6,9,"jkgghj",1) == "Tidak bisa Sign Up." #Integer , Integer , Integer , String ,Integer .
    assert sign_up(4.7,6.4,2.7,8.2,9.8)=="Tidak bisa Sign Up." # Float , Float , Float , Float , Float . 
    assert sign_up("gjhfjk","hsagfs","gdggdh",8,"shfgs")=="Sign Up berhasil." #String , String , String , Integer , String .
    assert sign_up(4,0,0.5,"hftfkj",7.8)=="Tidak bisa Sign Up."# Integer , Integer , Float , String , Float . 
    assert sign_up(4.7,"gsdfgsd",9,0.5,"dfafdh")=="Tidak bisa Sign Up." # Float , String , Integer , Float , String.
    assert sign_up("fgaagaf",9,1.4,"dfagfs",7)== "Tidak bisa Sign Up."#String , Integer , Float , String , Integer.
    assert sign_up(9,0.7,"jpfgsj",9,"kjaflaf")=="Tidak bisa Sign Up."# Integer , Float , String , Integer , String .
    assert sign_up(7.4,9,"Fgafdfa",14,8)=="Tidak bisa Sign Up."#Float , Integer , String , Integer , Integer .
    assert sign_up("dsfgvdga", 9.3, 2, 0.4,9.1)#String , Float , Integer , Float , Float . 
    assert sign_up("",0.4,0,"dfgsdfgs","")=="Tidak bisa Sign Up."#Kosong , Float , Integer , String , Kosong .
    assert sign_up(2,"dgagh","",7.4,"GFafdsaf")=="Tidak bisa Sign Up."#Integer , String , Kosong , Float , String.
    assert sign_up("FGsag" , "" , 0.6,9,"dgsdgf")=="Tidak bisa Sign Up."#String , Kosong , Float , Integer , String .
    assert sign_up(0.8,9,"jkhgk","",0)=="Tidak bisa Sign Up."#Float , Integer , String , Kosong , Integer . 
    assert sign_up("","","","","")=="Tidak bisa Sign Up."#Kosong , Kosong , Kosong , Kosong , Kosong .

def test_hapusakun() :
    #Username = String
    assert hapus_akun(8)=="Akun tidak berhasil dihapus."#Integer
    assert hapus_akun(7.4)=="Akun tidak berhasil dihapus."#Float
    assert hapus_akun("")=="Username harus diisi."#Kosong

def test_ganti_password():
    # Username = String , Password_Lama == String , Password_Baru == String .
    assert ganti_password(9,7,4)#Integer , Integer , Integer .
    assert ganti_password(0.7,9.3,2.7)#Float , Float , Float .
    assert ganti_password("","","")#Kosong , Kosong , Kosong .
    assert ganti_password("fdgdf", 0 , 9)#String , Integer , Integer .
    assert ganti_password(9,"dgfdfgf",7)#Integer, String , Integer .
    assert ganti_password(6,7,"gjh")#Integer , Integer , String .
    assert ganti_password(0.8,9,8)#Float ,Integer, Integer .
    assert ganti_password(2,4.3,5)#Integer ,Float, Integer .
    assert ganti_password(0,4,5.7)#Integer ,Integer, Float .
    assert ganti_password(7.9,"hjh","kihihu")#Float ,String, String .
    assert ganti_password("fzfdf",5.2,"dfad")#String ,Float, String .
    assert ganti_password("gfsads","fga",9.7)#String ,String, Float .
    assert ganti_password(8,"fdsgdf","fhdsgdf")#Integer ,String, String .
    assert ganti_password("dfgsdfg",9,"Fgdsg")#String ,Integer, String .
    assert ganti_password("dfhsg","fgsfg",9)#String , String , Integer .
    assert ganti_password(8,5.3,7.5)#Integer ,Float, Float .
    assert ganti_password(5.4,3,0.6)#Float ,Integer, Float .
    assert ganti_password(7.5,5.9,5)#Float ,Float, Integer .
    assert ganti_password("jkhkh",8.6,9.5)#String ,Float, Float .
    assert ganti_password(0.5,"hkhk",7.5)#Float ,String, Float .
    assert ganti_password(6.9,5.9,"hkjhk")#Float ,Float , String .
    assert ganti_password(0.8,"","")#Float ,Kosong, Kosong .
    assert ganti_password("",9.8,"")#Kosong ,Float, Kosong .
    assert ganti_password("","",5.64)#Kosong ,Kosong, Float .

def test_update_profil():
    #String , string , integer , string .
    assert update_profil(6,9,"jkgghj",1) == "Tidak bisa Update Profil. " # Integer , Integer , String ,Integer .
    assert update_profil(6.4,2.7,8.2,9.8)=="Tidak bisa Update Profil. " #  Float , Float , Float , Float . 
    assert update_profil("hsagfs","gdggdh",8,"shfgs")=="Update Profil berhasil." # String , String , Integer , String .
    assert update_profil(0,0.5,"hftfkj",7.8)=="Tidak bisa Update Profil. "#  Integer , Float , String , Float . 
    assert update_profil("gsdfgsd",9,0.5,"dfafdh")=="Tidak bisa Update Profil. " #  String , Integer , Float , String.
    assert update_profil(9,1.4,"dfagfs",7)== "Tidak bisa Update Profil. "# Integer , Float , String , Integer.
    assert update_profil(0.7,"jpfgsj",9,"kjaflaf")=="Tidak bisa Update Profil. "#  Float , String , Integer , String .
    assert update_profil(9,"Fgafdfa",14,8)=="Tidak bisa Update Profil. "# Integer , String , Integer , Integer .
    assert update_profil( 9.3, 2, 0.4,9.1)=="Tidak bisa Update Profil. "# Float , Integer , Float , Float . 
    assert update_profil(0.4,0,"dfgsdfgs","")=="Tidak bisa Update Profil. "# Float , Integer , String , Kosong .
    assert update_profil("dgagh","",7.4,"GFafdsaf")=="Tidak bisa Update Profil. "# String , Kosong , Float , String.
    assert update_profil( "" , 0.6,9,"dgsdgf")=="Tidak bisa Update Profil. "# Kosong , Float , Integer , String .
    assert update_profil(9,"jkhgk","",0)=="Tidak bisa Update Profil. "# Integer , String , Kosong , Integer . 
    assert update_profil("","","","")=="Tidak bisa Update Profil. " # Kosong , Kosong , Kosong , Kosong .

