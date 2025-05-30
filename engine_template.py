def get_vehicle_class(abbreviation):
    # Dictionary mapping abbreviations to vehicle classes
    vehicle_classes = {
        'SUV': 'Sport Utility Vehicle',
        'SED': 'Sedan',
        'TRK': 'Truck',
        'MC': 'Motorcycle',
        'VAN': 'Van',
        'CUV': 'Crossover Utility Vehicle',
        'EV': 'Electric Vehicle',
        'HB': 'Hatchback'
    }

    abbreviation = abbreviation.upper()  # Normalize input to uppercase
    return vehicle_classes.get(abbreviation, 'Unknown vehicle class')


def main():
    abbr = input("Enter vehicle abbreviation (e.g., SUV, SED, TRK): ").strip()
    vehicle_class = get_vehicle_class(abbr)
    print(f"Assigned vehicle class: {vehicle_class}")


if __name__ == "__main__":
    main()
