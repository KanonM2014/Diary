import pytest

def Penjumlahan(angka1,angka2):
    if (type (angka1) == int or type (angka1) == float) and (type (angka2) == int or type (angka2) ==float):
        return angka1 + angka2
    else:
        return "Input yang dimasukkan salah."

def test_latihan():
    assert 1 == 1

def test_penjumlahan():
    assert Penjumlahan( 2,3 ) == 5
    assert Penjumlahan(-1,1) == 0
    assert Penjumlahan(0,0) == 0
    assert Penjumlahan("a","b") == "Input yang dimasukkan salah."
    assert Penjumlahan(1,"a") == "Input yang dimasukkan salah." 
    assert Penjumlahan("b",2) == "Input yang dimasukkan salah."
    assert Penjumlahan(0.2 , 0.5)== 0.7
    assert Penjumlahan(True , False) == "Input yang dimasukkan salah."
    assert Penjumlahan(0.2 , 1) == 1.2
def Pengurangan(angka1,angka2):
    if (type (angka1) == int or type (angka1) == float) and (type (angka2) == int or type (angka2) ==float):
        return angka1 - angka2
    else:
        return "Input yang dimasukkan salah."


def test_pengurangan():
    assert Pengurangan(7,2) == 5
    assert Pengurangan(-1,2) == -3
    assert Pengurangan(0,0) == 0
    assert Pengurangan("a","b") == "Input yang dimasukkan salah."
    assert Pengurangan(1,"a") == "Input yang dimasukkan salah." 
    assert Pengurangan("b",2) == "Input yang dimasukkan salah."
    assert Pengurangan(0.2 , 0.5)== -0.3
    assert Pengurangan(True , False) == "Input yang dimasukkan salah."
    assert Pengurangan(0.2 , 1) == - 0.8

def Perkalian(angka1,angka2):
    if (type (angka1) == int or type (angka1) == float) and (type (angka2) == int or type (angka2) ==float):
        return angka1 * angka2
    else:
        return "Input yang dimasukkan salah."


def test_perkalian():
    assert Perkalian(7,2) == 14
    assert Perkalian(-1,2) == -2
    assert Perkalian(0,0) == 0
    assert Perkalian("a","b") == "Input yang dimasukkan salah."
    assert Perkalian(1,"a") == "Input yang dimasukkan salah." 
    assert Perkalian("b",2) == "Input yang dimasukkan salah."
    assert Perkalian(0.2 , 0.5)== 0.1
    assert Perkalian(True , False) == "Input yang dimasukkan salah."
    assert Perkalian(0.2 , 1) == 0.2   