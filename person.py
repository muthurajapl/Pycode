class Person:
    def __init__(self, name, job = None, pay = 0):
        self.name = name
        self.job = job
        self.pay = pay
        
if __name__ == '__main__':
    #self-test codebob
    bob = Person('Bob Smith', job = None, pay =100)
    sue = Person("Sue Jones", job = 'dev', pay = 100000)
    print ('{1} {0}'.format(bob.pay, bob.name.split()[-1]))
    print ('%s %s' % (sue.name.split(), sue.pay))
        
        