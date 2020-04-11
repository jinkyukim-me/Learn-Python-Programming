# When you define a class
class Tea(Base1, Base2):
    party = 'Elice'

    def Coding(self):
        return 'Build Projects'


# Python essentially does this
def Coding(self):
    return 'Build Projects'
body = {'party':'Elice', 'Coding': Coding}
Tea = type('Tea', (Base1, Base2), body)

