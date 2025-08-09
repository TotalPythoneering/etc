# File: banner.py
# Console Message

prefix = \
   {1:"DEBUG", 2:"WARNING", 3:"ERROR", 4:"INFO"}
           
def message(which, message):
    # "sanity checking"
    if which < 1 or which > len(prefix)+1:
        which = 1
    print(prefix[which], message, sep=': ')


if __name__ == "__main__":
    for which in prefix.keys():
        message(which, "This is "
            + prefix[which].lower())

