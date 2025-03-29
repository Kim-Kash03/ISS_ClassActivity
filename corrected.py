def find_cube_pairs(target): #missing colon for defining function
    solutions = []
    max_num = round(target ** (1/3))  # Fixed targ!= target and exponentiation ***

    for a in range(1, max_num + 1):  # Fix 'ranges' function and missing colon
        for b in range(a, max_num + 1):  # Fix 'ranges' function and missing colon
            if a**3 + b**3 == target:  # Fix exponentiation and 'targ'
                solutions.append((a, b))  # Fix variable name 'sol'

    return solutions  # Fix return statement

pairs = find_cube_pairs(1729)  # Remove the extra comma
print("Valid cube pairs for 1729:")  # Fix printf to print
for a, b in pairs:  # Fix variable name and missing colon
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1729")  # 1728--1729 & printf to print
