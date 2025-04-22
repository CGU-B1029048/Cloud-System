from pyfiglet import Figlet

def calculate_multiplies(digits_arr):
    ans = 0
    n = 0
    for digit in digits_arr:
        if digit == 'x':
            ans += n
            n = 0
        else:
            n = n*10 + digit
    return ans * n

def solve_slant(output):
    digits = []
    i = 0
    while i < len(output[4]):
        # print(i)
        # char is space -> 4 or 7
        if output[4][i] == ' ':
            #  check if last
            if not output[4][i:].strip():
                break
            #  solve 4
            if output[3][i+1] == '_':
                digits.append(4)
                i += 1
                while output[3][i] != '/':
                    i += 1
                if output[4][i] == '_':
                    i -= 1
                continue
            #  solve 7
            else:
                digits.append(7)
                cnt = 0
                while cnt < 2:
                    if output[4][i] == '/':
                        cnt += 1
                    i += 1
                if output[4][i] == '_':
                    i -= 1
                continue
        # char is \, -> 6, 8, 0
        if output[4][i] == '\\':
            #  solve 6
            if output[2][i+6] == '\\':
                digits.append(6)
                i += 6
                if output[4][i] == '_':
                    i -= 1
                continue
            #  solve 8
            if output[1][i+2] == '(':
                digits.append(8)
                i += 6
                if output[4][i] == '_':
                    i -= 1
                continue
            #  solve 0
            if output[1][i+7] == '\\':
                digits.append(0)
                i += 6
                if output[4][i] == '_':
                    i -= 1
                continue

        # char is /, -> 1, 2, 3, 5, 9, x
        if output[4][i] == '/':
            # if pattern /_/ -> 1, 7 or x
            if output[4][i:i+3] == '/_/':
                #  solve 1
                if output[1][i+2] == '<':
                    digits.append(1)
                    i += 3
                    if output[4][i] == '_':
                        i -= 1
                    continue
                #  solve 7
                if output[1][i] == '/':
                    digits.append(7)
                    i += 3
                    if output[4][i] == '_':
                        i -= 1
                    continue
                #  solve x
                if output[4][i+3] == '|':
                    digits.append('x')
                    i += 5
                    if output[4][i] == '|':
                        i += 1
                    continue
            #  solve 2
            if output[1][i+6] == '\\':
                digits.append(2)
                i += 6
                if output[4][i] == '_':
                    i -= 1
                continue                
            #  solve 3
            if output[2][i+6] == '<':
                digits.append(3)
                i += 6
                if output[4][i] == '_':
                    i -= 1
                continue     
            #  solve 5
            if output[2][i+7] == '\\':    
                digits.append(5)
                i += 7
                if output[4][i] == '_':
                    i -= 1
                continue             #  solve 9
            if output[3][i+4] == ',':
                digits.append(9)
                i += 6
                if output[4][i] == '_':
                    i -= 1
                continue

    # print(digits)
    return calculate_multiplies(digits)

def gen_slant_str(text):
    process = Figlet(font='slant')

    if not text:
        text = '1234567890x'
    output = process.renderText(text)

    out = []
    for line in str(output).splitlines():
        if line.strip():
            out.append(line)

    return out
def test():
    for a in range(100):
        for b in range(100):
        # print(gen_slant_str(f'{a}'))
            # if any(char in f'{a}x{b}' for char in box):
            #     continue
            ans = solve_slant(gen_slant_str(f'{a}x{b}'))
            if a*b != ans :
                print(f'incorrect, ans is {a}x{b}, solved {[str(t) for t in ans]}')
    
# print(solve_slant(gen_slant_str('17x1')))
# for line in gen_slant_str(''):
#     print(line)
# print('end')