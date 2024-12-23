import matplotlib.pyplot as plt

# Modifikasi data dengan menambahkan jumlah likes, comments, dan shares untuk setiap post
users = {
    'yudhi': {
        'profile': {'name': 'Yudhi', 'age': 21, 'bio': 'Student of Informatics'},
        'posts': [
            {'content': 'Hello, this is my first post!', 'likes': 50, 'comments': 10, 'shares': 5},
            {'content': 'I love programming!', 'likes': 80, 'comments': 20, 'shares': 10}
        ]
    },
    'elon': {
        'profile': {'name': 'Elon', 'age': 52, 'bio': 'CEO of SpaceX'},
        'posts': [
            {'content': 'I build SpaceX', 'likes': 100, 'comments': 50, 'shares': 20},
            {'content': 'We are going to Mars!', 'likes': 200, 'comments': 150, 'shares': 50}
        ]
    },
    'alex': {
        'profile': {'name': 'Alex', 'age': 23, 'bio': 'IT Student'},
        'posts': [
            {'content': 'info bang', 'likes': 200, 'comments': 52, 'shares': 30},
            {'content': 'kopag bang', 'likes': 250, 'comments': 250, 'shares': 55}
        ]
    }
}

# Data extraction for plotting
names = [users[user]['profile']['name'] for user in users]
likes = [sum(post['likes'] for post in users[user]['posts']) for user in users]
comments = [sum(post['comments'] for post in users[user]['posts']) for user in users]
shares = [sum(post['shares'] for post in users[user]['posts']) for user in users]


figure, sumbu = plt.subplots(2, 2, figsize=(12, 8))

# line plot
sumbu[0, 0].plot(names, likes, marker='o', color='b', linestyle='--', label='Likes')
sumbu[0, 0].set_title('Total Likes')
sumbu[0, 0].set_ylabel('Likes')
sumbu[0, 0].legend()

# scatter plot
sumbu[0, 1].scatter(comments, shares, c=['r', 'g', 'b'], s=100, alpha=0.7)
sumbu[0, 1].set_title('Comments & Shares')
sumbu[0, 1].set_xlabel('Comments')
sumbu[0, 1].set_ylabel('Shares')

# pie chart
sumbu[1, 0].pie(likes, labels=names, autopct='%1.1f%%', colors=['orange', 'purple', 'cyan'], startangle=140)
sumbu[1, 0].set_title('Likes Distribution')


sumbu[1, 1].bar(names, likes, color='blue', alpha=0.6)
sumbu[1, 1].set_title('Likes Bar Chart')
sumbu[1, 1].set_xlabel('Users')
sumbu[1, 1].set_ylabel('Likes')

# Adjust layout
plt.tight_layout()
plt.show()
