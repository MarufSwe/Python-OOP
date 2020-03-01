class Language:
    java = 'Maruf'
    python = 'Galib'
    php = 'Johny'


class SubClass(Language):
    def callSuper(self):
        self.php


sub = SubClass()
print(sub.php)

