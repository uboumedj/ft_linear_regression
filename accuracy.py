import sys
import csv
from training import read_source_data
from estimation import read_thetas, estimate_price

# Computing the coefficient of determination, a statistic meant to represent how well
# the model fits the real data.

def calculate_accuracy(t0, t1, km, price):
	length = len(price)
	mean = sum(price) / length
	ss_tot = 0
	ss_res = 0
	for i in range(length):
		ss_tot += pow(price[i] - mean, 2)
		estimated = estimate_price(t0, t1, km[i], km, price)
		ss_res += pow(price[i] - estimated, 2)
	try:
		coeff_determination = 1 - (ss_res / ss_tot)
	except ZeroDivisionError:
		print("\033[1;91mError: \033[0mData inside [data.csv] seems to be invalid for this operation.")
		sys.exit(1)
	return(coeff_determination)

# Display function with a little bit of color variation depending on accuracy

def display_accuracy(accuracy):
	print("The coefficient of determination of the linear regression algorithm on the dataset [data.csv] is \033[1;94m" + str(accuracy) + "\033[0m.")
	color = "\033[1;94m"
	if (accuracy > 0.7):
		color = "\033[1;92m"
	elif (accuracy < 0.5):
		color = "\033[1;91m"
	print("It basically means that the resulting linear function has an accuracy of approx. " + color + str(round(accuracy * 100)) + "%\033[0m.")

# Main function

def main(argv):
	t0, t1 = read_thetas()
	km, price = read_source_data()
	accuracy = calculate_accuracy(t0, t1, km, price)
	display_accuracy(accuracy)

if __name__ == "__main__":
	main(sys.argv)