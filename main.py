# Keshav Santhanam
# 9-7-2024
# 1, 7, 16, 35

# Wozniak spaced repetition algorithm 
date_progression = [1, 7, 16, 35]
daily_limit = 9
inputs = [1,2,3,4,5,6,7,8,9,10,11,12]
days = [""] * 30
data_to_next_date = {}
for input in inputs:
	data_to_next_date[input] = [0, date_progression[0]]
data_to_repeat_dates = {}

for current_date in range(len(days)):
    # inserting new info
	for input in inputs:
		if len(days[current_date]) < daily_limit:
			days[current_date] += str(input) + ", "
			# adjusting next deadline
			data_to_next_date[input][0] += 1
			current_date_increment = data_to_next_date[input][0] if data_to_next_date[input][0] <= 3 else 3
			data_to_next_date[input][1] = date_progression[current_date_increment] + current_date
    
	# inserting repeated info
	for input, next_date in data_to_next_date.items():
		if len(days[current_date]) < daily_limit:
			if next_date[1] <= current_date:
				days[current_date] += str(input) + ", "
				print("here", days[current_date])
				data_to_next_date[input] = [next_date[0] + 1, date_progression[next_date[0] + 1]]
		

# print out the resulting problems to solve on each given day
for i, day in enumerate(days):
    print("Day", i + 1, "= ", day)
    
	

		
	

