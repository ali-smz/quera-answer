n = int(input())
movies = []

for i in range(n):
    movie = input()
    movies.append(movie.title())

print('\n'.join(movies))
