
def rev_sentence(sentence): 
    
    reverse_sentence = ''.join(reversed(sentence)) 
  
    return reverse_sentence.capitalize()
  
if __name__ == "__main__": 
    input = 'I Love Bangladesh'
    words = input.split(' ')
    for i in range(len(words)):
        print(rev_sentence(words[i]),end =" ")