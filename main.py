class UnitConverter:
    def cm_to_feet(self, cm):
        return cm / 30.48

    def km_to_miles(self, km):
        return km * 0.621371

    def usd_to_inr(self, usd):
        exchange_rate = 73.5  # Replace this with the current exchange rate
        return usd * exchange_rate


def main():
    converter = UnitConverter()

    while True:
        print("Choose an option:")
        print("1. Convert cm to feet")
        print("2. Convert km to miles")
        print("3. Convert USD to INR")
        print("4. Exit")

        choice = int(input())

        if choice == 1:
            cm = float(input("Enter length in centimeters: "))
            feet = converter.cm_to_feet(cm)
            print(f"{cm} cm is equal to {feet:.2f} feet.\n")
        elif choice == 2:
            km = float(input("Enter distance in kilometers: "))
            miles = converter.km_to_miles(km)
            print(f"{km} km is equal to {miles:.2f} miles.\n")
        elif choice == 3:
            usd = float(input("Enter amount in USD: "))
            inr = converter.usd_to_inr(usd)
            print(f"{usd} USD is equal to {inr:.2f} INR.\n")
        elif choice == 4:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.\n")


if __name__ == "__main__":
    main()
