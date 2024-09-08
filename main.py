# Keshav Santhanam
# 9-7-2024
# 1, 7, 16, 35

# Wozniak spaced repetition algorithm 
date_progression = [1, 7, 16, 35]
daily_limit = 3
inputs = [1,2,3,4,5,6,7,8,9,10,11,12]
days = [""] * 365
data_to_next_date = {}
for input in inputs:
	data_to_next_date[input] = [0, date_progression[0]]
data_to_repeat_dates = {}

for current_date in range(len(days)):
	while len(days[current_date]) < daily_limit:
		# inserting repeated info
		for input, next_date in data_to_next_date.items():
			if next_date == current_date:
				days[current_date] += str(input)
		# inserting new info
		for input in inputs:
			days[current_date] += str(input)
			# adjusting next deadline
			data_to_next_date[input][0] += 1
			data_to_next_date[input][1] = date_progression[data_to_next_date[0]] + current_date
	

		
	

