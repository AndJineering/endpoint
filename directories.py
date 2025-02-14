class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.child = {}

    def add(self, path):
        parts = path.split('/')
        for part in parts:
            if part not in self.child:
                self.child[part] = Directory(part, self)
            self = self.child[part]

    def list(self, depth=0):
        sorted_keys = sorted(self.child.keys())
        for name in sorted_keys:
            print('  ' * depth + name)
            self.child[name].list(depth + 1)
