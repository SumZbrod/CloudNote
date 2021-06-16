class Triangle:
    """
    Square commutative list implemented via triangular list
    """
    def __init__(self, l=0):
        self.triangle_list = [[0]*i for i in range(1, l)]
    
    def set_position(poss:tuple) -> tuple:
        return poss[0], poss[1] if poss[0] < poss[1] else poss[1], poss[0]

    def __setitem__(self, poss:tuple, value) -> None:
        poss = self.set_position(poss)
        self.triangle_list[poss[0], poss[1]] = value
    
    def __getitem__(self, poss:tuple):
        poss = self.set_position(poss)
        return self.triangle_list[poss[0], poss[1]]


if __name__ == '__main__':
    pass
        
         