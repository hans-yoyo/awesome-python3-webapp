import orm

from models import User

def test():
    print('test start')
    yield from orm.create_pool(user='root', password='root', db='py_awesome')
    print('test start - step 2')
    user = User(name='Hyman', email='hyman213@163.com', passwd='123456', image='about:blank')
    print('test start - step 3')
    yield from user.save()


for x in test():
    pass