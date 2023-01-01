
#This was my first attempt
def reverse(msg):
    #original message
    out = []
    var = len(msg)
    num = 0
    #These are important variables
    #out is an empty list for which I can append letters later on
    #var allows me to set the number of iterations for the for loop
    #num allows me to pick negative indexes which mean I can pick letters at end of string
    for num in range(var):
        num = -num - 1
        out.append(msg[num])
        #I append the letter to a lisy
    print("".join(out))



#Slice notation is the fastest way to do this
def splice_reversed(msg):
    print(msg[::-1])

#reverse command
def reverse_command(msg):
    return print("".join(reversed(msg)))



#Improved reverse function
def reverse_for(msg):
    result = ""
    for i in msg:
        result = i + result
    print(result)

reverse("Python")
reverse_for("Python")
reverse_command("Python")
splice_reversed("Python")



    

    
