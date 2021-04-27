import sys
import csv
import math
from training import read_source_data
import matplotlib.pyplot as plt

# The csv file is opened to get the t0 and t1 values. If the file doesn't exist or is un-openable,
# the values are set to default (0.0) and a warning message is displayed.

def read_thetas():
	t0 = 0.0
	t1 = 0.0
	try:
		with open('theta.csv', 'r') as csvfile:
			file = csv.reader(csvfile, delimiter=',')
			first_row = next(file)
			if (first_row):
				t0 = float(first_row[0])
				t1 = float(first_row[1])
	except IOError as err:
		print("\033[1;91mWarning: \033[0mCheck that [theta.csv] file exists and you have appropriate access rights. Defaulting to 0.0 value for theta variables.")
	except ValueError:
		print("\033[1;91mError: \033[0m[theta.csv] file seems to be containing incorrect values. Defaulting to 0.0 value for theta variables.")
	return (t0, t1)

# Getting user input for the mileage of the car whose price is to be estimated by the program.

def get_mileage():
	try:
		user_input = input("Please enter the car's mileage: ")
		mileage = float(user_input)
		if (mileage < 0):
			print("\033[1;91mError: \033[0mThe mileage of your car can't be a negative, you cheater!\n")
			mileage = get_mileage()
		if (mileage > 4890993):
			print("\033[1;91mError: \033[0mThe mileage of your car is impossibly high, please try something smaller.\n")
			mileage = get_mileage()
	except ValueError:
		print("\033[1;91mError: \033[0mThe mileage of the car can only contain numbers, obviously...\n")
		mileage = get_mileage()
	except:
		print("Error while getting input. Exiting program.")
		sys.exit(1)
	return (mileage)

# Estimating the price very simply, basically searching for the corresponding point on the
# line and dealing with normalization.

def estimate_price(t0, t1, mileage, km, price):
	min_km = min(km)
	max_km = max(km)
	min_price = min(price)
	max_price = max(price)
	normalized_mileage = (mileage - min_km) / (max_km - min_km)
	normalized_price = t0 + t1 * normalized_mileage
	if (normalized_price != 0):
		real_price = normalized_price * (max_price - min_price) + min_price
	else:
		real_price = 0
	return (real_price)

# Price is displayed ine a rounded form.

def display_price(value):
	print("The estimated value of this car is \033[1;94m" + str(round(value)) + "\033[0m $.")
	if (value < 0):
		print("In other words, \033[1;91mdo not buy this car.\033[0m")

# Setting up the display using matplotlib. Plotting the points for each training data
# element as a [+], then the user's request as a [o], and the estimation line obtained with
# the gradient descent algorithm.

def show_graph(x, y, t0, t1, mileage, estimated_value):
	plt.plot(x, y, linestyle="none", marker="+", label="Training data")
	plt.plot([mileage], [estimated_value], 'tab:olive', linestyle="none", marker="d", label="User's car")
	plt.grid(True)
	plt.xlabel("Mileage (km)")
	plt.ylabel("Sale price ($)")
	plt.title("Estimated price based on given data")
	line_x = [min(x), max(x)]
	line_y = [estimate_price(t0, t1, line_x[0], x, y), estimate_price(t0, t1, line_x[1], x, y)]
	plt.plot(line_x, line_y, 'tab:olive', label="Price estimation line")
	plt.legend()
	plt.show()

# Main function

def main(argv):
	t0, t1 = read_thetas()
	km, price = read_source_data()
	mileage = get_mileage()
	value = estimate_price(t0, t1, mileage, km, price)
	display_price(value)
	if (len(argv) > 1 and argv[1] == "-v"):
		show_graph(km, price, t0, t1, mileage, value)

if __name__ == "__main__":
	main(sys.argv)