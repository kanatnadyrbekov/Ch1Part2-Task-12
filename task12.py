# Given a string that may or may not contain a letter of interest. 
# Print the index location of the first and last appearance of f. 
# If the letter f occurs only once,then output its index.
# If the letter f does not occur, then do not print anything.
# Don't use loops in this task.

sentence = input("Hello my friend: ")
letter = sentence.count("f")

if "f" not in sentence:
    print("none")
if "f" in sentence:
    if letter == 1:
        print(sentence.index("f"))
    else:
        print(sentence.index("f"))
        print(sentence.rindex("f"))


