class GlobalStorage:
    debug = False
    _share = {}

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(GlobalStorage, cls).__new__(cls)
        return cls.instance

    def __setattr__(self, key, value):
        self.__dict__[key] = value
        if self.debug:
            print(f"parameter {key} was set")

    def __getattr__(self, item):
        return self.__dict__[item]
