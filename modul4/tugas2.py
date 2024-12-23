import math
import time

def execution_timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Waktu eksekusi {func.__name__}: {end_time - start_time:.6f} detik")
        return result
    return wrapper

# (x, y)
@execution_timer
def parse_points(input_str):
    try:
        numbers = list(map(int, input_str.split(',')))
        if len(numbers) % 2 != 0:
            raise ValueError("Input harus memiliki jumlah angka genap.")
        points = [(numbers[i], numbers[i + 1]) for i in range(0, len(numbers), 2)]
        return points
    except ValueError as e:
        raise ValueError(f"Terjadi kesalahan: {e}")

# translasi
@execution_timer
def translation(tx, ty):
    def transform(points):
        return [(x + tx, y + ty) for x, y in points]
    return transform


# rotasi
@execution_timer
def rotation(angle_degrees):
    angle_radians = math.radians(angle_degrees)
    cos_theta = math.cos(angle_radians)
    sin_theta = math.sin(angle_radians)

    def transform(points):
        return [
            (
                round(x * cos_theta - y * sin_theta, 2),
                round(x * sin_theta + y * cos_theta, 2)
            )
            for x, y in points
        ]
    return transform

# dilatasi
@execution_timer
def dilation(scale):
    def transform(points):
        return [(x * scale, y * scale) for x, y in points]
    return transform

# transformasi
@execution_timer
def apply_transformations(points):
    translasi = translation(3, 7)
    rotasi = rotation(60)
    dilatasi = dilation(1.5)

    translated_points = translasi(points)
    print("Hasil Translasi:", translated_points)

    rotated_points = rotasi(translated_points)
    print("Hasil Rotasi:", rotated_points)

    dilated_points = dilatasi(rotated_points)
    print("Hasil Dilatasi:", dilated_points)

if __name__ == "__main__":
    try:
        user_input = "1,2,3,4,5,6,7,8,9,10"
        points = parse_points(user_input)
        print("Titik awal:", points)

        apply_transformations(points)
    except ValueError as e:
        print(e)
