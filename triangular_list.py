class Triangle:
    """
    Square commutative list implemented via triangular list
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
    >>> print(A)
        0, 1, 2, 3, 4
    0 | #
    1 | 0  #
    2 | 0, 0  #
    3 | 0, 0, 1  #
    4 | 0, 0, 0, 0  #
    """
    def __init__(self, l=0, def_value=0):
        self.l = l
        self.def_value = def_value
        self.triangle_list = [[def_value]*i for i in range(1, self.l)]
    
    def set_position(self, poss:list) -> tuple:
        if poss[0] > poss[1]:
            x, y = poss[1], poss[0]
        else:
            x, y = poss[0], poss[1]
        return x, y - 1

    def __setitem__(self, poss:tuple, value) -> None:
        poss = self.set_position(poss)
        self.triangle_list[poss[0]][poss[1]] = value
    
    def __getitem__(self, poss:tuple):
        poss = self.set_position(poss)
        return self.triangle_list[poss[0]][poss[1]]

    def make_new_line(self):
        self.triangle_list.append([self.def_value]*self.l) 

    def __str__(self) -> str:
        str_res = '    '+str([i for i in range(self.l)])[1:-1] + '\n'
        #str_res += '  '+'_'*(self.l-1)*3 + '\n'
        str_res += '0 | #\n'
        for i, line in enumerate(self.triangle_list):
            str_res += f'{1+i} | '+str(line)[1:-1] + '  #\n'
        return str_res[:-1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()

         