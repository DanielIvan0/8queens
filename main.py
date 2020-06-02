class Path:
    def __init__(self, n):
        self._max = n
        self._path = []
        self._result = []
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
        aux1 = i + j in [k + self._path[k] for k in range(len(self._path))]
        aux2 = i - j in [k - self._path[k] for k in range(len(self._path))]
        return aux0 or aux1 or aux2
    
def queensDumbBattle(n):
    path = Path(n)
    for i in range(n):
        expand(path, i)
    print(f'result -> {path.result}')

def expand(path, root):
    path.path.append(root)
    if len(path.path) == path.max:
        path.addPath(path.path)
    else:
        nudes = path.expandNode()
        for nude in nudes:
            expand(path, nude)
    path.path.pop()

queensDumbBattle(8)