import pycountry


def get_country_code(country_name: str) -> str:
    """
    Helper method that takes a country name and returns its alpha_2 country code
    """
    country_code = None
    countries = pycountry.countries.search_fuzzy(country_name)
    if countries and len(countries) > 0:
        country_code = countries[0].alpha_2

    return country_code
