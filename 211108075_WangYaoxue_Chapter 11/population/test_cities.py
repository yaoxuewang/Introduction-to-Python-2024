from city_functions_pop_optional import city_country

def test_city_country():
    """传入简单的城市和国家可行吗？"""
    santiago_chile = city_country('santiago', 'chile')
    assert santiago_chile == 'Santiago, Chile'

def test_city_country_population():
    """可向形参 population 传递值吗？"""
    santiago_chile = city_country('santiago', 'chile', population=5_000_000)
    assert santiago_chile == 'Santiago, Chile - population 5000000'