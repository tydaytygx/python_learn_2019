import decimal
decimal.getcontext().rounding = "ROUND_HALF_UP"#四舍五入
f = 1504.5
print(decimal.Decimal(1504.5).quantize(decimal.Decimal("0")))