'''
 * ARGS = returns as a tuple (values separated by commas)
** KWARGS = returns as a dictionary
'''

def save_car(brand, model, year, license_plate):
    # saves car in the database...
    print(f"Car successfully added! {brand}/{model}/{year}/{license_plate}")


save_car("Fiat", "Palio", 1999, "ABC-1234")
save_car(brand="Fiat", model="Palio", year=1999, license_plate="ABC-1234")
save_car(**{"brand": "Fiat", "model": "Palio", "year": 1999, "license_plate": "ABC-1234"})
