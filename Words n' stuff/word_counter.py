
def WordCounter(msg):
    file = open(msg,'r')
    lines = file.read() #Opens and reads the file
    word = 0 
    msg_list = lines.split() #Turns it into a list
    for i in msg_list:
        if i in ['I',',',':',';','.']: #Exceptions
            continue
        word += 1
    num_lines = len(lines.split('\n'))
    #print(len(msg_list)) I could use this however it might count things that aren't words
    print(f'Number of words : {word}')
    print(f'Number of lines are : {num_lines}')
    file.close()

WordCounter('animals.txt')



