class Vector:
    def __init__(self, elements=[]):
        self.elements = elements
        self.size = len(elements)
        self.capacity = len(elements)

    def __str__(self):
        return str([x for x in self.elements if x is not None])

    def __len__(self):
        return len([x for x in self.elements if x is not None])

    def __iter__(self):
        for element in self.elements:
            yield element

    def __getitem__(self, index):
        return self.get(index)

    def get(self, index):
        if 0 <= index < self.size:
            return self.elements[index]
        else:
            raise Exception("Index out of range")

    def info(self, heading=''):
        print(f"\n==================={('  ' + heading + '  ') if heading != '' else ''}====================")
        print(f"|  size = {self.size}")
        print(f"|  capacity = {self.capacity}")
        print(f"|  not None elements = {[x for x in self.elements if x is not None]}")
        print(f"|  all elements = {[x for x in self.elements]}")
        print("========================================\n")

    def add(self, element):
        if self.capacity == 0:
            self.size = 1
            self.elements = [element] + [None for _ in range(self.size)]
            self.capacity = len(self.elements)

        elif self.size == self.capacity:  # все элементы массива заняты
            self.elements = self.elements + [None for _ in range(self.size)]
            self.capacity = len(self.elements)
            self.elements[self.size] = element
            self.size += 1

        else:  # есть свободное место
            self.elements[self.size] = element
            self.size += 1

    def insert(self, value, index):
        if index < 0 or index > self.size:
            raise Exception("Index out of range")
        if index == self.size:  # добавление в конец массива
            self.add(value)
        else:
            if self.size == self.capacity:  # нет свободных элементов
                self.elements = self.elements + [None for _ in range(self.size)]
                self.capacity = len(self.elements)
            for i in range(self.size + 1):
                if i < index:
                    self.elements[i] = self.elements[i]
                elif i > index:
                    self.elements[i] = self.elements[i - 1]
            self.elements[index] = value
            self.size += 1

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise Exception("Index out of range")
        if index == self.size - 1:
            self.remove_back()
        else:
            self.elements[index] = None
            for i in range(index, self.size - 1):
                self.elements[i] = self.elements[i + 1]
            self.size -= 1
            self.elements[self.size] = None

    def remove_back(self):
        if len(self.elements) == 0:
            raise Exception("No elements in the array")
        self.elements[self.size - 1] = None
        self.size -= 1


class Program:
    if __name__ == "__main__":
        array = Vector([1, 2, 3, 4])

        print(array)

        array.insert(5, 3)
        array.info(heading="Вставка элемента по индексу")

        array.remove(2)
        array.info(heading="Удаление элемента с конца")
