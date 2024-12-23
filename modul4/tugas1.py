from functools import reduce, wraps

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
contains_keyword = lambda post, keyword: keyword.lower() in post['content'].lower()
filter_post = lambda posts, keyword: list(filter(lambda post: contains_keyword(post, keyword), posts))
increment_count = lambda count, _: count + 1
count_total_posts = lambda posts: reduce(increment_count, posts, 0)
 
# Built-in Higher Order Function
display_posts = lambda posts: (
    "--- Postingan ---\n" +
    "\n".join(map(lambda p: f'{p["content"]}', posts))
    if posts else "Tidak ada postingan."
)

# Fungsi dengan Decorator
def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Menjalankan fungsi '{func.__name__}'...")
        result = func(*args, **kwargs)
        print(f"Fungsi '{func.__name__}' selesai dijalankan.\n")
        return result
    return wrapper

@log_execution
def search_user(users, name):
    user = find_user(users, name)
    if user:
        profile_info = display_profile(user['profile'])
        posts_info = display_posts(user['posts'])
        return f'{profile_info}\n\n{posts_info}'
    return f"Pengguna dengan nama '{name}' tidak ditemukan."

@log_execution
def search_and_filter_posts(users, name, keyword):
    user = find_user(users, name)
    if user:
        filtered_posts = filter_post(user['posts'], keyword)
        return display_posts(filtered_posts) if filtered_posts else "Tidak ada postingan yang sesuai."
    return f"Pengguna dengan nama '{name}' tidak ditemukan."

# Closure Implementation
def make_post_counter(users):
    """Closure untuk menghitung total postingan dari seluruh pengguna."""
    def count_all_posts():
        all_posts = [post for user in users.values() for post in user['posts']]
        return count_total_posts(all_posts)
    return count_all_posts

# Testing fungsi secara langsung
if __name__ == "__main__":
    # Menampilkan profil dan postingan pengguna
    print(search_user(users, 'yudhi'))
    print(search_user(users, 'elon'))
    
    # Filter postingan berdasarkan kata kunci
    print(search_and_filter_posts(users, 'elon', 'Mars'))
    
    # Menggunakan closure untuk menghitung total postingan
    count_posts = make_post_counter(users)
    print(f"Total semua postingan: {count_posts()}")
