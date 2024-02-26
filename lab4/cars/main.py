import vehicleclass

def main():
    bikes = [
        vehicleclass.Motorcycle('Honda', 30000, 10000, 180),
        vehicleclass.Motorcycle('Ducatti', 5000, 15400, 300),
        vehicleclass.Motorcycle('Suzuki', 100, 11000, 220)
    ]
    trucks = [
        vehicleclass.Truck('Ford', 25000, 30000),
        vehicleclass.Truck('Chevrolet', 20000, 28000),
        vehicleclass.Truck('Dodge', 30000, 35000)
    ]
    compare_list = []

    while len(compare_list) < 2:
        choice = input('Would you like to viw bikes or trucks? (b or t) ').lower()
        if choice == 'b':
            display_vehicles('Bikes', bikes)
        elif choice == 't':
            display_vehicles('Trucks', trucks)
        else:
            print('Invalid option.')
            continue

        if ask_to_compare():
            if choice == 'b':
                select_vehicle(bikes, compare_list)
            elif choice == 't':
                select_vehicle(trucks, compare_list)

        if len(compare_list) > 0:
            if input('Would you like to go ahead and compare now (y or n) ').lower() == 'y':
                break

    print('\nVehicles selected for comparison:')
    for vehicle in compare_list:
        print(vehicle_info(vehicle))
        vehicle.make_noise()

def display_vehicles(category, vehicles):
    print(f'\nDisplaying {category}:')
    i = 1
    for vehicle in vehicles:
        print(f"{i}. {vehicle_info(vehicle)}")
        i += 1

def ask_to_compare():
    return input('Do you want to compare one of these vehicles? (y or n) ').lower() == 'y'

def select_vehicle(vehicles, compare_list):
    vehicle_number = int(input('Which vehicle do you want to compare (please list number)? ')) - 1
    if 0 <= vehicle_number < len(vehicles):
        compare_list.append(vehicles[vehicle_number])
        print('Vehicle added for comparison.')

def vehicle_info(vehicle):
    info = f"Make: {vehicle.make}, Miles: {vehicle.miles}, Price: ${vehicle.price}"
    if hasattr(vehicle, 'top_speed'):
        info += f", Top Speed: {vehicle.top_speed} mph"
    return info

if __name__ == '__main__':
    main()