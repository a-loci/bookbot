def count_text_words(file_path):
    with open(file_path,"r") as file:
        splitter= file.read()
        splt_list=splitter.split()

    num_words=0
    for words in splt_list:
        num_words+=1
    return f"{num_words} words found in the document"