"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open('task2.txt') as f:
    rows = f.readlines()
    expanded_rows = [row.split() for row in rows]

rows_count, words_count = len(rows), sum([len(word_list) for word_list in expanded_rows])

print(f"Строк в файле - {rows_count}, "
      f"Слов в файле - {words_count}")