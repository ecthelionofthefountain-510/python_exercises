import mini_calculations

def main():
    x, y = 3, 5
    print(f"{x} + {y} =", mini_calculations.add(x, y))
    print(f"{x} * {y} =", mini_calculations.multiply(x, y))

if __name__ == "__main__":
    main()