def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    list_chars = dict_to_list(num_chars)
    ordered_list = order_list(list_chars)
    

    print("--- Begin report of ", book_path," ---")
    print(f"{num_words} words found in the document")
    ordered_list
    print("--- End report ---")

def order_list(list):
    list.sort(key=lambda x: x["num"], reverse=True) # sorts the list based on the num (2nd thing in the list)
    
    for char in list:
        letter = char["letter"]
        count = char["num"]
        print(f"The '{letter}' character was found {count} times")
        

def dict_to_list(dict):
    list = [{"letter": char, "num": count} for char, count in dict.items()] # magic line: it takes a dictionary with key-value pairs, takes the key and names it char, value is count, and then creates a list with letter = char and num = count
    return list

def get_num_chars(text):
    count = {} # empty dictionary
    lowered_text = text.lower() # make input lowercase

    for char in lowered_text: # iterate over each character in the text
        if char.isalpha(): # make sure the character is in the alphabet
                if char in count: # if the character already exists in dictionary, increase number
                    count[char] += 1
                else: # if character doesn't already exist in dictionary, set number to 1
                    count[char] = 1
    return count

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()