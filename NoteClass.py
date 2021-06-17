import triangular_list

class Note:
    def __init__(self, content:str, tags:set) -> None:
        self.content = content
        self.tags = tags

    def __str__(self) -> str:
        return self.content
    
    def __repr__(self) -> str:
        return f'"{self.content}": {self.tags}'
    
class Book(list):
    """
    >>> A_book = Book()
    >>> A_book += Note("a", {1, 2, 3})
    >>> A_book += Note("b", {3, 4, 5})
    >>> A_book += Note("c", {2, 3, 4})
    >>> A_book.make_weights_table_between_notes()
    >>> A_book.weights_table
        0, 1, 2
    0 | #
    1 | 0.2  #
    2 | 0.5, 0.5  #
    >>> A_book.get_next_note()
    "a": {1, 2, 3}
    >>> A_book.weights_table
        0, 1, 2
    0 | #
    1 | 0.2  #
    2 | -0.5, 0.5  #
    >>> A_book += Note("d", {1, 5})
    >>> A_book.make_weights_table_between_notes()
    >>> A_book.weights_table
        0, 1, 2, 3
    0 | #
    1 | 0.2  #
    2 | 0.5, 0.5  #
    3 | 0.25, 0.25, 0.0  #
    >>> print(A_book.get_next_note())
    a
    >>> print(A_book.get_next_note())
    c
    >>> print(A_book.get_next_note())
    b
    >>> print(A_book.get_next_note())
    d
    """
    def __init__(self) -> None:
        super().__init__()
        self.tag_set = set()
        self.weights_table = triangular_list.Triangle(def_value=1)
        self.flag_make_new_weights_table = True
        self.last_ind = -1

    def __iadd__(self, note:Note) -> None:
        self.append(note)
        self.tag_set.update(note.tags)
        self.weights_table.make_new_line()
        self.flag_make_new_weights_table = True
        return self
    
    def del_note(self, ind:int) -> None:
        del self[ind]
        self.weights_table.del_line()
        self.flag_make_new_weights_table = True

    def IoU(self, A:set, B:set):
        V = A.intersection(B)
        U = A.copy()
        U.update(B)
        return len(V)/len(U)

    def make_weights_table_between_notes(self):
        self.last_ind = len(self) - 1
        for i in range(len(self)-1):
            for j in range(i+1, len(self)):
                self.weights_table[i, j] = self.IoU(self[i].tags, self[j].tags)
                
    def get_next_note(self, ind:int=None):
        """
        ind - start index
        """
        if not ind:
            ind = self.last_ind
        if self.flag_make_new_weights_table:
            self.make_weights_table_between_notes()
            self.flag_make_new_weights_table = False
        max_weight = False
        for i in range(len(self)):
            if i == ind:
                continue
            if not max_weight or max_weight < self.weights_table[ind, i]:
                max_weight = self.weights_table[ind, i]
                self.last_ind = i
        self.weights_table[ind, self.last_ind] -= 1
        return self[self.last_ind]

class Library(dict):
    """
    Library["title"][id notes]

    >>> My_library = Library()
    >>> My_library.make_new_book('A')
    >>> My_library.make_new_book('B')
    >>> My_library.make_new_book('C')

    >>> My_library['A'] += Note('qwerty', {2, 3, 4})
    >>> My_library['B'] += Note('wasd', {4, 5, 6})
    >>> My_library['B'] += Note('ijkl', {5, 6, 7})

    >>> print(repr(My_library))
    A: 1  B: 2  C: 0  
    """
    def __repr__(self) -> str:
        str_res = ''
        for title in self:
            str_res += f"{title}: {len(self[title])}  "
        return str_res
    
    def make_new_book(self, title):
        self[title] = Book()

if __name__ == '__main__':
    import doctest
    doctest.testmod()
