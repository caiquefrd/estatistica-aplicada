media = 4.85
n1 = 20
trust_level_aim = 0.98
standard_deviation = 0.75
z1 = 2.33

def square_root(num):
    return num ** 0.5

def find_trust_indice(media, z, standard_deviation, n):
    result_pos = media + ((z * standard_deviation) / square_root(n))

    result_neg = media - ((z * standard_deviation) / square_root(n))

    return result_pos, result_neg

result = find_trust_indice(media, z1, standard_deviation, n1)
print(result)


