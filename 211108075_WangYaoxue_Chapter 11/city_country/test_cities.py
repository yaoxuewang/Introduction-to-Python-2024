from city_functions import city_country

def test_city_country():
    """传入简单的城市和国家可行吗？"""
    santiago_chile = city_country('santiago', 'chile')
    assert santiago_chile == 'Santiago, Chile'