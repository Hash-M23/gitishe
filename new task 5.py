my_list = [5, 4, 3, 2, 1]
print(f"Рейтинг - {my_list}")
num = int(input("Введите число что бы поставить оценку"))
print("Введите 100 - что бы выйти")
while num != 100:
	for el in range(len(my_list)):
		if my_list[el] == num:
			my_list.insert(el + 1, num)
			break
		elif my_list[0] < num:
			my_list.insert(0, num)
		elif my_list[-1] > num:
			my_list.append(num)
		elif my_list[el] > num and my_list[el + 1] < num:
			my_list.insert(el + 1,num)
	print(f"Текущий список - {my_list}")
	num = int(input("Введите число"))