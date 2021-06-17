import triangular_list

class Note:
    def __init__(self, content:str, tags:set) -> None:
        self.content = content
        self.tags = tags

    def __str__(self) -> str:
        return self.content
    
    def __repr__(self) -> str:
        return f'"{self.content}": {self.tags}'
    
class Book:
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
        self.len = 0
        self.notes = []
        self.tag_set = set()
        self.weights_table = triangular_list.Triangle(def_value=1)
        self.flag_make_new_weights_table = True
        self.last_ind = -1

    def __add__(self, note:Note) -> None:
        self.len += 1
        self.notes.append(note)
        self.tag_set.update(note.tags)
        self.weights_table.make_new_line()
        self.flag_make_new_weights_table = True
        return self
    
    def remove(self, ind:int) -> None:
        self.len -= 1
        self.notes.remove(ind)
        self.weights_table.remove_line()
        self.flag_make_new_weights_table = True

    def __getitem__(self, ind:int) -> None:
        return self.notes[ind]

    def __len__(self) -> int:
        return self.len

    def IoU(self, A:set, B:set):
        V = A.intersection(B)
        U = A.copy()
        U.update(B)
        return len(V)/len(U)

    def make_weights_table_between_notes(self):
        self.last_ind = len(self) - 1
        for i in range(self.len-1):
            for j in range(i+1, self.len):
                self.weights_table[i, j] = self.IoU(self.__getitem__(i).tags, self.__getitem__(j).tags)
                
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

class Library:
    def __init__(self) -> None:
        self.books = {}

    def __setitem__(self, title:str, book:Book) -> None:
        self.books[title] = book
    
    def __getitem__(self, title:str) -> Book:
        return self.books[title]
    
    def __repr__(self) -> str:
        str_res = ''
        for title in self.books:
            str_res += f"{title}: {len(self.books[title])}  "
        return str_res

if __name__ == '__main__':
    import doctest
    doctest.testmod()
