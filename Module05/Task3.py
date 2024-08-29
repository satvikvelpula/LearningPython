while True:
     try:
         number = int(input("Enter a number: "))

         if number >= 1:
             for i in range(2, (number // 2) + 1):
                 if number % i == 0:
                     print(f'{number} is not a prime number. ')
                     break
             else:
                 print(f'{number} is a prime number.')
     except ValueError:
         break