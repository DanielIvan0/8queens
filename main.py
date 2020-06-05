from math import ceil
class Path:
    def __init__(self, n):
        self._max = n
        self._path = []
        self._result = []
        self._notAvSum = []
        self._notAvRest = []
    @property
    def path(self):
        return self._path
    @property
    def max(self):
        return self._max
    @property
    def result(self):
        return self._result
    def addPath(self, r):
        self._result.append(r.copy())
    def append(self, node):
        self._notAvSum.append(len(self._path) + node)
        self._notAvRest.append(len(self._path) - node)
        self._path.append(node)
    def pop(self):
        self._notAvSum.pop()
        self._notAvRest.pop()
        self._path.pop()
    def expandNode(self):
        response = []
        if len(self.path) < self._max:
            i = len(self._path)
            for j in range(self._max):
                if not self.inPathOfDeath(i, j):
                    response.append(j)
        return response
    def inPathOfDeath(self, i, j):
        aux0 = j in self._path
        aux1 = i + j in self._notAvSum
        aux2 = i - j in self._notAvRest
        return aux0 or aux1 or aux2
    
def queensDumbBattle(n):
    path = Path(n)
    for i in range(n):
        expand(path, i)
    return [[(i, item[i]) for i in range(len(item))] for item in path.result]

def expand(path, root):
    path.append(root)
    if len(path.path) == path.max:
        path.addPath(path.path)
    else:
        nudes = path.expandNode()
        for nude in nudes:
            expand(path, nude)
    path.pop()