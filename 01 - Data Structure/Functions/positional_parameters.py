def create_car(model, year, license_plate, /, brand, engine, fuel):
    print(model, year, license_plate, brand, engine, fuel)


create_car("Palio", 1999, "ABC-1234", brand="Fiat", engine="1.0", fuel="Gasoline")
create_car(model="Palio", year=1999, license_plate="ABC-1234", brand="Fiat", engine="1.0", fuel="Gasoline")  # invalid
