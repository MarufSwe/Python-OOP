class Hello:
    def __init__(self, name):
        self.a = 10
        self._b = 20
        self.__c = 30
        print(self.__c)

hello = Hello('name')
print(hello.a)
print(hello._b)
print(hello.__c)