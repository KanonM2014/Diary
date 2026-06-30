import pytest

def Penjumlahan(angka1,angka2):
    return angka1 + angka2

def test_latihan():
    assert 1 == 1

def test_penjumlahan():
    assert Penjumlahan( 2,3 ) == 5
    assert Penjumlahan(-1,1) == 0
    assert Penjumlahan(0,0) == 0



