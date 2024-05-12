class Queue:
    def __init__(self):
        self.__items = []

    def enqueue(self, item):
        self.__items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.__items.pop(0)

    def is_empty(self):
        return len(self.__items) == 0

    def size(self):
        return len(self.__items)
    
    def __iter__(self):
        return iter(self.__items)

class Node:
    def __init__(self, key: float | None = None, value: float | None = None) -> None:
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.count = 0

class BST:
    def __init__(self):
        self.__root = None # Representa o nó da raíz da Binary Search Tree
    
    # Associa o valor à chave na BST
    def put(self, key: int, val: str):
        self.__root = self.__put(self.__root, key, val)

    # Associa o valor à chave na BST. Se o nó já existir, substitui o seu valor pelo recebido
    def __put(self, x: Node, key: int, val: str):
        if x is None:
            return Node(key, val)
        if key == x.key:
            x.value = val
        elif key > x.key:
            x.right = self.__put(x.right, key, val)
        else: # key < x.key
            x.left = self.__put(x.left, key, val)
        x.count = 1 + self.size(x.left) + self.size(x.right)
        return x

    # Devolve a posição da chave key
    def rank(self, key: int):
        return self.__rank(key, self.__root)
    
    def __rank(self, key: int, x: Node):
        if x is None:
            return 0
        if x.key == key:
            return self.size(x.left)
        elif key < x.key:
            return self.__rank(key, x.left)
        else: # key > x.key
            return 1 + self.size(x.left) + self.__rank(key, x.right)
 
    # Devolve o valor double correspondente à chave recebida, ou 0 se não encontrar a chave
    def get(self, key: int):
        x = self.__root
        while x:
            if key == x.key:
                return x.value
            elif key > x.key:
                x = x.right
            elif key < x.key:
                x = x.left
        return 0
    
    # Devolve o tamanho da BST
    def size(self, x: Node):
        if x is None:
            return 0
        return x.count

    # Devolve a chave do nó k
    def select(self, key: int):
        return self.__select(self.__root, key)

    # Devolve o Nó que contém a key da classificação (rank) k
    def __select(self, x: Node, key: int):
        if x is None:
            return None
        left_size = self.size(x.left)
        if left_size == key:
            return x
        elif left_size > key:
            return self.__select(x.left, key)
        else: #left_size < k
            return self.__select(x.right, key - left_size - 1)

    # Iterador de chaves
    def keys(self):
        q = Queue()
        self.inorder(self.__root, q)
        return q
    
    def inorder(self, x: Node, q: Queue):
        if x is None:
            return
        self.inorder(x.left, q)
        q.enqueue(x.key)
        self.inorder(x.right, q)

    # Verifica se o rank e o select devolve a classificação e chave correta.
    def checkRankSelect(self):
        for i in range(self.size(self.__root)):
            key = self.select(i).key
            if i != self.rank(key):
                return False
            if key != self.select(self.rank(key)).key:
                return False
        return True

def main():
    bst = BST()

    #preenche a BST
    max = int(input())
    for _ in range(max):
        num, txt = input().split(" ")
        num = int(num)
        bst.put(num, txt)
    print(bst.checkRankSelect())
    for k in bst.keys():
        print(k)

if __name__ == "__main__":
    main()