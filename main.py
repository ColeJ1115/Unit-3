import circleclass

def main():
    try:
        test = circleclass.Circle()
        print(f'Diameter:{test.calculate_diameter()}')
        print(f'Circumference{test.calculate_circumference()}')
        print(f'Area:{test.get_area()}')
        while True:
            you_grow = input('Do you wish to grow you circle? (y/n) ')
            you_grow = you_grow.lower()
            if you_grow != 'y':
                break
            print('Please wait while your circle magically grows. ')
            test.grow()
            print(f'New Radius: {test.get_radius()}')
            print(f'New Diameter: {test.calculate_diameter()}')
            print(f'New Circumference: {test.calculate_circumference()}')
            print(f'New Area: {test.get_area()}')
    except ValueError:
        print('Invalid input')
    print('Goodbye')


if __name__ == '__main__':
    main()

