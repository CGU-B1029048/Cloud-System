from pyfiglet import Figlet
from slant import solve_slant
import sys
import random
import subprocess

def banner_digit(digit):
    if digit[3][1:6] == '#####':
        if digit[4][6] == ' ':
            return 2
        if digit[1][6] == ' ':
            return 5
        if digit[2][6] == ' ':
            return 6
        if digit[2][0] == ' ':
            return 3
        if digit[2][6] == ' ':
            return 6
        if digit[4][0] == ' ':
            return 9
        return 8
    if all([digit[i][2] == '#' for i in range(7)]):
        return 1
    if digit[4] == '#######':
        return 4
    if all([digit[i][6-i] == '#' for i in range(1,5)]):
        return 7
    if all([digit[1][1] == '#', digit[1][5] == '#', digit[5][1] == '#', digit[5][5] == '#']):
        return 0
    return -1

def solve_banner(output):
    digits = []
    prev = -1
    for index in range(len(output[0])):
        if not ''.join([output[i][index] for i in range(7)]).strip():
            if index and ((index - prev) > 1):
                digits.append([line[prev+1:index] for line in output])
            prev = index

    num = 0
    ans = 0
    for digit in digits:
        if all([digit[i][j] == '#' for i in range(3,5) for j in range(2,4)]):
            ans += num
            num = 0

        else:
            num = num*10 + banner_digit(digit)
    print(f'{ans}*{num}')
    return ans * num

def solve_and_submit(payer):
    # for i in range(10):
    # a = random.randint(1,99)
    # b = random.randint(1,99)
    # equation = f'{a}x{b}'
    # equation = '1234567890x'
    # process = subprocess.Popen(['figlet', '-f', 'banner', equation], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    while True:
        process = subprocess.Popen(['./app_mining', payer], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        try:
            while True:
                output = []
                while True:
                    line = process.stdout.readline()
                    if line.strip():
                        output.append(line)
                        print(line, end='')
                    else:
                        break
                print(f'len of output:{len(output)}')
                if len(output) == 5:
                    ans = solve_slant(output)
                    process.stdin.write(f'{ans}\n')
                    process.stdin.flush()
                    print('=======')
                    print(process.stdout.readline())
                if '#' in ''.join(output):
                    ans = solve_banner(output)
                    # out, _ = process.communicate(input=f'{ans}')
                    process.stdin.write(f'{ans}\n')
                    process.stdin.flush()
                    print('=======')
                    print(process.stdout.readline())
                    # test = []
                    # while True:
                    #     out = process.stdout.readline()
                    #     if out.strip():
                    #         test.append(out)
                    #         print(out, end='')
                    #     else :
                    #         break
                    # print(test)
                    # print('=======')
                    # process.kill()
                    # process.wait()
                else:
                    print("Restarting process...")
                    process.kill()
                    process.wait()
                    break
        except Exception as e:
            print(f"Error: {e}")
            process.kill()
            process.wait()
    # process.wait()
if __name__ ==  '__main__':
    if len(sys.argv) != 2:
        print("Usage: python banner.py <miner>")
        sys.exit(1)
    payer = sys.argv[1].lower()
    solve_and_submit(payer)

