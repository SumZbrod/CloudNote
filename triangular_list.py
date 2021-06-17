class Triangle:
    """
    Square commutative list implemented via triangular list
    >>> A = Triangle()
    >>> A.triangle_list
    []
    >>> A.make_new_line()
    >>> A.triangle_list
    []
    >>> A[0, 0]
    0
    >>> A.make_new_line()
    >>> A.triangle_list
    [[0]]
    >>> A = Triangle(5)
    >>> A.set_position((2, 3))
    (2, 2)
    >>> A.set_position((3, 2))
    (2, 2)
    >>> A[2, 3] = 1
    >>> A[2, 3]
    1
    >>> A[3, 2]
    1
    >>> A
        0, 1, 2, 3, 4
    0 | #
    1 | 0  #
    2 | 0, 0  #
    3 | 0, 0, 1  #
    4 | 0, 0, 0, 0  #
    >>> A.make_new_line()
    >>> A
        0, 1, 2, 3, 4, 5
    0 | #
    1 | 0  #
    2 | 0, 0  #
    3 | 0, 0, 1  #
    4 | 0, 0, 0, 0  #
    5 | 0, 0, 0, 0, 0  #
    >>> A.remove_line()
    >>> A
        0, 1, 2, 3, 4
    0 | #
    1 | 0  #
    2 | 0, 0  #
    3 | 0, 0, 1  #
    4 | 0, 0, 0, 0  #
    """
    def __init__(self, len=0, def_value=0):
        self.len = len
        self.def_value = def_value
        self.triangle_list = [[def_value]*i for i in range(1, self.len)]
    
    def set_position(self, poss:list) -> tuple:
        if poss[0] < poss[1]:
            x, y = poss[1], poss[0]
        else:
            x, y = poss[0], poss[1]
        return x - 1, y

    def __setitem__(self, poss:tuple, value) -> None:
        poss = self.set_position(poss)
        self.triangle_list[poss[0]][poss[1]] = value
    
    def __getitem__(self, poss:tuple):
        if poss[0] == poss[1] and poss[0] < len(self):
            return self.def_value
        poss = self.set_position(poss)
        return self.triangle_list[poss[0]][poss[1]]

    def make_new_line(self):
        self.len += 1
        if self.len >= 2:
            self.triangle_list.append([self.def_value]*(len(self)-1)) 

    def remove_line(self):
        self.len -= 1
        del self.triangle_list[-1]

    def __str__(self) -> str:
        str_res = '    '+str([i for i in range(len(self))])[1:-1] + '\n'
        #str_res += '  '+'_'*(self.len-1)*3 + '\n'
        str_res += '0 | #\n'
        for i, line in enumerate(self.triangle_list):
            str_res += f'{1+i} | '+str(line)[1:-1] + '  #\n'
        return str_res[:-1]

    def __repr__(self) -> str:
        return str(self)

    def __len__(self):
        return self.len
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    #A = Triangle()
    #A.make_new_line()
    #A.make_new_line()
    #A.make_new_line()
    #print(A)
    #print(A.set_position([2, 0]))
