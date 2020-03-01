class Tree:
    class Position:
        """Abstraction representing the location of single element"""
        def element(self):
            raise NotImplementedError("Must be implemented by subclass")
        
        def __eq__(self, other):
            """ Return True if other position represents the same location"""
            raise NotImplementedError("Must be implemented by subclass")
        
        def __ne__(self, other):
            """ Return True if other position does not represents the same location"""
            return not(self == other)

    def root(self):
        raise NotImplementedError("Must be implemented by subclass")

    def parent(self, p):
        """ Return Position representing p's parent or None if p is root """
        raise NotImplementedError("Must be implemented by subclass")   

    def num_children(self, p):
        """ Return the number of children that position p has"""
        raise NotImplementedError("Must be implemented by subclass")

    def children(self, p):
        """Generate an iteration of Positions representing p's children"""
        raise NotImplementedError("Must be implemented by subclass")

    def __len__(self):
        """Return total number of elements in the tree"""
        raise NotImplementedError("Must be implemented by subclass")

    def is_root(self, p):
        """Return True if Position p representation the root of the tree"""
        return self.root() == p

    def is_leaf(self, p):
        """Return True if Position p have no children"""
        return self.num_children(p) == 0
    
    def is_empty(self):
        """Return True if tree is empty"""
        return len(self) == 0

    def depth(self, p):
        """Return the number of levels separating Position p from the root"""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def height1(self):
        """Return the height of the tree"""
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def _height2(self, p):
        """Return the height of the subtree rooted at Position p"""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))
    
    def height(self, p=None):
        """ Return the height of the subtree rooted t Position p
        if p is None, return the height of the entire tree
        """
        if p is None:
            p = self.root()
        return self._height2(p)

