from enum import Enum

class WorkType(Enum):
    PARTIME = 'PT'
    FULLTIME = 'FT'
    
    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class Team(Enum):
    DATA = 'DT'
    RECRUITMENT = 'RH'
    MARKETING = 'DM'
    
    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]