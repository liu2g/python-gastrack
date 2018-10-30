# Author      : Zuguang Liu
# Date        : 2018-10-28 23:53:41
# Python Ver  : 3.6
# Description : 

class Foo(object):
    def _get_bar(self):
        return self.__bar
    def _set_bar(self, value):
        if not isinstance(value, int):
            raise TypeError("bar must be set to an integer")
        self.__bar = value
    bar = property(_get_bar, _set_bar)

f = Foo()
f.bar = "three"