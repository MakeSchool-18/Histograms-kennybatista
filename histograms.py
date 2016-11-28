#!python


from __future__ import division, print_function


class Dictogram(dict):
    # here we're Initializing the class, but not giving it values yet.
    # We give it values in line 23
    def __init__(self, iterable=None):
        """Initialize this histogram as a new dict; update with given items"""
        super(Dictogram, self).__init__()
        self.types = 0  # the number of distinct item types in this histogram
        self.tokens = 0  # the total count of all item tokens in this histogram
        if iterable:
            self.update(iterable)

    def update(self, iterable):
        """Update this histogram with the items in the given iterable"""
        for item in iterable:
            # TODO: increment item count
            if self.get(item) is not None:
                self.tokens += 1
                self[item] += 1 # increase it's val if it already exists
            else:
                self[item] = 1 # because the item doesn't exist, we set the default val to 1
                self.tokens += 1
                self.types += 1



    def count(self, item):
        """Return the count of the given item in this histogram, or 0"""
        if item in self:
            return self[item]
        else:
            return 0


class Listogram(list):

    def __init__(self, iterable=None):
        """Initialize this histogram as a new list; update with given items"""
        super(Listogram, self).__init__()
        self.types = 0  # the number of distinct item types in this histogram
        self.tokens = 0  # the total count of all item tokens in this histogram
        if iterable:
            self.update(iterable)

    def update(self, iterable):
        """Update this histogram with the items in the given iterable"""
        for item in iterable:
            index = self._index(item)
            if index is None:
                self.append((item, 1))
                self.types += 1
                self.tokens += 1
            else:
                count = self[index][1]
                self[index] = (item, count + 1)
                self.tokens = 1


    def count(self, item):
        """Return the count of the given item in this histogram, or 0"""
        index = self._index(item)
        if index is None:
            return 0
        else:
            return self[index][1]

    def __contains__(self, item):
        """Return True if the given item is in this histogram, or False"""
        if self._index(item) is None:
            return False
        else:
            return True

    def _index(self, target):
        """Return the index of the (target, count) entry if found, or None"""
        for index, (word, count) in enumerate(self):
            if word == target:
                return index
        return None


def test_histogram(text_list):
    print('text list:', text_list)

    hist_dict = Dictogram(text_list)
    print('dictogram:', hist_dict)

    hist_list = Listogram(text_list)
    print('listogram:', hist_list)


def read_from_file(filename):
    """Parse the given file into a list of strings, separated by seperator."""
    return file(filename).read().strip().split()


if __name__ == '__main__':
    import sys
    arguments = sys.argv[1:]  # exclude script name in first argument
    if len(arguments) == 0:
        # test hisogram on letters in a word
        word = 'abracadabra'
        test_histogram(word)
        print()
        # test hisogram on words in a sentence
        sentence = 'one fish two fish red fish blue fish'
        word_list = sentence.split()
        test_histogram(word_list)
    elif len(arguments) == 1:
        # test hisogram on text from a file
        filename = arguments[0]
        text_list = read_from_file(filename)
        test_histogram(text_list)
    else:
        # test hisogram on given arguments
        test_histogram(arguments)
