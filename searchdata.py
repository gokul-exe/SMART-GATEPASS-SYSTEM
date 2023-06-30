import csv

def binary_search_data(roll_number):
    with open('data.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        rows = list(csv_reader)

        left = 0
        right = len(rows) - 1

        while left <= right:
            mid = (left + right) // 2
            mid_roll_number = rows[mid]['Roll Number']

            if mid_roll_number == roll_number:
                return rows[mid]

            if mid_roll_number < roll_number:
                left = mid + 1
            else:
                right = mid - 1

    return None
if __name__=="__main__":
# Example usage
 roll_number = '19TH0405'
 result = binary_search_data(roll_number)


