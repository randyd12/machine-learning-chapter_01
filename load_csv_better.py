# Example of loading Pima Indians CSV dataset
from csv import reader

# Load a CSV file
def load_csv(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				blank_row_count += 1
				continue
			dataset.append(row)
	return dataset

# Load dataset
filename = 'pima-indians-diabetes.csv'
dataset = load_csv(filename)
blank_row_count=0
print('Loaded data file {0} with {1} rows and {2} columns.  Blanks: {3}'.format(filename, len(dataset), len(dataset[0]), blank_row_count))
print(dataset[0])
