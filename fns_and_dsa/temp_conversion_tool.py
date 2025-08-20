def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

if __name__ == "__main__":
    c = 25
    f = 77
    print(f"{c}°C = {celsius_to_fahrenheit(c)}°F")
    print(f"{f}°F = {fahrenheit_to_celsius(f):.2f}°C")
