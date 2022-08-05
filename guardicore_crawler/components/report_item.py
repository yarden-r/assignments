import imp


from abc import ABC, abstractmethod

"""
    Abstract class for report item.
"""


class ReportItem(ABC):
    def __init__(self,name:str):
        self.name = name

    @abstractmethod
    def __str__(self):
        pass
