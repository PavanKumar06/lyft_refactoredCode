from datetime import datetime
from carFactory import CarFactory

current_date = datetime.now()
last_service_date = datetime(2016, 11, 26)
current_mileage = 50000
last_service_mileage = 48000
tire_wear = [0.91, 0.04, 0.24, 0.69]

# Creating an object of CarFactory
factory = CarFactory()

# Calling the create_calliope method
rorschach_car = CarFactory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear)
thovex_car = CarFactory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear)

print(rorschach_car.battery.needs_service())
print(rorschach_car.engine.needs_service())
print(rorschach_car.tires.needs_service())

print(thovex_car.battery.needs_service())
print(thovex_car.engine.needs_service())
print(thovex_car.tires.needs_service())
