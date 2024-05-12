class Node:
    def __init__(self, key: float | None = None, value: float | None = None) -> None:
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.count = 0

class BST:
    def __init__(self):
        self.__root = Node() # Representa o nó da raíz da Binary Search Tree
    
    # Associa o valor à chave na BST
    def put(self, key, val):
        self.__root = self.put(self.__root, key, val)

    # Associa o valor à chave na BST. Se o nó já existir, substitui o seu valor pelo recebido
    def put(self, x: Node, key, val):
        
        if x is None:
            return Node(key, val)
        if key == x.key:
            x.value = val
        elif key > x.key:
            x.right = self.put(x.right, key, val)
        else: # key < x.key
            x.left = self.put(x.left, key, val)
        x.count = 1 + self.size(x.left) + self.size(x.right)

    # Devolve a posição da chave key
    def rank(self, key):
        pass
    
    def rank(self, key, x):
        pass
 
    # Devolve o valor double correspondente à chave recebida, ou 0 se não encontrar a chave
    def get(self, key):
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
    def size(self):
        return self.__root.count

    # Devolve a chave do nó k
    def select(self, k):
        pass

    # Devolve o Nó que contém a key da classificação (rank) k
    def select(self, x, k):
        pass

    # Iterador de chaves
    def keys(self):
        pass
    
    def inorder(self, x, q):
        pass

    # Verifica se o rank e o select devolve a classificação e chave correta.
    def checkRankSelect(self):
        pass

def main():
    bst = BST()

    #preenche a BST
    max = int(input())
    for _ in range(max):
        num, txt = input().split(" ")
        num = int(num)
        bst.put(num, txt)
    print(bst.checkRankSelect())

if __name__ == "__main__":
    main()