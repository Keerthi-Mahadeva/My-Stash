def main():
    freq={}
    line = raw_input()
    while(line != 'quit'):
        words = line.split(' ')
        for word in words:
            freq[word] = freq.get(word,0) + 1
        line = raw_input()

    for word in freq:
        print (word + ' ' + freq[word] + ' times')

main()
