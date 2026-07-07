import pytest

from Backend.api.Dairy import MembuatDiary

def test_membuat_diary():
    assert MembuatDiary("15/05/2025","hikafhif","gsafdfa") == "Diary berhasil ditambahkan."
    assert MembuatDiary("13/04/2023", 13042023,"fsdadfdsf") == "Diary berhasil ditambahkan."
    assert MembuatDiary("12/08/2024","fdgdsf",120998) == "Diary berhasil ditambahkan."