# determine password (number of times dial finishes on 0)

def main():   
    with open("rotations.txt", "r", encoding="utf-8") as f:  
        d = 50      # dial starts on 50
        z = 0       # start with 0 hits

        # iterate through the rotations and move amount, note passes through 0
        for line in f:
            direction = line[0].upper()
            amount = int(line[1:])

            step = 1 if direction == "R" else -1

            for _ in range(amount):
                d = (d + step) % 100
                if d == 0:
                    z += 1
    print(z)


if __name__ == "__main__":
    main()