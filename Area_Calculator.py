def calc_area(shape):
    shape = shape.lower()

    if shape == "rectangle":
        l = float(input("Enter length: "))
        b = float(input("Enter breadth: "))
        print(f"Area: {l * b}")

    elif shape == "square":
        s = float(input("Enter side: "))
        print(f"Area: {s * s}")

    elif shape == "triangle":
        h = float(input("Enter height: "))
        b = float(input("Enter base: "))
        print(f"Area: {0.5 * b * h}")

    elif shape == "circle":
        r = float(input("Enter radius: "))
        pi = 3.14159
        print(f"Area: {pi * r * r}")

    elif shape == "parallelogram":
        b = float(input("Enter base: "))
        h = float(input("Enter height: "))
        print(f"Area: {b * h}")

    else:
        print("Shape not available")

if __name__ == "__main__":
    shape_name = input("Enter shape name: ")
    calc_area(shape_name)