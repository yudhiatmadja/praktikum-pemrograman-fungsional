from functools import reduce

users = {
    'yudhi': {
        'profile': {
            'name': 'Yudhi',
            'age': '21',
            'bio': 'Student of Informatics'
        },
        'posts': [
            {'content': 'Hello, this is my first post!'},
            {'content': 'I love programming!'}
        ]
    },
    'elon': {
        'profile': {
            'name': 'Elon',
            'age': '21',
            'bio': 'CEO of SpaceX'
        },
        'posts': [
            {'content': 'I build SpaceX'},
            {'content': 'We are going to Mars!'}
        ]
    }
}

find_user = lambda users, name: users.get(name)

display_profile = lambda profile: f'Nama: {profile["name"]}\nUmur: {profile["age"]}\nBio: {profile["bio"]}'

display_posts = lambda posts: "--- Postingan ---\n" + "\n".join(map(lambda p, i: f'{i + 1}. {p["content"]}', posts, range(len(posts)))) if posts else "Tidak ada postingan."

contains_keyword = lambda post, keyword: keyword.lower() in post['content'].lower()

filterPost = lambda posts, keyword: list(filter(lambda post: contains_keyword(post, keyword), posts))

increment_count = lambda count, _: count + 1

count_total_posts = lambda posts: reduce(increment_count, posts, 0)


def search_user(users, name):
    user = find_user(users, name)
    if user:
        profile_info = display_profile(user['profile'])
        posts_info = display_posts(user['posts'])
        return f'{profile_info}\n\n{posts_info}'
    return f"Pengguna dengan nama '{name}' tidak ditemukan."


def main():
    while True:
        name = input("Masukkan nama pengguna yang ingin dicari: ")
        result = search_user(users, name)
        print(result)

        keyword = input("Masukkan kata kunci untuk filter postingan: ")
        user = find_user(users, name)
        if user:
            filtered_posts = filterPost(user['posts'], keyword)
            filtered_posts_info = display_posts(filtered_posts) if filtered_posts else "Tidak ada postingan yang sesuai."
            print(filtered_posts_info)

        if input("Ingin cari lagi? (y/n): ").lower() != "y":
            break


if __name__ == "__main__":
    main()
