import abc

class DictionaryImplementor():
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def search(entry,val):
        pass

    @abc.abstractmethod
    def insert(entry,val):
        pass

    @abc.abstractmethod
    def delete(entry,val):
        pass

    @abc.abstractmethod
    def sort(entry):
        pass
