
users = {
    '066': {
        'password': '123',
        'profile': {
            'name': 'Yudhi',
            'age': '21',
            'bio': 'Student of Informatics'
        },
        'posts': [
            {'nim': '066', 'content': 'Hello, this is my first post!'}
        ]
    },
    '321': {
        'password': '321',
        'profile': {
            'name': 'elon musk',
            'age': '21',
            'bio': 'CEO of SpaceX'
        },
        'posts': [
            {
                'nim': '321',
                'content': 'I build spaceX'
            }
        ]
    }
}

friends = {
    '066': ['321'], 
    '321': ['066']   
}

posts = [
    {'nim': '066', 'content': 'Hello, this is my first post!'},
    {'nim': '321', 'content': 'I build spaceX'}
 
]


def register():
    nim = input("Masukkan NIM: ")
    if nim in users:
        print("NIM sudah terdaftar!")
        return
    
    password = input("Masukkan password: ")
    users[nim] = {'password': password, 'profile': {}, 'posts': []}
    friends[nim] = [] 
    print("Registrasi berhasil!")
    is_skip = input("Apakah Anda ingin mengisi profil sekarang? (y/n): ")
    if is_skip.lower() == 'y':
        IsiProfile(nim)


def login():
    nim = input("Masukkan NIM: ")
    password = input("Masukkan password: ")
    
    if nim in users and users[nim]['password'] == password:
        print("Login berhasil!")
        user_menu(nim)
    else:
        print("NIM atau password salah!")


def IsiProfile(nim):
    name = input("Masukkan nama: ")
    age = input("Masukkan umur: ")
    bio = input("Masukkan bio singkat: ")
    users[nim]['profile']['name'] = name
    users[nim]['profile']['age'] = age
    users[nim]['profile']['bio'] = bio
    print("Profil berhasil diperbarui!")

def create_post(nim):
    post_content = input("Tulis postingan Anda: ")
    post = {'nim': nim, 'content': post_content}
    users[nim]['posts'].append(post)  
    posts.append(post)  
    print("Postingan berhasil dibuat!")


def view_posts():
    if not posts:
        print("Belum ada postingan.")
    else:
        print("\n--- Postingan Terbaru ---")
        for index, post in enumerate(posts):
            user_name = users[post['nim']]['profile']['name']
            print(f"{index + 1}. {user_name}: {post['content']}")


def add_friend(nim):
    friend_nim = input("Masukkan NIM teman yang ingin ditambahkan: ")
    if friend_nim in users and friend_nim != nim:
        friends[nim].append(friend_nim)
        print(f"Teman dengan NIM {friend_nim} berhasil ditambahkan!")
    else:
        print("NIM tidak valid")


def view_friends(nim):
    if not friends[nim]:
        print("Anda belum memiliki teman.")
    else:
        print("\n--- Friend List ---")
        for friend_nim in friends[nim]:
            print(f"- {users[friend_nim]['profile']['name']}")


def user_menu(nim):
    while True:
        print("\n--- Menu Pengguna ---")
        print("1. Lihat Profil")
        print("2. Edit Profil")
        print("3. Buat Postingan")
        print("4. Lihat Postingan Global")
        print("5. Tambah Teman")
        print("6. Lihat Daftar Teman")
        print("7. Logout")
        
        choice = input("Pilih menu: ")
        
        if choice == '1':
            print("Profil:", users[nim]['profile'])
        elif choice == '2':
            IsiProfile(nim)
        elif choice == '3':
            create_post(nim)
        elif choice == '4':
            view_posts()
        elif choice == '5':
            add_friend(nim)
        elif choice == '6':
            view_friends(nim)
        elif choice == '7':
            print("Logout berhasil!")
            break
        else:
            print("Pilihan tidak valid!")


def main():
    while True:
        print("\n--- Aplikasi Sosial Media ---")
        print("1. Register")
        print("2. Login")
        print("3. Keluar")
        
        choice = input("Pilih menu: ")
        
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Terima kasih telah menggunakan aplikasi ini!")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
