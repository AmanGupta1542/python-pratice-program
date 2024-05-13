
class Fibonacci:
    def __init__(self) -> None:
        self.first = 0
        self.second = 1
        self.count = 2
    def using_for_loop(self, loop_count):
        print(self.first)
        print(self.second)
        for i in range (loop_count-2):
            next = self.first + self.second
            self.first = self.second
            self.second = next
            print(next)

    def using_recursion(self, loop_count):
        print(self.first)
        print(self.second)
        def fibonacci_recursion():
            if self.count < loop_count:
                next = self.first + self.second
                self.first = self.second
                self.second = next
                print(next)
                self.count += 1
                fibonacci_recursion()
            else:
                return
        fibonacci_recursion()

    def get_nth_fibonacci_number(self, n):
        def F(n):
            if n <= 1:
                return n
            else:
                return F(n - 1) + F(n - 2)
            
        print(F(n))
        

fibonacci_obj = Fibonacci()

print(''' 
    Plese choose one of the following options:
    1. Fibonacci number till n using for loop
    2. Fibonacci number till n using for recursion
    3. Get nth Fibonacci number
 ''')

choice = input("Enter your choice (1, 2 or 3) : ")

try:
    number = int(input("Enter a number : "))
except ValueError:
    print("Please enter a number")
    exit(1) # The exit(1) command indicates that the program encountered an error and did not complete successfully.
except Exception as e:
    print("Unknown exception occurred : ", e)
    exit(1)


print('choice is ', choice)
if choice == '1':
    fibonacci_obj.using_for_loop(number)
elif choice == '2':
    fibonacci_obj.using_recursion(number)
elif choice == '3':
    fibonacci_obj.get_nth_fibonacci_number(number)
else:
    print("Invalid choice number")
