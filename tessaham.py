def find_max_profit(prices):
    min_price = float('inf')  # Harga saham terendah, diinisialisasi dengan nilai tak terhingga
    max_profit = 0  # Keuntungan maksimal, diinisialisasi dengan nilai 0

    for price in prices:
        if price < min_price:
            min_price = price  # Memperbarui harga saham terendah jika ditemukan harga lebih rendah

        elif price - min_price > max_profit:
            max_profit = price - min_price  # Memperbarui keuntungan maksimal jika ditemukan keuntungan yang lebih besar

    return max_profit

# Contoh data harga saham
prices = [100, 89, 70, 80, 78, 75, 90, 95, 88, 84, 93, 90, 85]

# Memanggil fungsi untuk mencari keuntungan maksimal
profit = find_max_profit(prices)

print("Keuntungan Maksimal: ", profit, "USD")
