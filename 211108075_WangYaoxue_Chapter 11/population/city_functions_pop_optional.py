"""一系列处理城市的函数"""

def city_country(city, country, population=0):
    """返回一个表示城市和国家的字符串"""
    output_string = f"{city.title()}, {country.title()}"
    if population:
        output_string += f" - population {population}"
    return output_string