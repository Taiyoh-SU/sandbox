import decimal
import math

base_price = decimal.Decimal(int(input("金額：")))

discount_price  = base_price/2

direct_discount=discount_price*decimal.Decimal(0.7)
coupon=(discount_price*decimal.Decimal(0.3)).quantize(decimal.Decimal("1000"),rounding=decimal.ROUND_HALF_UP)

if discount_price >= 20000:
    direct_discount=14000
    coupon=6000

print(f"{base_price}円のプランでは、\n実質負担額は{base_price-direct_discount}円、\nクーポン額は{coupon}円です。")
