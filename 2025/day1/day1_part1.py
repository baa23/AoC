# determine password (number of times dial finishes on 0)

def main():   
    with open("rotations.txt", "r", encoding="utf-8") as f:  
        dial = 50      # dial starts on 50
        count = 0       # start with 0 hits

        # iterate through the rotations and move amount, note if finishing on 0
        for line in f:
            direction = line[0].upper()
            amount = int(line[1:])

            dial = turn_dial(dial, direction, amount)

            if dial == 0:
                count += 1

    print(count)

def turn_dial(d, dir, n):
    if dir == "R":
        d += n
        d = d % 100
        return d
    elif dir == "L":
        d -= n
        d = d % 100
        return d


if __name__ == "__main__":
    main()