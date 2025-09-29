# Простий конвертер ETH -> USD (офлайн, вручну задаєш курс)
def eth_to_usd(eth_amount: float, eth_price_usd: float) -> float:
    return round(eth_amount * eth_price_usd, 2)

if __name__ == "__main__":
    try:
        eth = float(input("2 ETH?: "))
        price = float(input("Курс ETH в USD 2500): "))
        total = eth_to_usd(eth, price)
        print(f"≈ {total} USD")
    except ValueError:
        print("Введи числа, будь ласка 🙏")
