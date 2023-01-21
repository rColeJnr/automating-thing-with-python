def collatz(num):
    if (num % 2 == 0): 
        result = num/2; print (f'{result}'); return result;
    else:
        result = num*3+1; print(result); return result

def main():
    try:
        num = int(input())
    except:
        print("enter a number")
        num = int(input())
    whatever = collatz(num)
    while whatever != 1:
        print(whatever)
        whatever = collatz(whatever)
    list = []
    list.append("object")

main()