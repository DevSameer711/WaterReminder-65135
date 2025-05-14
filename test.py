import pytest
from water_rem import calculate_water_intake, get_reminder_interval, recommend_water_temperature

def test_calculate_water_intake():
    assert calculate_water_intake(70, 25) == 2.45  
    assert calculate_water_intake(40, 10) == 1.2   
    assert calculate_water_intake(60, 60) == 2.4   

def test_get_reminder_interval():
    assert get_reminder_interval(1.2) == "Every 4 hours"
    assert get_reminder_interval(2.0) == "Every 3 hours"
    assert get_reminder_interval(3.0) == "Every 2 hours"

def test_recommend_water_temperature():
    assert recommend_water_temperature(60) == "Lukewarm water recommended"
    assert recommend_water_temperature(25) == "Cool water recommended"
    assert recommend_water_temperature(40) == "Room temperature water recommended"
