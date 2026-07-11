import pytest

from Backend.api.Dairy import MembuatDiary
from Backend.api.Dairy import MenghapusDiary

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
    