def count_words_of_length(string, m):
    words = string.split()
    count = sum(1 for word in words if len(word) == m)
    return count

input_string = input("enter root : ")
m = int(input("enter number whidh : "))

word_count = count_words_of_length(input_string, m)
print(f"whith word=m {m} : {word_count}")
