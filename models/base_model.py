class BaseModel():


    @classmethod
    def from_entity(cls, *args, **kwargs):
        raise NotImplementedError

    def to_entity(self, *args, **kwargs):
        raise NotImplementedError