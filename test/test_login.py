import pytest
from Backend.api.login import login
from Backend.api.login import sign_up

def test_signup ():
    assert sign_up (4,6) == "Tidak bisa Sign Up."
    assert sign_up(4,"gsdfgsd")=="Tidak bisa Sign Up."
    assert sign_up("gjhfjk",7)=="Tidak bisa Sign Up."
    assert sign_up(4.3,"gsdfgsd")=="Tidak bisa Sign Up."
    assert sign_up(4,"gsdfgsd")=="Tidak bisa Sign Up."