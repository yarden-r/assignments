

"""
    This class makes sure that only one instance of a derived class is created.
"""
class Singleton:

    def __new__(cls, *args, **kwargs):
    
        """
            since __new__ is called when an instance of the class is created,
            we can use it to check if the instance already exists.
            if it does, we return the instance, otherwise we create a new one.
        """
    
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

