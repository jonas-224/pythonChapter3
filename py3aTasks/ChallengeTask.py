total_area = 0
num_triangles = int(input("How many triangles? "))

for i in range(1, num_triangles + 1):
    print(f"\nTriangle {i}:")
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area = 0.5 * base * height
    print(f"Area: {area}")
    total_area += area

print(f"\nTotal area of all triangles: {total_area}")
