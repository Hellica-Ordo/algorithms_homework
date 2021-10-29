"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою!!! версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.

2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.
"""
from collections import Counter, deque

huffman_table = {}

class HuffmanCoding:

    def __init__(self, my_string):
        self.my_string = my_string
        self.tree = self.huffman_tree()
        self.code = self.huffman_coding(self.tree)
        self.str = self.string_code()

    def huffman_tree(self):
        symbols_count = Counter(self.my_string)     # частота появления символов в строке
        sorted_symbols = deque(sorted(symbols_count.items(), key = lambda item: item[1]))   # пока что отсортированный словарь от Counter
        if len(sorted_symbols) != 1:
            while len(sorted_symbols) > 1:          # построение дерева
                sum_priorities = sorted_symbols[0][1] + sorted_symbols[1][1]
                combined = {0: sorted_symbols.popleft()[0], 1: sorted_symbols.popleft()[0]}
                for i, j in enumerate(sorted_symbols):
                    if sum_priorities > j[1]:
                        continue
                    else:
                        sorted_symbols.insert(i, (combined, sum_priorities))
                        break
                else:
                    sorted_symbols.append((combined, sum_priorities))

        else:
            sum_priorities = sorted_symbols[0][1]
            combined = {0: sorted_symbols.popleft()[0], 1: None}
            sorted_symbols.append((combined, sum_priorities))

        return sorted_symbols[0][0]     # а это уже дерево целиком должно быть

    def huffman_coding(self, tree, path = ''):
        if not isinstance(tree, dict):  # isinstance проверяет принадлежность данных к определённому типу данных/типу данных из кортежа из аргументов
            huffman_table[tree] = path
        else:
            self.huffman_coding(tree[0], path = f"{path}0")     # непосредственно кодирование в последовательность 0 и 1
            self.huffman_coding(tree[1], path = f"{path}1")
        return huffman_table

    def string_code(self, coded_str =''):
        for i in self.my_string:
            coded_str += f'{self.code[i]} '
        return coded_str


test_string = "Hello world!"
test_func = HuffmanCoding(test_string)
print(test_func.str)