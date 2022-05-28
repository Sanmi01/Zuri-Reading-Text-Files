import re
def read_file_content(filename):
    # [assignment] Add your code here 
    file = open(filename, "r")
    content = file.read()
    file.close()
    return content

def count_words():
    text = read_file_content("./story.txt")
    text = re.sub('[^A-Za-z0-9]', ' ', text)
    text = text.lower()
    text = text.strip()
    wordstring = text.split()

    word_count = {}
    for word in wordstring:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

print(count_words())