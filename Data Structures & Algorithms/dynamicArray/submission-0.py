class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = [None] * capacity
        self.current_index = 0


    def get(self, i: int) -> int:
        return self.capacity[i]

    def set(self, i: int, n: int) -> None:
        self.capacity[i] = n
        if i >= self.current_index:
            self.current_index = i+1

    def pushback(self, n: int) -> None:
        if (self.current_index) >= len(self.capacity):
            self.resize()
        self.capacity[self.current_index] = n
        self.current_index += 1

    def popback(self) -> int:
        poped_element = self.capacity[self.current_index-1]
        self.capacity[self.current_index-1] = None
        self.current_index -= 1
        return poped_element

    def resize(self) -> None:
        self.capacity += [None] * len(self.capacity)

    def getSize(self) -> int:
        return self.current_index
    
    def getCapacity(self) -> int:
        return len(self.capacity)
