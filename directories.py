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
        # Directories when listed should be sorted by the parent
        sorted_keys = sorted(self.child.keys())
        for name in sorted_keys:
            print('  ' * depth + name)
            self.child[name].list(depth + 1)

    def delete(self, path):
        parts = path.split('/')
        parent = self.get_parent(parts[:-1])

        if parent and parts[-1] in parent.child:
            del parent.child[parts[-1]]
        else:
            missing_path = []

            for part in parts:
                if part in self.child:
                    self = self.child[part]
                else:
                    missing_path.append(part)
                    break
            print(f"Cannot delete {path} - {'/'.join(missing_path)} does not exist")

    def move(self, src, dest):
        src_parts = src.split('/')
        dest_parts = dest.split('/')

        src_parent = self.get_parent(src_parts[:-1])
        if not src_parent or src_parts[-1] not in src_parent.child:
            print(f"Cannot move {src} - {src} does not exist")
            return

        src_dir = src_parent.child.pop(src_parts[-1])

        for part in dest_parts:
            if part not in self.child:
                self.child[part] = Directory(part, self)
            self = self.child[part]

        self.child[src_dir.name] = src_dir
        src_dir.parent = self




    def get_parent(self, parts):
        # Takes in a split directory path and attempts to locate the parent
        for part in parts:
            if part not in self.child:
                return None # If any part of the path doesn't exist, return None
            self = self.child[part]
        return self


