import sys
import csv
import matplotlib.pyplot as plt

# The csv file is opened and data is stored in the km and price arrays. Any non-numeric
# row is basically ignored - and to match the subject, the file has to be named "data.csv".

def read_source_data():
	km = []
	price = []
	try:
		with open('data.csv', 'r') as csvfile:
			file = csv.reader(csvfile, delimiter=',')
			for row in file:
				if (len(row) == 2 and row[0].isnumeric() and row[1].isnumeric()):
					km.append(float(row[0]))
					price.append(float(row[1]))
	except IOError:
		print("\033[1;91mError: \033[0mCheck that [data.csv] dataset file exists and you have appropriate access rights.")
		sys.exit(1)
	return (km, price)

# Data is normalized for easier handling. Gradient descent will perform
# better this way rather than with the original values, whose ranges vary widely.
# The min-max normalization implemented here will bring that scale back to [0, 1].

def normalize_data(data):
	mini = min(data)
	maxi = max(data)
	result = []
	for elem in data:
		try:
			result.append((elem - mini) / (maxi - mini))
		except ZeroDivisionError:
			print("\033[1;91mError: \033[0mA whole field of the dataset inside [data.csv] is equal, which makes no sense for this algorithm.")
			sys.exit(1)
	return (result)

# Gradient descent algorithm 

def gradient_descent(x, y):
	m = len(x)
	iterations = 300
	learning_rate = 0.5
	t0 = 0.0
	t1 = 0.0
	for cycle in range(0, iterations):
		tmp_t0 = 0.0
		tmp_t1 = 0.0
		for i in range(0, m):
			tmp_t0 += t0 + (t1 * x[i]) - y[i]
			tmp_t1 += (t0 + (t1 * x[i]) - y[i]) * x[i]
		tmp_t0 = learning_rate * (1 / m) * tmp_t0
		tmp_t1 = learning_rate * (1 / m) * tmp_t1
		t0 -= tmp_t0
		t1 -= tmp_t1
	return (t0, t1)

# Saving the resulting variables t0 and t1 after training, for use in the estimation
# program.

def save_result(t0, t1):
	with open('theta.csv', 'w') as csvfile:
			file = csv.writer(csvfile, delimiter=',')
			file.writerow([t0, t1])

# Setting up the display using matplotlib. First plotting the points for each data
# element, then the estimation line obtained with the gradient descent algorithm.

def show_graph(x, y, t0, t1):
	plt.plot(x, y, linestyle="none", marker="+", label="Training dataset")
	plt.grid(True)
	plt.xlabel("Mileage (km)")
	plt.ylabel("Sale price ($)")
	plt.title("Estimated price based on given data")
	min_x = min(x)
	max_x = max(x)
	min_y = min(y)
	max_y = max(y)
	line_x = [min_x, max_x]
	line_y = []
	for point in line_x:
		normalized_x = (point - min_x) / (max_x - min_x)
		point = t1 * normalized_x + t0
		if (point != 0):
			denormalized_y = point * (max_y - min_y) + min_y
		else:
			denormalized_y = 0
		line_y.append(denormalized_y)
	plt.plot(line_x, line_y, 'tab:olive', label="Best fitting line")
	plt.legend()
	plt.show()

# Main function, obviously

def main(argv):
	km, price = read_source_data()
	if (len(km) < 2):
		print("\033[1;91mError: \033[0mDataset is not large enough for this to work!")
		sys.exit(1)
	x = normalize_data(km)
	y = normalize_data(price)
	t0, t1 = gradient_descent(x, y)
	save_result(t0, t1)
	if (len(argv) > 1 and argv[1] == "-v"):
		show_graph(km, price, t0, t1)

if __name__ == "__main__":
	main(sys.argv)