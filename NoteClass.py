import triangular_list

class Note:
    def __init__(self, content:str, tags:set) -> None:
        self.content = content
        self.tags = tags

class Book:
    def __init__(self) -> None:
        self.len = 0
        self.notes = []
        self.tag_set = set()
        self.weights_table = triangular_list.Triangle(self.len)
        self.make_new_weights_table = True

    def __add__(self, note:Note) -> None:
        self.len += 1
        self.notes.append(note)
        self.tag_set.update(note.tags)
        self.weights_table.make_new_line()
        self.make_new_weights_table = True
        return self
    
    def remove(self, ind:int) -> None:
        self.len -= 1
        self.notes.remove(ind)
        self.weights_table.remove_line()
        self.make_new_weights_table = True

    def __getitem__(self, ind:int) -> None:
        return self.notes[ind]

    def __len__(self) -> int:
        return self.len

    def IoU(A:set, B:set):
        V = len(A.intersection(B))
        U = len(A.update(B))
        return V/U

    def make_weights_table_between_notes(self):
        for i in range(self.l-1):
            for j in range(i+1, self.l):
                self.weights_table[i, j] = self.IoU(self.__getitem__(i), self.__getitem__(j))

    def next_note(self, ind:int):
        """
        ind - start index
        """
        if self.make_new_weights_table:
            self.make_weights_table_between_notes()
            self.make_new_weights_table = False
        max_weight = False
        res_ind = 0
        for i in range(self.l):
            if i == ind:
                continue
            if not max_weight or max_weight < self.weights_table[ind, i]:
                max_weight = self.weights_table[ind, i]
                res_ind = i
        self.weights_table[ind, res_ind] -= 1
        return res_ind
class Library:
    def __init__(self) -> None:
        self.books = {}

    def __setitem__(self, title:str, book:Book) -> None:
        self.books[title] = book
    
    def __getitem__(self, title:str) -> Book:
        return self.books[title]
    
    def __str__(self) -> str:
        str_res = ''
        for title in self.books:
            str_res += f"{title}: [{len(self.books[title])}]\n"
        return str_res[:-1] #removes the last line break
        
if __name__ == '__main__':
    My_library = Library()
    My_library['Q'] = Book()
    print(My_library)
    My_library['Q'] += Note('wasd', set('q w e r'.split()))
    print(My_library)
