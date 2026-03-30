# Temperature convertion functions
def celsius_to_fahrenheit(celsius): return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit): return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius): return celsius + 273.15

def kelvin_to_celsius(kelvin): return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit): return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(kelvin): return (9/5) * (kelvin - 273.15) + 32

def convert_temperature(temperature):
    try:
        # check length of input and count the number of alphabetic characters
        if len(temperature) < 2:
            raise ValueError(
                'Wrong input. It must contain number and unit of temperature')
        count = 0
        for t in temperature:
            if t.isalpha():
                count += 1
        if count > 1:
            raise ValueError(
                'Wrong input. It must contain only one unit of temperature')
        # extract the last character as the unit and the rest as the number
        char = temperature[-1].upper()
        number = float(temperature[:-1].strip())
        # convertion
        c_to_f = celsius_to_fahrenheit(number)
        c_to_k = celsius_to_kelvin(number)
        f_to_c = fahrenheit_to_celsius(number)
        f_to_k = fahrenheit_to_kelvin(number)
        k_to_c = kelvin_to_celsius(number)
        k_to_f = kelvin_to_fahrenheit(number)
        if char == 'C':
            result1 = f'{c_to_f:.2f} fahrenheit'
            result2 = f'{c_to_k:.2f} kelvin'
        elif char == 'F':
            result1 = f'{f_to_c:.2f} celsius'
            result2 = f'{f_to_k:.2f} kelvin'
        elif char == 'K':
            result1 = f'{k_to_c:.2f} celsius'
            result2 = f'{k_to_f:.2f} fahrenheit'
        else:
            raise ValueError(
                'Wrong input. It must contain only one unit of temperature (C, F or K)')
    except ValueError as e:
        print(e)
    except TypeError:
        print('Please enter valid input')
    else:
        return f'{number} {char} is equal to {result1} and {result2}.'

def call_temperature_convertor():
    user_input = input('Please enter temperature in Celsius, Fahrenheit or Kelvin: ')
    convert_temperature(user_input)

# call the function
call_temperature_convertor()

def convert_temperature(temperature):
    while True:
        try:
            # check length of input and count the number of alphabetic characters
            if len(temperature) < 2:
                raise ValueError(
                    'Wrong input. It must contain number and unit of temperature')
            count = 0
            for t in temperature:
                if t.isalpha():
                    count += 1
            if count > 1:
                raise ValueError(
                    'Wrong input. It must contain only one unit of temperature')
            # extract the last character as the unit and the rest as the number
            char = temperature[-1].upper()
            number = float(temperature[:-1].strip())
            # convertion
            c_to_f = celsius_to_fahrenheit(number)
            c_to_k = celsius_to_kelvin(number)
            f_to_k = fahrenheit_to_kelvin(number)
            f_to_c = fahrenheit_to_celsius(number)
            k_to_c = kelvin_to_celsius(number)
            k_to_f = kelvin_to_fahrenheit(number)
            if char == 'C':
                result1 = f'{c_to_f:.2f} fahrenheit'
                result2 = f'{c_to_k:.2f} kelvin'
            elif char == 'F':
                result1 = f'{f_to_c:.2f} celsius'
                result2 = f'{f_to_k:.2f} kelvin'
            elif char == 'K':
                result1 = f'{k_to_c:.2f} celsius'
                result2 = f'{k_to_f:.2f} fahrenheit'
            else:
                raise ValueError(
                    'Oops... It must contain only one unit of temperature (C, F or K)')
        except ValueError as e:
            print(e)
        except TypeError:
            print('Please enter valid input')
        else:
            return f'{number} {char} is equal to {result1} and {result2}.'
