def apples(n, k):
    apples_student = k // n
    remaining_apples = k % n
    return apples_student, remaining_apples

n = int(input("Клькість школярів: "))
k = int(input("Кількість яблук: "))

result = apples(n, k)

print("Кількість яблук на кожного школяра:", result[0])
print("Залишок яблук у кошику:", result[1])
