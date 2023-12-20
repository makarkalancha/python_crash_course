def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # print(f"Sorry, the file {filename} does not exist.")
        """failing silently"""
        pass
    else:
        # Count the approximate number of words in the file
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")
    
filename = 'Crash_course/ch_10/books/alice.txt'
count_words(filename)
print("+++++++++++++++++++++++++++++")
filenames = ['Crash_course/ch_10/books/alice.txt', 
             'Crash_course/ch_10/books/siddhartha.txt',
             'Crash_course/ch_10/books/moby_dick1.txt',
             'Crash_course/ch_10/books/little_women.txt']
for filename in filenames:
    count_words(filename)
