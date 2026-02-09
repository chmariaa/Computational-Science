from decimal import Decimal, getcontext, ROUND_HALF_UP

getcontext().prec = 105 

# formula: volume of a sphere -> V = (4/3) * pi * r^3
radius = Decimal(10) 

# pi with 105 decimal places
pi = "3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148"

# the true volume using pi value
pi_true = Decimal(pi)
volume_true = (Decimal(4)/Decimal(3)) * pi_true * (radius**3)

print(f"{'Decimals':<10} | {'Method':<10} | {'Calculated Volume':<25} | {'Difference (Error)'}")
print("-" * 85)

decimal = [20, 40, 60, 100]

for d in decimal:
    # truncate
    pi_trunc = Decimal(pi[:d+2])
    
    # round
    pi_round = Decimal(pi).quantize(Decimal("1." + "0"*d), rounding=ROUND_HALF_UP)

    # calculate volume
    vol_trunc = (Decimal(4)/Decimal(3)) * pi_trunc * (radius**3)
    vol_round = (Decimal(4)/Decimal(3)) * pi_round * (radius**3)

    # differences
    diff_trunc = vol_trunc - volume_true
    diff_round = vol_round - volume_true

    print(f"{d:<10} | {'Trunc':<10} | {float(vol_trunc):.10f}...    | {diff_trunc:.2E}")
    print(f"{d:<10} | {'Round':<10} | {float(vol_round):.10f}...    | {diff_round:.2E}")