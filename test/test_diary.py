import pytest
from Backend.api.Dairy import MembuatDiary
from Backend.api.Dairy import MenghapusDiary
from Backend.api.Dairy import MembenarkanDiary
def test_membuat_diary():
    assert MembuatDiary("15/05/2025","hikafhif","gsafdfa") == "Diary berhasil ditambahkan."
    assert MembuatDiary("13/04/2023", 13042023,"fsdadfdsf") == "Diary berhasil ditambahkan."
    assert MembuatDiary("12/08/2024","fdgdsf",120998) == "Diary berhasil ditambahkan."
    assert MembuatDiary("23/04/2022","sdhifuah","")== "Diary tidak berhasil ditambahkan."
    assert MembuatDiary("","","") == "Diary tidak berhasil ditambahkan."
    assert MembuatDiary("12/06/2021","","jhgffhm")== "Diary tidak berhasil ditambahkan."
    assert MembuatDiary("","fhgjk","gjhgfjh")== "Diary tidak berhasil ditambahkan."
def test_menghapus_diary():
    assert MenghapusDiary("vfhsxhbgfg") == "Diary tidak berhasil dihapus."
    assert MenghapusDiary(0.4) == "Diary tidak berhasil dihapus."
    assert MenghapusDiary(100) == "Data tidak ada."
    assert MenghapusDiary(0)   == "Data tidak ada."
def test_membenarkan_diary():
    #Urutan integer. Pilihan string. Mengganti string 
    assert MembenarkanDiary("ghfkh",3,5)=="Diary tidak berhasil diubah." #string . integer. integer.
    assert MembenarkanDiary(0.4,0.8,0.12)=="Diary tidak berhasil diubah."#float . float . float .
    assert MembenarkanDiary(9,"jhkhj",12)=="Diary tidak berhasil diubah."#integer .  string .int.
    assert MembenarkanDiary("kjgk",0.8,0.12)=="Diary tidak berhasil diubah."#string . float .float.
    assert MembenarkanDiary(8,0,3)=="Diary tidak berhasil diubah."#integer.int.int.
    assert MembenarkanDiary("gjhgbkj","hgjkg","hjfh")=="Diary tidak berhasil diubah."#str .str.str.
    assert MembenarkanDiary(0,"fgsgfg",0.3)=="Diary tidak berhasil diubah."#int.str.float.
    assert MembenarkanDiary("jgg",6,0.7)=="Diary tidak berhasil diubah."#str.int.float.
    assert MembenarkanDiary(0.4,8,"hjfh")=="Diary tidak berhasil diubah."#float.int.string.
    assert MembenarkanDiary(0.4,0.8,"")=="Diary tidak berhasil diubah."#float.float.kosong.
    assert MembenarkanDiary(0.4,"","hjfh")=="Diary tidak berhasil diubah."#float.kosong.string.
    assert MembenarkanDiary("",0.8,"hjfh")=="Diary tidak berhasil diubah."#kosong.float.string.
    assert MembenarkanDiary("","","hjfh")=="Diary tidak berhasil diubah."#kosong.kosong.string.
    assert MembenarkanDiary(0.4,"","")=="Diary tidak berhasil diubah."#float.kosong.kosong.
    assert MembenarkanDiary("",0.8,"")=="Diary tidak berhasil diubah."#kosong.float.kosong.
    assert MembenarkanDiary("","","")=="Diary tidak berhasil diubah."#kosong.kosong.kosong.
    assert MembenarkanDiary(4,9.1,"hjfh")=="Diary tidak berhasil diubah."#int.float.string.
    assert MembenarkanDiary(0.4,0.9,"hjfh")=="Diary tidak berhasil diubah."#float.float.string.