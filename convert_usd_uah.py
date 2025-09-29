```python
# Простий конвертер USD → UAH (курс вводиш сам)
def convert(usd, rate):
    return round(usd * rate, 2)

if __name__ == "__main__":
    try:
        usd = float(input("Введи суму в USD: "))
        rate = float(input("Введи курс (UAH за 1 USD): "))
        print(f"≈ {convert(usd, rate)} UAH")
    except ValueError:
        print("Введи числа, будь ласка.")
