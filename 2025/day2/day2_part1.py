# checking for invalid ids within id ranges given, sum all invalid ids
import sys

def main():
    try:
        with open("ids.txt", "r", encoding="utf-8") as f: # obtain id ranges from file
            id_ranges = f.read().split(",") 
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)

    invalid_total = 0 # to keep track of sum each invalid id 
   

    for interval in id_ranges:
        # number before '-' is beginning, number after '-' is end
        # start at the beginning > check if id valid, if not at end +1 and repeat
        
        interval = interval.strip()

        start = int(interval.split("-")[0])
        end = int(interval.split("-")[1])

        for test_id in range(start, end + 1):
            invalid_total += int(check_id(test_id))

    print(invalid_total)

def check_id(test_id):
    """ 
    Checks if the id is a repeating pattern of 2 numbers
    returns 0 if no patters, else returns the id
    """
    digits = len(str(test_id))

    if digits % 2 == 0:
        split = digits // 2
        
        return test_id if str(test_id)[:split] == str(test_id)[split:] else 0
    else:
        return 0


main()