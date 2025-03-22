

def count_text_words(frankenstein):
        splt_list=frankenstein.split()

        num_words=0
        for words in splt_list:
            num_words+=1
        return f"Found {num_words} total words"


def count_char(frankenstein):
        txt=frankenstein

        counts = {}
        for char in txt:
            if char.isalpha():
                char = char.lower()
                counts[char] = counts.get(char, 0) + 1
        return counts
     


def sort_dict(counts):
    lst_tuples = [(i, j) for i, j in counts.items() if i.isalpha()]

    sorted_list = sorted(lst_tuples, key=lambda item: item[1], reverse=True)

    for char, count in sorted_list:
        print(f"{char}: {count}")

