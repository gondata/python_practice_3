import sys

if len(sys.argv) == 3:
    text = sys.argv[1]      # 0 is the file name
    repetitions = int(sys.argv[2])
    for r in range(repetitions):
        print(text)

else:
    print('Error')