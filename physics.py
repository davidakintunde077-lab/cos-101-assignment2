# PHYSICS CALCULATOR

# 1. ACCELERATION
def acceleration():
    print("\n--- ACCELERATION ---")
    u = float(input("Enter initial velocity: "))
    v = float(input("Enter final velocity: "))
    t = float(input("Enter time: "))

    if t == 0:
        print("Time cannot be zero.")
    else:
        a = (v - u) / t
        print("Acceleration =", a, "m/s²")


# 2. MOMENTUM
def momentum():
    print("\n--- MOMENTUM ---")
    m = float(input("Enter mass: "))
    v = float(input("Enter velocity: "))

    p = m * v
    print("Momentum =", p, "kg m/s")


# 3. FREQUENCY
def frequency():
    print("\n--- FREQUENCY ---")
    T = float(input("Enter time period: "))

    if T == 0:
        print("Time period cannot be zero.")
    else:
        f = 1 / T
        print("Frequency =", f, "Hz")


# 4. WAVE SPEED
def wave_speed():
    print("\n--- WAVE SPEED ---")
    f = float(input("Enter frequency: "))
    wavelength = float(input("Enter wavelength: "))

    v = f * wavelength
    print("Wave speed =", v, "m/s")


# 5. GRAVITATIONAL FORCE
def gravitational_force():
    print("\n--- GRAVITATIONAL FORCE ---")

    G = 6.674 * (10 ** -11)

    m1 = float(input("Enter mass of first object: "))
    m2 = float(input("Enter mass of second object: "))
    r = float(input("Enter distance between the objects: "))

    if r == 0:
        print("Distance cannot be zero.")
    else:
        F = (G * m1 * m2) / (r ** 2)
        print("Gravitational Force =", F, "N")


# MAIN PROGRAM

while True:

    print("\n====== PHYSICS CALCULATOR ======")
    print("1. Acceleration")
    print("2. Momentum")
    print("3. Frequency")
    print("4. Wave Speed")
    print("5. Gravitational Force")

    choice = input("\nSelect an operation (1-5): ")

    if choice == "1":
        acceleration()

    elif choice == "2":
        momentum()

    elif choice == "3":
        frequency()

    elif choice == "4":
        wave_speed()

    elif choice == "5":
        gravitational_force()

    else:
        print("Invalid selection. Please choose between 1 and 5.")

    # ASK USER WHETHER TO CONTINUE

    again = input("\nDo you want to continue? (yes/no): ").lower()

    if again != "yes":
        print("\nThank you for using the Physics Calculator!")
        break