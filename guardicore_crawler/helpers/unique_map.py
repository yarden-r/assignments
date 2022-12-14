
class UniqueMap(object):
    """
    This map will only contain unique values.
    """
    def __init__(self):
        self.map = {}

    def insert(self, key, value):
        if self.contains(key, value):
<<<<<<< HEAD
            self.map[key] = value
=======
            return False
        self.map[key] = value
        return True
>>>>>>> 16526ccb1471151ed68a24deaea3638eb22cc87e
        
    def contains(self, key, value):
        if key in self.map and self.map[key] == value:
            return True
        return False

    def get(self, key):
        return self.map[key]

    def get_all(self):
        return self.map.values()

    def __str__(self):
        return str(self.map)

    def __len__(self):
        return len(self.map)
