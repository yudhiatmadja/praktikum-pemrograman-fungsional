nilai_mahasiswa = {
    "yudhi": {
        "fungsional": 100,
        "mobile": 100,
        "web": 100,
    },
    "alex": {
        "fungsional": 90,
        "mobile": 80,
        "web": 70,
    },
    "albert": {
        "fungsional": 70,
        "mobile": 90,
        "web": 100,
    }
}

def averageStudent(nilai_mahasiswa):
    rata_rata_mahasiswa = {}
    for nama, nilai in nilai_mahasiswa.items():
        average = sum(nilai.values()) / len(nilai)
        rata_rata_mahasiswa[nama] = average
    return rata_rata_mahasiswa
    
def averageStudents(nilai_mahasiswa):
    total_nilai = 0
    total_matkul = 0
    for nilai in nilai_mahasiswa.values():
        total_nilai += sum(nilai.values())
        total_matkul += len(nilai)
    return total_nilai / total_matkul

average_Student = averageStudent(nilai_mahasiswa)
print("rata rata nilai per mahasiswa : ", average_Student)

averageAll = averageStudents(nilai_mahasiswa)
print("rata rata semua mahasiswa : ", averageAll)