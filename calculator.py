def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * discount_percent / 100)
        return discounted_price
    else:
        return price

# User Input and Output
original_price = float(input("Enter the original price of the item: $"))
discount = float(input("Enter the discount percentage: "))
final_price = calculate_discount(original_price, discount)

print(f"The final price after applying the discount is: ${final_price}")
