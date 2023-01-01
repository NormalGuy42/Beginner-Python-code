#First design
def binary_to_deci():
    #Ask for input
    binary = input("Enter your binary number: ")
    #Turn input into list to get indices
    b_list = list(binary)

    #Variables that get iterated
    pow = len(b_list) - 1
    num = 0
    ans = 0
    result = 0
    for i in range(len(b_list)):
        i = int(b_list[num])
        ans = i * (2**pow)
        num = num + 1
        pow = pow - 1
        #results get added as the code is iterated
        result = result + ans
    print(result)

#Designed using Python Guide
def betterStringBinary():
   binary_num = int(input("Enter the Binary Number: "))
   dec_num = 0
   m = 1
   length = len(str(binary_num))

   for k in range(length):
        reminder = binary_num % 10
        print(reminder,"reminder")
        dec_num = dec_num + (reminder * m)
        print(dec_num,"dec_num")
        m = m * 2
        binary_num = int(binary_num/10)

   print("Equivalent Decimal Value = ", dec_num)

#Inbuilt function
def BinaryToDecimal(n):
    dec_number= int(str(n),2)
    print('The decimal conversion is:', dec_number)

#Turns decimal numbers into binary
def DecimalToBinary(num):
    #This program divides by 2 and notes the remainder as long as the 
    #number is bigger than 1
   if num > 1:
      DecimalToBinary(num // 2)
   print(num % 2, end = '')

betterStringBinary()



