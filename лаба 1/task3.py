list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

print("Общее количество игроков:", len(list_players))

one = list_players[::2]
print("Первая команда:", one)
two = list_players[::-2]
print("Вторая команда:", two)
# индекс середины
middle_index = len(list_players) // 2

first_team = list_players[:middle_index]
second_team = list_players[middle_index:]

print(first_team)
print(second_team)
