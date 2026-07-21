import pytest
from Backend.api.login import login
from Backend.api.login import sign_up
from Backend.api.login import hapus_akun

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
