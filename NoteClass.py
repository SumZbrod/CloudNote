class Note:
    def __init__(self, content:str, tags:set) -> None:
        self.content = content
        self.tags = tags

class Book:
    def __init__(self) -> None:
        self.len = 0
        self.notes = []
        self.tag_set = set()
    
    def __add__(self, note:Note) -> None:
        self.len += 1
        self.notes.append(note)
        self.tag_set.update(note.tags)
        return self
    
    def remove(self, ind:int) -> None:
        self.len -= 1
        self.notes.remove(ind)

    def __getitem__(self, ind:int) -> None:
        return self.notes[ind]

    def __len__(self) -> int:
        return self.len

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
